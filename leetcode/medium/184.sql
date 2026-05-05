/*
Write a solution to find employees who have the highest salary in each
department.

Input: Employee table = [[1, "Joe", 70000, 1], [2, "Jim", 90000, 1], [3, "Henry", 80000, 2]], Department table = [[1, "IT"], [2, "Sales"]]
Output: [["IT", "Jim", 90000], ["Sales", "Henry", 80000]]
*/

select d.name as Department, e.name as Employee, e.salary as Salary
from Employee e
join Department d on e.departmentId = d.id
where (departmentId, salary) in (
    select departmentId, max(salary)
    from Employee
    group by departmentId
);
