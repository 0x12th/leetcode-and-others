/*
Write a solution to find all customers who never order anything.

Input: Customers table = [[1, "Joe"], [2, "Henry"], [3, "Sam"], [4, "Max"]], Orders table = [[1, 3], [2, 1]]
Output: [["Henry"], ["Max"]]
*/

select c.name as Customers
from Customers c
left join Orders o on c.id = o.customerId
where o.customerId is null;
