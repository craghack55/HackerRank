/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/

SELECT (a.count-b.count)
 FROM
   (SELECT COUNT(city) count FROM station) a,
   (SELECT COUNT(distinct city) count FROM station) b;