/*
Write a solution to find the second highest distinct salary from the Employee
table. If there is no second highest salary, return null.

Input: Employee table = [[1, 100], [2, 200], [3, 300]]
Output: [[200]]
*/

select max(e.salary) as SecondHighestSalary
from Employee as e
where e.salary not in (
    select max(e2.salary)
    from Employee as e2
);
