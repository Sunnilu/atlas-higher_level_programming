-- create table 'second_table' in database 'hbtn_0c_0
-- Add props (id INT), (name VAR CHAR(256)), (score INT) 
CREATE TABLE IF NOT EXISTS second_table (id INT, name VARCHAR(256), score INT)

-- Script should create a maximum of 4 records
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (1, "John", 10);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (2, "Alex", 3);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (3, "Bob", 14);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (4, "George", 8);
