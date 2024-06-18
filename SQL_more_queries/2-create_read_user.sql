-- Create the database of hbtn_0d_2 and user user_0d_2

-- Create the database if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create the user if it does not exist
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant SELECT privilege on the database to the user
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Flush privileges to ensure the changes take effect immediately
FLUSH PRIVILEGES;
