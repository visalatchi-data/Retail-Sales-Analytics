SELECT COUNT(*) AS total_orders,
       SUM(sales) AS total_sales,
	   SUM(profit) AS total_profit
FROM sales_data;