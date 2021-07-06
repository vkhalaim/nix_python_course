-- 1
SELECT product_title
FROM products
WHERE product_id NOT IN (
    SELECT products_product_id FROM cart_product
);
-- 2
SELECT product_title
FROM products
WHERE product_id NOT IN (
    SELECT products_product_id FROM cart_product
) OR
product_id IN (
    SELECT products_product_id FROM orders
    JOIN cart_product
    ON orders.carts_cart_id = cart_product.carts_cart_id
    WHERE order_status_order_status_id = 5
);
-- 3
SELECT product_title, COUNT(*) FROM products
JOIN cart_product
ON products.product_id = cart_product.products_product_id
GROUP BY product_title
ORDER BY 2 DESC LIMIT 10;
-- 4
SELECT product_title, COUNT(*) FROM products
JOIN cart_product
ON products.product_id = cart_product.products_product_id
JOIN orders
ON orders.carts_cart_id = cart_product.carts_cart_id
WHERE orders.order_status_order_status_id = 4
GROUP BY product_title
ORDER BY 2 DESC LIMIT 10;
-- 5
SELECT users.first_name, users.last_name, MAX(orders.total) from users
JOIN carts
ON users.user_id = carts.users_user_id
JOIN orders
ON carts.cart_id = orders.carts_cart_id
GROUP BY users.first_name, users.last_name
ORDER BY MAX(orders.total) DESC LIMIT 5;
-- 6
SELECT users.first_name, users.last_name, COUNT(orders.carts_cart_id) from users
JOIN carts
ON users.user_id = carts.users_user_id
JOIN orders
ON carts.cart_id = orders.carts_cart_id
GROUP BY users.first_name, users.last_name
ORDER BY COUNT(orders.carts_cart_id) DESC LIMIT 5;
-- 7
SELECT users.first_name, users.last_name, MAX(orders.total) from users
JOIN carts
ON users.user_id = carts.users_user_id
JOIN orders
ON carts.cart_id = orders.carts_cart_id
WHERE orders.order_status_order_status_id = 5
GROUP BY users.first_name, users.last_name
ORDER BY MAX(orders.total) DESC LIMIT 5;