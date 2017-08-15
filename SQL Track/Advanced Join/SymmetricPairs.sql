/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/

select distinct f1.x, f1.y from functions f1, functions f2
    where (f1.x = f2.y and f1.y = f2.x) and (f1.x < f1.y or 
                                             (select count(*) from functions f where f.x = f1.x and f.y = f1.x) > 1)
    order by f1.x asc;