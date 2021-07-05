/*1*/
SELECT AVG(total) FROM orders
WHERE order_status_order_status_id = 3;
/*2*/
SELECT MAX(total) FROM orders
WHERE order_status_order_status_id = 3 AND
created_at BETWEEN '07.31.2020' AND '09.30.2020';