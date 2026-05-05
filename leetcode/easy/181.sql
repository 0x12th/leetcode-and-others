/*
Write a solution to find the employees who earn more than their managers.

Input: Employee table = [[1, "Joe", 70000, 3], [2, "Henry", 80000, 4], [3, "Sam", 60000, null], [4, "Max", 90000, null]]
Output: [["Joe"]]
*/

select E.name as Employee
from Employee M
inner join Employee E on M.id = E.managerId
where E.salary > M.salary;
