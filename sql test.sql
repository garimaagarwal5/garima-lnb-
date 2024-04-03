create database test;
use test;
create table products(product_id int primary key,product_name varchar(255),category varchar(255));
insert into products values(1,'laptop','electronics'),
(2,'shirt','Clothing'),
(3,'Microwave','HomeAppliances');
create table sales(sale_id int primary key,
product_id int,
sale_date date,
quantity int,
price decimal(10,2)
);
insert into sales values (1,1,'2024-1-1',5,1000.00),
(2,2,'2024-1-2',10,20.00),
(3,3,'2024-1-3',3,150.00);

select sum(price) from sales join products where sales.product_id=products.product_id group by products.product_id;

create table employees(employeeid int primary key,employee_name varchar(255),manager_id int);
insert into employees values(1,'john doe',2),
(2,'jane smith',null),
(3,'bob johnson',2);
select e.employee_name as employee_name,e1.employee_name as manager_name from employees e join employees e1 on e.manager_id=e1.employeeid;