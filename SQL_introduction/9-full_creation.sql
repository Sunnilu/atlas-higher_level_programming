-- Create database if not exists
CREATE DATABASE IF NOT EXISTS hbtn_test_db_9;

-- Use the database
USE hbtn_test_db_9;

-- Drop table if exists (in case we want to reset it)
DROP TABLE IF EXISTS second_table;

-- Create table 'second_table' with id, name, and score columns
CREATE TABLE second_table (
    id INT,
    name VARCHAR(256),
    score INT
);

-- Insert records into 'second_table'
INSERT INTO second_table (id, name, score) VALUES
(1, 'John', 10),
(2, 'Alex', 3),
(3, 'Bob', 14),
(4, 'George', 8);
