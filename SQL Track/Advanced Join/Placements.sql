/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/

select name from 
    (select s.id id, p.salary po from students s, packages p 
        where p.id = s.id) a, 
    (select s.id id, p.salary pf from students s, friends f, packages p 
        where f.id = s.id and p.id = f.friend_id) b, students s
    where s.id = a.id and s.id = b.id and a.po - b.pf < 0
    order by b.pf;