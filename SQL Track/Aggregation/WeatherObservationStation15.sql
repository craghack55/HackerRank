/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/

select round(long_w, 4) from station where lat_n = (select max(lat_n) from station where lat_n < 137.2345);