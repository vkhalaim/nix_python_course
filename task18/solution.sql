CREATE TABLE potential_customers(
    id serial not null primary key,
    email varchar(255) not null,
    name_ varchar(255) not null,
    surname varchar(255) not null,
    second_name varchar(255) not null,
    city varchar(255) not null
);

INSERT INTO potential_customers(email, name_, surname, second_name, city)
SELECT users.email, users.first_name, users.last_name, users.middle_name, users.city
FROM users
JOIN carts ON users.user_id = carts.users_user_id
WHERE carts.cart_id IN (
    SELECT carts_cart_id FROM orders
    WHERE order_status_order_status_id IN (1, 2, 5)
);

SELECT *
FROM (
    SELECT name_, surname, email FROM potential_customers
    WHERE city = 'city 17'
    UNION
    SELECT first_name, last_name, email FROM users
    WHERE city = 'city 17'
) AS united_tables;