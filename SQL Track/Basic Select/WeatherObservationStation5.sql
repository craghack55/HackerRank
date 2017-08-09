/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/

select * from 
    (select city, length(city) from station where length(city) = (select min(length(city)) from station) 
     order by city asc) where rownum = 1;

select * from 
    (select city, length(city) from station where length(city) = (select max(length(city)) from station) 
     order by city asc) where rownum = 1;