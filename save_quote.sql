CREATE DATABASE IF NOT EXISTS SavedQuotes;

CREATE TABLE myData ( 
    id INT(8) UNSIGNED NOT NULL auto_increment,
    Quote VARCHAR(255) default NULL,
    Author VARCHAR(255) default NULL.
    Catagory VARCHAR(255) default NULL,
    PRIMARY KEY (id)
) AUTO_INCREMENT=1;