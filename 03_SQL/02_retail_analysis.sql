-- 1. Overall KPIs
SELECT COUNT(*) AS orders,
       ROUND(SUM(sales),2) AS total_sales,
	   ROUND(SUM(PROFIT),2) AS total_profit,
	   ROUND(SUM(profit)/SUM(sales)*100,2) AS margin_pct 
FROM sales_data;

-- 2. Category-wise 
SELECT category,
       ROUND(SUM(sales),2) AS sales,
	   ROUND(SUM(profit),2) AS profit,
	   ROUND(SUM(profit)/SUM(sales)*100,2) AS margin_pct
FROM sales_data
GROUP BY category
ORDER BY profit DESC;

-- 3. Region-wise
SELECT region,
       ROUND(SUM(sales),2) AS sales,
	   ROUND(SUM(profit),2) AS profit,
	   ROUND(SUM(profit)/SUM(sales)*100,2) AS margin_pct
FROM sales_data
GROUP BY region
ORDER BY profit DESC;

-- 4. Discount vs Profit
SELECT discount,
       COUNT(*) AS orders,
	   ROUND(SUM(profit),2) AS profit,
	   ROUND(SUM(profit)/SUM(sales)*100,2) AS margin_pct
FROM sales_data
GROUP BY discount
ORDER BY discount;

-- 5. Loss-making orders
SELECT category,
       COUNT(*) AS loss_orders,
	   ROUND(SUM(profit),2) AS total_loss 
FROM sales_data
WHERE profit < 0
GROUP BY category
ORDER BY total_loss;

-- 6. Top 10 customers
select customer_id, 
       ROUND(SUM(sales),2) AS sales,
	   ROUND(SUM(profit),2) AS profit
FROM sales_data
GROUP BY customer_id
ORDER BY sales DESC
LIMIT 10;

-- 7. Monthly trend
SELECT order_year, month_no,
       ROUND(SUM(sales),2) AS sales,
	   ROUND(SUM(profit),2) AS profit
FROM sales_data
GROUP BY order_year, month_no
ORDER BY order_year, month_no;

-- 8. Top product per region (window function)
SELECT region,product,profit
FROM(
    SELECT region,product,
	ROUND(SUM(profit),2) AS profit,
	RANK() OVER (PARTITION BY region ORDER BY SUM(profit) DESC) AS rnk
    FROM sales_data
	GROUP BY region, product 
) t
WHERE rnk = 1;

-- 9. Loss orders by discount
SELECT discount,
       COUNT(*) AS loss_orders,
	   ROUND(SUM(profit),2) AS total_loss
FROM sales_data
WHERE profit < 0
GROUP BY discount
ORDER BY discount;

-- 10. Region vs average discount
SELECT region,
       ROUND(AVG(discount)*100,1) AS avg_discount_pct,
	   ROUND(SUM(profit)/SUM(sales)*100,2) AS margin_pct
FROM sales_data
GROUP BY region
ORDER BY margin_pct;