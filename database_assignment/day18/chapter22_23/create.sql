-- 초급
insert into customers (name, address) values ('김대정', '경기도 안양시');
insert into products (name, price) values ('iphone15', 1500000);
insert into employees (firstName, lastName) values ('Alice', 'Johnson');
insert into offices (city, phone) values ('san francisco', '123-456-7890');
insert into orders (orderDate, customerID) values ('2023-01-01', 1);
insert into orderdetails (orderID, productID, quantityOrdered, priceEach) values (1, 1, 2, 20.00);
insert into payments (customerID, amount, paymentDate) values (1, 200.00, '2023-01-01');
insert into productlines (productLine, textDescription) values ('classic cars', 'various classic cars models');
insert into customers (name, address, city) values ('Jane Smith', '456 Elm St', 'New York');
insert into products (name, price, productLine) values ('vintage train', 34.99, 'trains');

-- 중급
insert into customers (name, address) values ('김대정', '경기도 안양시'),
                                             ('김일일', '경기도 안산시');

insert into products (name, price) values ('iphone15', 1500000),
                                          ('iphone15 pro', 1800000);

insert into employees (firstName, lastName) values ('Alice', 'Johnson'),
                                                   ('Brown', 'Blazer');

insert into orders (orderDate, customerID) values ('2023-01-01', 1),
                                                  ('2023-01-02', 2);
insert into orderdetails (orderID, productID, quantityOrdered, priceEach) values (2, 3, 2, 15.00),
                                                                                 (2, 4, 2, 25.00);

insert into payments (customerID, amount, paymentDate) values (2, 100.00, '2023-01-02'),
                                                              (3, 200.00, '2023-01-03');

insert into customers (name, address, city) values ('Jane Smith', '456 Elm St', 'New York');
insert into orders (customerID, orderDate) values (LAST_INSERT_ID(), '2023-01-04');

insert into employees (firstName, lastName) values ('Nancy', 'Blue');
update employees set  jobTitle = 'Sales Rep' where employeeNumber = LAST_INSERT_ID();

insert into products (name, price, productLine) values ('rc helicopter', 29.99, 'helicopters');
update products set quantityInStock = 30 where productCode = LAST_INSERT_ID();

insert into offices (city, phone) values ('Los Angeles', '987-654-3210');
update employees set officeCode = LAST_INSERT_ID() where lastName = 'Blue';

insert into productlines (productLine, textDescription) values ('motorcycle', 'Various motorcycle models');
insert into products (name, price, productLine) values ('Harley Bike', 55.99, 'Motorcycles'),
                                                       ('Yamaha Bike', 45.99, 'Motorcycle');

-- 고급
insert into customers (name, address) values ('Linda Grey', '654 Maple St');
insert into orders (cutomerID, orderDate) values (LAST_INSERT_ID(), '2023-01-05');
insert into orderdetails (orderID, productID, quantityOrdered, priceEach) values (LAST_INSERT_ID(), 5, 2, 45.00);

insert into employees (firstName, lastName) values ('Rachel', 'Purple');
update employees set reportsTo =
    (select employeeNumber from employees where lastName = 'Johnson') where lastName = 'Purple';

insert into products (name, price, productLine) values ('Electric Train', 80.00, 'Trains');
insert into orders (orderDate, customerID) values ('2023-01-06', 2);
insert into orderdetails (orderID, productID, quantityOrdered, priceEach)
values (LAST_INSERT_ID(), LAST_INSERT_ID(), 1, 80.00);

insert into orders (orderDate, customerID) values ('2023-01-07', 3);
insert into payments (customerID, amount, paymentDate) values (3, 200.00, '2023-01-07');

insert into orderdetails (orderID, productID, quantityOrdered, priceEach) values (3, 6, 3, 25.00);
update products set quantityInStock = quantityInStock - 3 where productCode = 6;