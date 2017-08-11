/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/

SELECT N, (CASE WHEN P IS NULL THEN 'Root' WHEN EXISTS (SELECT P FROM BST B WHERE A.N = B.P) THEN 'Inner' ELSE 'Leaf' END) FROM BST A ORDER BY N;
