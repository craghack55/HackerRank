/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/

select Doctor, Professor, Singer, Actor from (select * from 
    (select Name, occupation, (ROW_NUMBER() OVER (PARTITION BY occupation ORDER BY name)) 
     as row_num from occupations order by name asc) 
     pivot (min(name) for occupation in 
     ('Doctor' as Doctor,'Professor' as Professor,'Singer' as Singer,'Actor' as Actor)) order by row_num); 
                                            