# 코멘토 SQL 과제

## 1주차

### 1번

**Country 별로 ContactName이 ‘A’로 시작하는 Customer의 숫자를 세는 쿼리를 작성하세요.**

```sql
SELECT count(*) FROM Customers
where ContactName like 'A%';
```

### 2번

**Customer 별로 Order한 Product의 총 Quantity를 세는 쿼리를 작성하세요.**

```sql
select CustomerID, sum(Quantity)
from Orders
join OrderDetails
on Orders.OrderID = OrderDetails.OrderID
group by CustomerID
```

### 3번

**년월별, Employee별로 Product를 몇 개씩 판매했는지와 그 Employee의 FirstName을 표시하는 쿼리를 작성하세요.**

```sql
SELECT strftime('%Y-%m', OrderDate) as month, Orders.EmployeeID, OrderDetails.Quantity, Employees.FirstName
from Orders
join OrderDetails
on Orders.OrderID = OrderDetails.OrderID
join Employees
on Orders.EmployeeID = Employees.EmployeeID
group by month, Orders.EmployeeID
```

## 2주차

### 1번

**상품(product)의 카테고리(category)별로, 상품 수와 평균 가격대(list_price)를 찾는 쿼리를 작성하세요.**

```sql
SELECT category AS '카테고리', 
COUNT(1) AS '상품 수', 
AVG(list_price) AS '평균 가격'
FROM products
GROUP BY category
```

### 2번

**2006년 1분기에 고객(customer)별 주문(order) 횟수, 주문한 상품(product)의 카테고리(category) 수, 총 주문 금액(quantity * unit_price)과 고객의 이름(last_name, first_name)을 찾는 쿼리를 작성하세요. (힌트: join)**

```sql
SELECT customer_id, 
COUNT(orders.customer_id) AS '주문 횟수', 
COUNT(products.category) AS '카테고리 수',
SUM(order_details.quantity*order_details.unit_price) AS '총 주문 금액', 
last_name AS '성', 
first_name AS '이름'
FROM orders
JOIN customers ON orders.customer_id = customers.id
JOIN order_details ON orders.id = order_details.order_id
JOIN products ON order_details.product_id = products.id
WHERE date_format(orders.order_date, '%Y-%m') BETWEEN '2006-01' AND '2006-03'
group by customer_id
```

### 3번

 **2006년 3월에 주문(order)된 건의 주문 상태(status_name)를 찾는 쿼리를 작성하세요. (join을 사용하지 않고 쿼리를 작성하세요.) (힌트: sub-query)**

```sql
SELECT id AS '주문 번호',
(
  SELECT status_name
  FROM orders_status
  WHERE orders.status_id = orders_status.id 
) AS '주문 상태'
FROM orders
WHERE date_format(order_date, "%Y-%m") = '2006-03';
```

### 4번 

**2006년 1분기 동안 세 번 이상 주문(order) 된 상품(product)과 그 상품의 주문 수를 찾는 쿼리를 작성하세요. (order_status는 신경쓰지 않으셔도 됩니다.) (힌트: sub-query or having)**

```sql
SELECT product_id, COUNT(product_id) AS '주문 횟수'
FROM order_details
GROUP BY product_id
HAVING COUNT(product_id) > 3;
```

### 5-1번

**2006년 1분기, 2분기 연속으로 하나 이상의 주문(order)을 받은 직원(employee)을 찾는 쿼리를 작성하세요. (order_status는 신경쓰지 않으셔도 됩니다.) (힌트: sub-query, inner join)**

```sql
SELECT t1.employee_id,
(
    SELECT CONCAT(employees.last_name, ' ', employees.first_name) 
    FROM employees
    WHERE employees.id = t1.employee_id 
) AS '직원 이름'
FROM (
    SELECT DISTINCT employee_id
    FROM orders
    WHERE date_format(order_date, '%Y-%m') BETWEEN '2006-01' AND '2006-03'
) AS t1
JOIN(
    SELECT DISTINCT employee_id
    FROM orders
    WHERE date_format(order_date, '%Y-%m') BETWEEN '2006-04' AND '2006-06'
) AS t2
ON t1.employee_id = t2.employee_id
```



### 5-2번

**2006년 1분기, 2분기 연속으로 하나 이상의 주문을 받은 직원별로, 2006년 2분기 동안 받은 주문 수를 찾는 쿼리를 작성하세요. (order_status는 신경쓰지 않으셔도 됩니다.) (힌트: sub-query 중첩)**

### 5-3번

**2006년 1분기, 2분기 연속으로 하나 이상의 주문을 받은 직원별로, 월별 주문 수를 찾는 쿼리를 작성하세요. (order_status는 신경쓰지 않으셔도 됩니다.) (힌트: date_format() )**