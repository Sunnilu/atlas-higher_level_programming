#!/bin/bash

read -s -p "Enter MySQL root password:" PASSWORD
mysql -h localhost -u root -p"$password" --silent -e "SHOW DATABASES;"