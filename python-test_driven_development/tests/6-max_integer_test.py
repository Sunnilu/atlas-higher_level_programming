#!/usr/bin/python3/**
 *    Copyright (C) 2018-present MongoDB, Inc.
 *
 *    This program is free software: you can redistribute it and/or modify
 *    it under the terms of the Server Side Public License, version 1,
 *    as published by MongoDB, Inc.
 *
 *    This program is distributed in the hope that it will be useful,
 *    but WITHOUT ANY WARRANTY; without even the implied warranty of
 *    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *    Server Side Public License for more details.
 *
 *    You should have received a copy of the Server Side Public License
 *    along with this program. If not, see
 *    <http://www.mongodb.com/licensing/server-side-public-license>.
 *
 *    As a special exception, the copyright holders give permission to link the
 *    code of portions of this program with the OpenSSL library under certain
 *    conditions as described in each individual source file and distribute
 *    linked combinations including the program with the OpenSSL library. You
 *    must comply with the Server Side Public License in all respects for
 *    all of the code used other than as permitted herein. If you modify file(s)
 *    with this exception, you may extend this exception to your version of the
 *    file(s), but you are not obligated to do so. If you do not wish to do so,
 *    delete this exception statement from your version. If you delete this
 *    exception statement from all source files in the program, then also delete
 *    it in the license file.
 */

/*
 * A C++ unit testing framework.
 *
 * Most users will include the umbrella header "mongo/unittest/unittest.h".
 *
 * For examples of basic usage, see mongo/unittest/unittest_test.cpp.
 *
 * ASSERT macros and supporting definitions are in mongo/unittest/assert.h.
 *
 */

#pragma once

#include <boost/filesystem/operations.hpp>
#include <boost/filesystem/path.hpp>
#include <boost/optional.hpp>
#include <cmath>
#include <fmt/format.h>
#include <functional>
#include <optional>
#include <sstream>
#include <string>
#include <tuple>
#include <type_traits>
#include <utility>
#include <vector>

#include "mongo/base/status_with.h"
#include "mongo/base/string_data.h"
#include "mongo/logv2/log_debug.h"
#include "mongo/logv2/log_detail.h"
#include "mongo/unittest/test_info.h"
#include "mongo/util/assert_util.h"
#include "mongo/util/optional_util.h"
#include "mongo/util/str.h"
#include "mongo/util/synchronized_value.h"

/**
 * Construct a single test, named `TEST_NAME` within the test Suite `SUITE_NAME`.
 *
 * Usage:
 *
 * TEST(MyModuleTests, TestThatFooFailsOnErrors) {
 *     ASSERT_EQUALS(error_success, foo(invalidValue));
 * }
 */
#define TEST(SUITE_NAME, TEST_NAME) \
    UNIT_TEST_DETAIL_DEFINE_TEST_(SUITE_NAME, TEST_NAME, ::mongo::unittest::Test)

/**
 * Construct a single test named TEST_NAME that has access to a common class (a "fixture")
 * named "FIXTURE_NAME". FIXTURE_NAME will be the name of the Suite in which the test appears.
 *
 * Usage:
 *
 * class FixtureClass : public mongo::unittest::Test {
 * protected:
 *   int myVar;
 *   void setUp() { myVar = 10; }
 * };
 *
 * TEST(FixtureClass, TestThatUsesFixture) {
 *     ASSERT_EQUALS(10, myVar);
 * }
 */
#define TEST_F(FIXTURE_NAME, TEST_NAME) \
    UNIT_TEST_DETAIL_DEFINE_TEST_(FIXTURE_NAME, TEST_NAME, FIXTURE_NAME)

#define UNIT_TEST_DETAIL_DEFINE_TEST_(SUITE_NAME, TEST_NAME, TEST_BASE) \
    UNIT_TEST_DETAIL_DEFINE_TEST_PRIMITIVE_(                            \
        SUITE_NAME, TEST_NAME, UNIT_TEST_DETAIL_TEST_TYPE_NAME(SUITE_NAME, TEST_NAME), TEST_BASE)

