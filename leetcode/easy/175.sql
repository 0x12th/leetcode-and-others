/*
Write a solution to report the first name, last name, city, and state of each
person in the Person table. If the address of a personId is not present in the
Address table, report null instead.

Input: Person table = [[1, "Wang", "Allen"], [2, "Alice", "Bob"]], Address table = [[1, 2, "New York City", "New York"]]
Output: [["Allen", "Wang", null, null], ["Bob", "Alice", "New York City", "New York"]]
*/

select p.firstName, p.lastName, a.city, a.state
from Person p
left join Address a on p.personId = a.personId;
