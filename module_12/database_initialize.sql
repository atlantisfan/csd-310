CREATE TABLE user (
    user_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(75) NOT NULL,
    last_name VARCHAR(75) NOT NULL
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
    locale VARCHAR (500) NOT NULL
	);
Insert new records to fill each table

INSERT into user (first_name,last_name)
Values ('Daisy','Johnson');
INSERT into user (first_name,last_name)
Values ('Bobbi','Morse');
INSERT into user (first_name,last_name)
Values ('Phil','Caulson');
INSERT INTO book (book_name,details,author)
VALUES ('Treasure Island','details','Robert Louis Stevenson');
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
VALUES ('Shakeup','details','Stuart Woods');
INSERT INTO book (book_name,details,author)
VALUES ('The Friend','details','Sigrid Nunez');
INSERT INTO book (book_name,details,author)
VALUES ('The Locker','details','Rankin Lothier');

INSERT INTO store (locale)
VALUES ('1721 Conway Drive, Suite 1A, Keene TX 76059');

INSERT INTO wishlist (user_id, book_id)
VALUES ('1','2');
INSERT INTO wishlist (user_id, book_id)
VALUES ('3','8');
INSERT INTO wishlist (user_id, book_id)
VALUES ('6','6');
	