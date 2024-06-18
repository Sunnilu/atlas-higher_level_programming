-- Create the database of hbtn_0d_2 and user_0d_2

CREATE DATABASE IF NOT EXITS hbtn_0d_2;
CREATE USER IF NOT EXITS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON 'hbtn_0d_2'.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
