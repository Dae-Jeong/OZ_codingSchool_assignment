-- 초급
select * from customers;
select * from products;
select firstName, lastName, jobTitle from employees;
select city, address, phone from offices;
select * from orders order by orderDate desc limit 10;
select * from orderdetails where orderID = 1;
select * from payments where customerID = 1;
select productLine, textDescription from productlines;
select * from customers where city = 'New York';
select * from products where price between 20 and 50;


-- 중급
select * from orders where customerID = 2;
select * from orderdetails where productID = 3;
select * from payments where paymentDate between '2023-01-01' and '2023-01-31';
select firstName, lastName from employees where jobTitle = 'sales rep';
select * from offices where country = 'USA';
select * from products where productLine = 'classic cars';
select * from customers order by customerNumber desc limit 5;
select * from products where quantityInStock < 10;
select * from orders where orderDate between '2022-12-01' and '2022-12-31';
select orderID, sum(quantityOrdered * priceEach) as totalAmount from orderdetails where orderID = 2 group by orderID;


-- 고급
select city, count(*) as customerCount from customers group by city;
select productLine, avg(price) as averagePrice from products group by productLine;
select officeCode, avg(salary) as averageSalary from employees group by officeCode;
select productID, sum(quantityOrdered) as totalOrdered
from orderDetails group by productID order by totalOrdered desc limit 5;

