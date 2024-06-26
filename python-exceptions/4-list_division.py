#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            division_result = 0
            if i < len(my_list_1) and i < len(my_list_2):
                try:
                    division_result = my_list_1[i] / my_list_2[i]
                except ZeroDivisionError:
                    print("division by 0")
                except TypeError:
                    print("wrong type")
            else:
                print("out of range")
        except IndexError:
            division_result = 0
        finally:
            result.append(division_result)
    return result

