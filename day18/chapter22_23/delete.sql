-- 초급
delete from customers where customerID = 1;
delete from products where productID = 1;
delete from employees where employeeID = 1;
delete from offices where officeID = 1;
delete from orders where orderdID = 1;
delete from orderdetails where orderID = 1;
delete from payments where customerID = 1;
delete from productlines where productLine = 'Classic Cars';
delete from customers where city = 'San Francisco';
delete from products where productLine = 'Classic Cars';


-- 중급
delete from employees where department = 'Sales';
delete from offices where country = 'USA';
delete from orders where orderDate between '2022-12-01' and '2022-12-31';
delete from orderdetails where orderID = 2;
delete from payments where customerID = 2;
delete from productlines where productLine IN ('motorcycles', 'planes');
delete from customers where customerNumber in (select customerNumber from customers order by customerNumber desc limit 5);
delete from products where quantityInStock = 0;
delete from employees where jobTitle = 'sales rep';
delete from offices where officeSize < 10;


-- 고급
DELETE FROM orders WHERE orderDate BETWEEN '2022-01-01' AND '2022-12-31';
DELETE FROM orderdetails WHERE productID IN (SELECT productID FROM products ORDER BY quantityInStock ASC LIMIT 5);
DELETE FROM payments WHERE amount < 50;
DELETE FROM productlines WHERE productLine NOT IN (SELECT DISTINCT productLine FROM products);
DELETE FROM customers WHERE lastOrderDate < '2022-01-01';