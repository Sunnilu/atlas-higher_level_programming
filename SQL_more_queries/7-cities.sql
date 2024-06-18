-- Create the database hbtn_0d_usa if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Switch to the newly created database
USE hbtn_0d_usa;

-- Create the table cities within the hbtn_0d_usa database
CREATE TABLE IF NOT EXISTS cities (
  id INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,
  state_id INT NOT NULL,
  name VARCHAR(256) NOT NULL,
  FOREIGN KEY(state_id) REFERENCES states(id)
);
