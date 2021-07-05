/*1*/
SELECT * FROM products
WHERE price > 80.0 AND price <= 150.0;
/*2*/
SELECT * FROM orders
WHERE created_at > '01.10.2020';
/*3*/
SELECT * FROM orders
WHERE created_at >= '01.01.2020' AND created_at <= '06.30.2020';

SELECT * FROM orders
WHERE created_at BETWEEN '01.01.2020' AND '06.30.2020';
/*4*/
SELECT * FROM products
WHERE category_id = 7 OR category_id = 11 OR category_id = 18;

SELECT * FROM products
WHERE category_id IN (7, 11, 18);
/*5*/
SELECT * FROM orders
WHERE created_at <= '12.31.2020' AND order_status_order_status_id = 2;
/*6*/
SELECT * from carts
WHERE cart_id IN (SELECT carts_cart_id FROM orders WHERE order_status_order_status_id = 5);