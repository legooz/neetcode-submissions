-- Select customers with positive revenue in 2020.


SELECT customer_id
FROM customers
WHERE revenue > 0 and year = 2020