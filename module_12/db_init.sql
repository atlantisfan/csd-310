DROP USER IF EXISTS 'whatabook_user'@'localhost';

-- create whatabook_user and grant them all privileges to the whatabook database 
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

-- grant all privileges to the whatabook database to user whatabook_user on localhost 
GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';

-- drop contstraints if they exist
ALTER TABLE wishlist DROP FOREIGN KEY fk_book;
ALTER TABLE wishlist DROP FOREIGN KEY fk_user;

-- drop tables if they exist
DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS user;

CREATE DATABASE whatabook;
USE whatabook;

--Create Tables in whatabook database
	CREATE TABLE user (
		user_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
		first_name VARCHAR(75) NOT NULL,
		last_name VARCHAR(75) NOT NULL,
		email VARCHAR(200)
		);
	CREATE TABLE wishlist (
		wishlist_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
		user_id int REFERENCES user(user_id),
		book_id int REFERENCES book(book_id)
		);	
	CREATE TABLE book (
		book_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
		book_name VARCHAR (200) NOT NULL,
		details VARCHAR (500) NOT NULL,
		author VARCHAR (200) NOT NULL);
	CREATE TABLE store (
		store_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
		locale VARCHAR (500) NOT NULL,
		hours VARCHAR (500) NOT NULL
		);


--	Insert users
	INSERT into user (first_name,last_name,email)
	Values ('Daisy','Johnson','quake@shield.gov');
	INSERT into user (first_name,last_name,email)
	Values ('Bobbi','Morse','bobbi@hailhydra.cz');
	INSERT into user (first_name,last_name,email)
	Values ('Phil','Caulson','director@shield.gov');

--Insert book titles, details, and authors
	INSERT INTO book (book_name,details,author)
	VALUES ('Treasure Island','A boy must save his family from poverty by aligning with Pirates to find a hidden treasure','Robert Louis Stevenson');
	INSERT INTO book (book_name,details,author)
	VALUES ('Kidnapped','details','Robert Louis Stevenson');
	INSERT INTO book (book_name,details,author)
	VALUES ('Carrie','details','Stephen King');
	INSERT INTO book (book_id,book_name,details,author)
	VALUES ('A Wild Sheep Chase','details','Haruki Murakami');
	INSERT INTO book (book_name,details,author)
	VALUES ('Market Forces','details','Richard K Morgan');
	INSERT INTO book (book_name,details,author)
	VALUES ('The Villa','details','Nora Roberts');
	INSERT INTO book (book_name,details,author)
	VALUES ('Lives of the Stoics','details','Ryan Holiday');
	INSERT INTO book (book_name,details,author)
	VALUES ('The Hunt for Red October','A story of the cold war and Russian submarine designed to destroy the United States','Tom Clancy');
	INSERT INTO book (book_name,details,author)
	VALUES ('Shadowspell Academy','Harry Potter meets Hunger Games','Shannon Mayer');
	INSERT INTO book (book_name,details,author)
	VALUES ('The Shore Road Mystery','Hardy Boys Mystery.','Franklin W. Dixon');
	INSERT INTO book (book_name,details,author)
	VALUES ('Shakeup','details','Stuart Woods');
	INSERT INTO book (book_name,details,author)
	VALUES ('The Friend','details','Sigrid Nunez');
	INSERT INTO book (book_name,details,author)
	VALUES ('The Locker','details','Rankin Lothier');
	INSERT INTO book (book_name,details,author)
	VALUES ('The God Shaped Brain','How Your view of God shapes your reality.','Timothy Jennings, MD');
	INSERT INTO book (book_name,details,author)
	VALUES ('Introduction to JAVA','A comprehensive guide to JAVA.','Y. Daniel Liang');
	INSERT INTO book (book_name,details,author)
	VALUES ('I Am Spock','Star Trek, my life, and the way of the Vulcan.','Leonard Nimoy');
	INSERT INTO book (book_name,details,author)
	VALUES ('Leonard','Memoires of my friend.','William Shatner');

--insert store information
	INSERT INTO store (locale, hours)
	VALUES ('1721 Conway Drive, Suite 1A, Keene TX 76059','Sun-Fri 8:00AM -8:00PM, SAT: CLOSED');

--insert wishlists
	INSERT INTO wishlist (user_id, book_id)
	VALUES ('1','15');
	INSERT INTO wishlist (user_id, book_id)
	VALUES ('1','16');
	INSERT INTO wishlist (user_id, book_id)
	VALUES ('1','3');
	INSERT INTO wishlist (user_id, book_id)
	VALUES ('1','10');
	INSERT INTO wishlist (user_id, book_id)
	VALUES ('3','8');
	INSERT INTO wishlist (user_id, book_id)
	VALUES ('3','6');
