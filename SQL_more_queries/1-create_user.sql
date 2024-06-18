-- Grant basic privileges to user 'user_0d_1'
GRANT SELECT, INSERT, UPDATE, DELETE ON *.* TO 'user_0d_1'@'localhost';

-- Add more privileges, checking after each addition
GRANT CREATE, DROP ON *.* TO 'user_0d_1'@'localhost';
GRANT RELOAD, SHUTDOWN ON *.* TO 'user_0d_1'@'localhost'
