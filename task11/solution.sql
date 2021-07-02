CREATE DATABASE Shop;

CREATE TABLE Categories (
	category_id INT PRIMARY KEY,
	category_title VARCHAR(255),
	category_description TEXT
);

CREATE TABLE Users (
	user_id INT PRIMARY KEY,
	email VARCHAR(255),
	password_ VARCHAR(255),
	first_name VARCHAR(255),
	last_name VARCHAR(255),
	middle_name VARCHAR(255),
	is_staff SMALLINT,
	country VARCHAR(255),
	city VARCHAR(255),
	address TEXT
);

CREATE TABLE Products (
	product_id INT PRIMARY KEY,
	product_title VARCHAR(255),
	product_description TEXT,
	in_stock INT,
	price real,
	slug VARCHAR(45),
	category_id INT REFERENCES Categories(category_id)
);

CREATE TABLE Order_status (
	order_status_id INT PRIMARY KEY,
	status_name VARCHAR(255)
);

CREATE TABLE Carts (
	cart_id INT PRIMARY KEY,
	subtotal DECIMAL,
	total DECIMAL,
	timestamp_ TIMESTAMP(2),
	Users_user_id INT REFERENCES Users (user_id)
);

CREATE TABLE Orders (
	order_id INT PRIMARY KEY,
	shipping_total DECIMAL,
	total DECIMAL,
	created_at TIMESTAMP(2),
	updated_at TIMESTAMP(2),
	Carts_cart_id INT REFERENCES Carts(cart_id),
	Order_status_order_status_id INT REFERENCES Order_status (order_status_id)
);

CREATE TABLE Cart_product (
	carts_cart_id INT REFERENCES Carts (cart_id),
	products_product_id INT REFERENCES Products (product_id),
	PRIMARY KEY (carts_cart_id, products_product_id)
);

COPY Users(user_id, email, password_, first_name, last_name, middle_name, is_staff, country, city, address)
FROM 'D:\Projects\JetBrains\nix_python\task11\sql_input_files\users.csv'
DELIMITER ','
CSV;

COPY Categories(category_id, category_title, category_description)
FROM 'D:\Projects\JetBrains\nix_python\task11\sql_input_files\categories.csv'
DELIMITER ','
CSV;

COPY Products(product_id, product_title, product_description, in_stock, price, slug, category_id)
FROM 'D:\Projects\JetBrains\nix_python\task11\sql_input_files\products.csv'
DELIMITER ','
CSV;

COPY Order_status(order_status_id, status_name)
FROM 'D:\Projects\JetBrains\nix_python\task11\sql_input_files\order_statuses.csv'
DELIMITER ','
CSV;

COPY Carts(cart_id, Users_user_id, subtotal, total, timestamp_)
FROM 'D:\Projects\JetBrains\nix_python\task11\sql_input_files\carts.csv'
DELIMITER ','
CSV;

COPY Orders(order_id, Carts_cart_id, Order_status_order_status_id, shipping_total, total, created_at, updated_at)
FROM 'D:\Projects\JetBrains\nix_python\task11\sql_input_files\orders.csv'
DELIMITER ','
CSV;

/* Temporary table for removing duplicates */
CREATE TABLE tmp (
    id_1 INT,
    id_2 INT
);

COPY tmp(id_1, id_2)
FROM 'D:\Projects\JetBrains\nix_python\task11\sql_input_files\cart_products.csv'
DELIMITER ','
CSV;

INSERT INTO Cart_product(carts_cart_id, products_product_id)
SELECT DISTINCT id_1, id_2 FROM tmp;

DROP TABLE tmp;