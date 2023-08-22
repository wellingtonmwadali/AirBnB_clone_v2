-- script prepares a MySQL server
-- create project testing database
-- dbname : hbnb_test_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- create new user named
-- username:hbnb_test with all privileges
-- password : hbnb_test_pwd if it dosen't exist
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- grant the SELECT privilege for user hbnb_test
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
-- grant all privileges to new user
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
