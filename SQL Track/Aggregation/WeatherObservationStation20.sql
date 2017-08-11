/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/

select round(lat_n , 4) from (select lat_n, row_number() over (order by lat_n) rnk from station) 
    where rnk = ((select ceil(count(*) / 2) from station));