#define UNIT_TEST_DETAIL_DEFINE_TEST_PRIMITIVE_(FIXTURE_NAME, TEST_NAME, TEST_TYPE, TEST_BASE) \
    class TEST_TYPE : public TEST_BASE {                                                       \
    private:                                                                                   \
        void _doTest() override;                                                               \
        static inline const ::mongo::unittest::TestInfo _testInfo{                             \
            #FIXTURE_NAME, #TEST_NAME, __FILE__, __LINE__};                                    \
        static inline const RegistrationAgent<TEST_TYPE> _agent{&_testInfo};                   \
    };                                                                                         \
    void TEST_TYPE::_doTest()

/**
 * Macro to construct a type name for a test, from its `SUITE_NAME` and `TEST_NAME`.
 * Do not use directly in test code.
 */
#define UNIT_TEST_DETAIL_TEST_TYPE_NAME(SUITE_NAME, TEST_NAME) \
    UnitTest_SuiteName##SUITE_NAME##TestName##TEST_NAME

namespace mongo::unittest {

class Result;

/**
 * Representation of a collection of tests.
 *
 * One Suite is constructed for each SUITE_NAME when using the TEST macro.
 *
 * See `OldStyleSuiteSpecification` which adapts dbtests into this framework.
 */
class Suite : public std::enable_shared_from_this<Suite> {
private:
    struct SuiteTest {
        std::string name;
        std::string fileName;
        std::function<void()> fn;
    };

    struct ConstructorEnable {
        explicit ConstructorEnable() = default;
    };

public:
    explicit Suite(ConstructorEnable, std::string name);
    Suite(const Suite&) = delete;
    Suite& operator=(const Suite&) = delete;

    void add(std::string name, std::string fileName, std::function<void()> testFn);

    std::unique_ptr<Result> run(const std::string& filter,
                                const std::string& fileNameFilter,
                                int runsPerTest);

    static int run(const std::vector<std::string>& suites,
                   const std::string& filter,
                   const std::string& fileNameFilter,
                   int runsPerTest);

    /**
     * Get a suite with the given name, creating and registering it if necessary.
     * This is the only way to make a Suite object.
     *
     * Safe to call during static initialization.
     */
    static Suite& getSuite(StringData name);

private:
    /** Points to the string data of the _name field. */
    StringData key() const {
        return _name;
    }

    std::string _name;
    std::vector<SuiteTest> _tests;
};

/**
 * Adaptor to set up a Suite from a dbtest-style suite.
 * Support for deprecated dbtest-style test suites. Tests are are added by overriding setupTests()
 * in a subclass of OldStyleSuiteSpecification, and defining an OldStyleSuiteInstance<T> object.
 * This approach is
 * deprecated.
 *
 * Example:
 *     class All : public OldStyleSuiteSpecification {
 *     public:
 *         All() : OldStyleSuiteSpecification("BunchaTests") {}
 *         void setupTests() {
 *            add<TestThis>();
 *            add<TestThat>();
 *            add<TestTheOtherThing>();
 *         }
 *     };
 *     OldStyleSuiteInitializer<All> all;
 */
class OldStyleSuiteSpecification {
public:
    struct SuiteTest {
        std::string name;
        std::function<void()> fn;
    };

    OldStyleSuiteSpecification(std::string name) : _name(std::move(name)) {}
    virtual ~OldStyleSuiteSpecification() = default;

    // Note: setupTests() is run by a OldStyleSuiteInitializer at static initialization time.
    // It should in most cases be just a simple sequence of add<T>() calls.
    virtual void setupTests() = 0;

    const std::string& name() const {
        return _name;
    }

    const std::vector<SuiteTest>& tests() const {
        return _tests;
    }

    /**
     * Add an old-style test of type `T` to this Suite, saving any test constructor args
     * that would be needed at test run time.
     * The added test's name will be synthesized as the demangled typename of T.
     * At test run time, the test will be created and run with `T(args...).run()`.
     */
    template <typename T, typename... Args>
    void add(Args&&... args) {
        addNameCallback(nameForTestClass<T>(), [=] { T(args...).run(); });
    }

    void addNameCallback(std::string name, std::function<void()> cb) {
        _tests.push_back({std::move(name), std::move(cb)});
    }

    template <typename T>
    static std::string nameForTestClass() {
        return demangleName(typeid(T));
    }

private:
    std::string _name;
    std::vector<SuiteTest> _tests;
};

/**
 * Define a namespace-scope instance of `OldStyleSuiteInitializer<T>` to properly create and
 * initialize an instance of `T` (an `OldStyleSuiteSpecification`). See
 * `OldStyleSuiteSpecification`.
 */
template <typename T>
struct OldStyleSuiteInitializer {
    template <typename... Args>
    explicit OldStyleSuiteInitializer(Args&&... args) {
        T t(std::forward<Args>(args)...);
        init(t);
    }

    void init(OldStyleSuiteSpecification& suiteSpec) const {
        suiteSpec.setupTests();
        auto& suite = Suite::getSuite(suiteSpec.name());
        for (auto&& t : suiteSpec.tests()) {
            suite.add(t.name, "", t.fn);
        }
    }
};

/**
 * UnitTest singleton class. Provides access to information about current execution state.
 */
class UnitTest {
    UnitTest() = default;

public:
    static UnitTest* getInstance();

    UnitTest(const UnitTest& other) = delete;
    UnitTest& operator=(const UnitTest&) = delete;

public:
    /**
     * Returns the currently running test, or `nullptr` if a test is not running.
     */
    const TestInfo* currentTestInfo() const;

public:
    /**
     * Used to set/unset currently running test information.
     */
    class TestRunScope {
    public:
        explicit TestRunScope(const TestInfo* testInfo) {
            UnitTest::getInstance()->setCurrentTestInfo(testInfo);
        }

        ~TestRunScope() {
            UnitTest::getInstance()->setCurrentTestInfo(nullptr);
        }
    };

private:
    /**
     * Sets the currently running tests. Internal: should only be used by unit test framework.
     * testInfo - test info of the currently running test, or `nullptr` is a test is not running.
     */
    void setCurrentTestInfo(const TestInfo* testInfo);

private:
    const TestInfo* _currentTestInfo = nullptr;
};

/**
 * Base type for unit test fixtures.  Also, the default fixture type used
 * by the TEST() macro.
 */
class Test {
public:
    Test();
    virtual ~Test();
    Test(const Test&) = delete;
    Test& operator=(const Test&) = delete;

    void run();

    /**
     * Called on the test object before running the test.
     */
    virtual void setUp() {}

    /**
     * Called on the test object after running the test.
     */
    virtual void tearDown() {}

protected:
    /**
     * Adds a Test to a Suite, used by TEST/TEST_F macros.
     */
    template <typename T>
    class RegistrationAgent {
    public:
        /**
         * These TestInfo must point to data that outlives this RegistrationAgent.
         * In the case of TEST/TEST_F, these are static variables.
         */
        explicit RegistrationAgent(const TestInfo* testInfo) : _testInfo{testInfo} {
            Suite::getSuite(_testInfo->suiteName())
                .add(
                    std::string{_testInfo->testName()}, std::string{_testInfo->file()}, [testInfo] {
                        UnitTest::TestRunScope trs(testInfo);
                        T{}.run();
                    });
        }

        StringData getSuiteName() const {
            return _testInfo->suiteName();
        }

        StringData getTestName() const {
            return _testInfo->testName();
        }

        StringData getFileName() const {
            return _testInfo->file();
        }

    private:
        const TestInfo* _testInfo;
    };

    /**
     * This exception class is used to exercise the testing framework itself. If a test
     * case throws it, the framework would not consider it an error.
     */
    class FixtureExceptionForTesting : public std::exception {};

    /**
     * Starts capturing messages logged by code under test.
     *
     * Log messages will still also go to their default destination; this
     * code simply adds an additional sink for log messages.
     *
     * Clears any previously captured log lines.
     */
    void startCapturingLogMessages();

    /**
     * Stops capturing log messages logged by code under test.
     */
    void stopCapturingLogMessages();

    /**
     * Gets a vector of strings, one log line per string, captured since
     * the last call to startCapturingLogMessages() in this test.
     */
    std::vector<std::string> getCapturedTextFormatLogMessages() const;
    std::vector<BSONObj> getCapturedBSONFormatLogMessages() const;

    /**
     * Returns the number of collected log lines containing "needle".
     */
    int64_t countTextFormatLogLinesContaining(const std::string& needle);

    /**
     * Returns the number of collected log lines where "needle" is a subset of a line.
     *
     * Does a Depth-First-Search of a BSON document. Validates each element in "needle" exists in
     * "haystack". It ignores extra elements in "haystack".
     *
     * In example haystack:     { i : 1, a : { b : 1 } },
     * a valid needles include: { i : 1}  or  {a : { b : 1}}
     * It will not find { b: 1 } since it does not search recursively for sub-tree matches.
     *
     * If a BSON Element is undefined, it simply checks for its existence, not its type or value.
     * This allows callers to test for the existence of elements in variable length log lines.
     */
    int64_t countBSONFormatLogLinesIsSubset(const BSONObj& needle);

    /**
     * Prints the captured log lines.
     */
    void printCapturedTextFormatLogLines() const;

private:
    /**
     * The test itself.
     */
    virtual void _doTest() = 0;
};

/**
 * Return a list of suite names.
 */
std::vector<std::string> getAllSuiteNames();

/** Invocation info (used e.g. by death test to exec). */
struct SpawnInfo {
    /** Copy of the original `argv` from main. */
    std::vector<std::string> argVec;
    /** If nonempty, this process is a death test respawn. */
    std::string internalRunDeathTest;
    /**
     * A unit test main has to turn this on to indicate that it can be brought to
     * the death test from a fresh exec with `--suite` and `--filter` options.
     * Otherwise death tests simply fork. See death_test.cpp.
     */
    bool deathTestExecAllowed = false;
};
SpawnInfo& getSpawnInfo();

struct AutoUpdateConfig {
    bool updateFailingAsserts = false;
    bool revalidateAll = false;
    boost::filesystem::path executablePath;
};

AutoUpdateConfig& getAutoUpdateConfig();

}  // namespace mongo::unittest
'''Unittest for max_integer([..])
'''
import unittest
max_integer = __import__('6-max_integer').max_integer

# File: tests/6-max_integer_test.py

import unittest
from max_integer import max_integer

class TestMaxInteger(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_single_element_list(self):
        self.assertEqual(max_integer([5]), 5)

    def test_duplicate_values(self):
        self.assertEqual(max_integer([3, 3, 3]), 3)

    def test_float_numbers(self):
        self.assertAlmostEqual(max_integer([1.5, 2.5, 3.5]), 3.5)
class TestStringMethods(unittest.TestCase):

  def test_upper(self):
      self.assertEqual('foo'.upper(), 'FOO')

  def test_isupper(self):
      self.assertTrue('FOO'.isupper())
      self.assertFalse('Foo'.isupper())

  def test_split(self):
      s = 'hello world'
      self.assertEqual(s.split(), ['hello', 'world'])
      # check that s.split fails when the separator is not a string
      with self.assertRaises(TypeError):
          s.split(2)
class SimpleWidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget('The widget')

    def test_default_widget_size(self):
        self.assertEqual(self.widget.size(), (50,50),
                         'incorrect default size')

    def test_widget_resize(self):
        self.widget.resize(100,150)
        self.assertEqual(self.widget.size(), (100,150),
                         'wrong size after resize')
class SimpleWidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget('The widget')

    def tearDown(self):
        self.widget.dispose()
    def suite():
    suite = unittest.TestSuite()
    suite.addTest(WidgetTestCase('test_default_size'))
    suite.addTest(WidgetTestCase('test_resize'))
    return suite
class NumbersTest(unittest.TestCase):

    def test_even(self):
        """
        Test that numbers between 0 and 5 are all even.
        """
        for i in range(0, 6):
            with self.subTest(i=i):
                self.assertEqual(i % 2, 0)

if __name__ == '__main__':
    unittest.main()

    """
Python unit testing framework, based on Erich Gamma's JUnit and Kent Beck's
Smalltalk testing framework (used with permission).

This module contains the core framework classes that form the basis of
specific test cases and suites (TestCase, TestSuite etc.), and also a
text-based utility class for running the tests and reporting the results
 (TextTestRunner).

Simple usage:

    import unittest

    class IntegerArithmeticTestCase(unittest.TestCase):
        def testAdd(self):  # test method names begin with 'test'
            self.assertEqual((1 + 2), 3)
            self.assertEqual(0 + 1, 1)
        def testMultiply(self):
            self.assertEqual((0 * 10), 0)
            self.assertEqual((5 * 8), 40)

    if __name__ == '__main__':
        unittest.main()

Further information is available in the bundled documentation, and from

  http://docs.python.org/library/unittest.html

Copyright (c) 1999-2003 Steve Purcell
Copyright (c) 2003-2010 Python Software Foundation
This module is free software, and you may redistribute it and/or modify
it under the same terms as Python itself, so long as this copyright message
and disclaimer are retained in their original form.

IN NO EVENT SHALL THE AUTHOR BE LIABLE TO ANY PARTY FOR DIRECT, INDIRECT,
SPECIAL, INCIDENTAL, OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE USE OF
THIS CODE, EVEN IF THE AUTHOR HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH
DAMAGE.

THE AUTHOR SPECIFICALLY DISCLAIMS ANY WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
PARTICULAR PURPOSE.  THE CODE PROVIDED HEREUNDER IS ON AN "AS IS" BASIS,
AND THERE IS NO OBLIGATION WHATSOEVER TO PROVIDE MAINTENANCE,
SUPPORT, UPDATES, ENHANCEMENTS, OR MODIFICATIONS.
"""

__all__ = ['TestResult', 'TestCase', 'IsolatedAsyncioTestCase', 'TestSuite',
           'TextTestRunner', 'TestLoader', 'FunctionTestCase', 'main',
           'defaultTestLoader', 'SkipTest', 'skip', 'skipIf', 'skipUnless',
           'expectedFailure', 'TextTestResult', 'installHandler',
           'registerResult', 'removeResult', 'removeHandler',
           'addModuleCleanup', 'doModuleCleanups', 'enterModuleContext']

# Expose obsolete functions for backwards compatibility
# bpo-5846: Deprecated in Python 3.11, scheduled for removal in Python 3.13.
__all__.extend(['getTestCaseNames', 'makeSuite', 'findTestCases'])

__unittest = True

from .result import TestResult
from .case import (addModuleCleanup, TestCase, FunctionTestCase, SkipTest, skip,
                   skipIf, skipUnless, expectedFailure, doModuleCleanups,
                   enterModuleContext)
from .suite import BaseTestSuite, TestSuite
from .loader import TestLoader, defaultTestLoader
from .main import TestProgram, main
from .runner import TextTestRunner, TextTestResult
from .signals import installHandler, registerResult, removeResult, removeHandler
# IsolatedAsyncioTestCase will be imported lazily.
from .loader import makeSuite, getTestCaseNames, findTestCases


# Lazy import of IsolatedAsyncioTestCase from .async_case
# It imports asyncio, which is relatively heavy, but most tests
# do not need it.

def __dir__():
    return globals().keys() | {'IsolatedAsyncioTestCase'}

def __getattr__(name):
    if name == 'IsolatedAsyncioTestCase':
        global IsolatedAsyncioTestCase
        from .async_case import IsolatedAsyncioTestCase
        return IsolatedAsyncioTestCase
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

