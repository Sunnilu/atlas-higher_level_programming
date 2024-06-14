#!/bin/bash
#prompt for the MYSQL root password
read -s -p "Enter MySQL root password:" PASSWORD
#execute the SHOW DATABASES command and print the output
mysql -h localhost -u root -p"$password" --silent -e "SHOW DATABASES;"