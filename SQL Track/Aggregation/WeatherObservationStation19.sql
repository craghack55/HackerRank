/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/

select round(sqrt(power((min(lat_n) - max(lat_n)), 2) + power((min(long_w) - max(long_w)), 2)),4) from station;