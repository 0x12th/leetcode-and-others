/*
Write a solution to find the rank of the scores. Scores should be ranked from
highest to lowest, and there should be no holes between ranks.

Input: Scores table = [[1, 3.50], [2, 3.65], [3, 4.00], [4, 3.85], [5, 4.00], [6, 3.65]]
Output: [[4.00, 1], [4.00, 1], [3.85, 2], [3.65, 3], [3.65, 3], [3.50, 4]]
*/

select s1.Score as score, count(distinct s2.Score) as rank
from Scores s1
left join Scores s2 on s1.Score <= s2.Score
group by s1.Id
order by s1.Score desc;
