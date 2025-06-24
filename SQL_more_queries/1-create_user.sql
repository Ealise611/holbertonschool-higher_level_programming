-- This script creates the MySQL user 'user_0d_1' with password 'user_0d_1_pwd' and grants all privileges on the database 'hbtn_0d_1' to this user.
CREATE USER 'user_0d_1'@'Localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'Localhost';
FLUSH PRIVILEGES;
