-- 초급
update customers set address = '456 updated st' where customerID = 1;
update products set price = 29.99 where productID = 1;
update employees set jobTitle = 'Manager' where employeeID = 1;
update offices set phone = '123-456-7891' where officeID = 1;
update orders set status = 'shipped' where orderID = 1;
update orderdetails set quantityOrdered = 3 where orderID = 1 and productID = 1;
update payments set amount = 250.00 where customerID = 1 and paymentDate = '2023-01-01'
update productlines set textDescription = 'Updated description' where productLine = 'Classic Cars';
update customers set email = 'john_updated@email.com' where customerID = 1;
update products set price = price 1 * 1;


-- 중급
UPDATE employees SET officeCode = 2 WHERE department = 'Sales';
UPDATE offices SET city = 'Updated City' WHERE country = 'USA';
UPDATE orders SET status = 'Cancelled' WHERE orderDate BETWEEN '2022-12-01' AND '2022-12-31';
UPDATE orderdetails SET priceEach = priceEach * 0.9
                    WHERE orderID IN (SELECT orderID FROM orders WHERE orderDate BETWEEN '2023-01-01' AND '2023-01-31');
UPDATE payments SET amount = amount * 1.05 WHERE customerID = 2;
UPDATE productlines SET textDescription = 'New description' WHERE productLine IN ('Classic Cars', 'Trains');
UPDATE customers SET phone = '999-999-9999' WHERE city = 'San Francisco';
UPDATE products SET price = price * 0.95 WHERE productLine = 'Classic Cars';
UPDATE employees SET salary = salary + 5000 WHERE employeeID = 2;
UPDATE offices SET address = '1234 New Address St', phone = '987-654-3211' WHERE officeID = 2;


-- 고급
UPDATE orders SET status = 'On Hold' WHERE orderDate BETWEEN '2022-01-01' AND '2022-12-31';
UPDATE orderdetails SET priceEach = priceEach * 1.1 WHERE orderID = 3;
UPDATE payments SET paymentDate = '2023-02-01' WHERE paymentDate BETWEEN '2023-01-01' AND '2023-01-31';
UPDATE productlines SET textDescription = 'New updated description'
                    WHERE productLine IN (SELECT productLine FROM products WHERE quantityInStock < 10);
UPDATE customers SET address = 'New Address' WHERE customerNumber BETWEEN 1 AND 10;

