SELECT category_title, COUNT(*) FROM categories
JOIN products
ON  categories.category_id = products.category_id
GROUP BY categories.category_title
ORDER BY 2 DESC;
