/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/

select id, name, cs from (select h.hacker_id id, h.name name, count(c.challenge_id) cs
    from hackers h, challenges c 
    where h.hacker_id = c.hacker_id
    group by h.hacker_id, h.name)
    where (select count(cs1) from (select h.hacker_id id, h.name name, count(c.challenge_id) cs1
        from hackers h, challenges c 
        where h.hacker_id = c.hacker_id
        group by h.hacker_id, h.name)
        where cs1 = cs
        group by cs1) = 1 or ((select max(cs1) from (select count(c.challenge_id) cs1
        from hackers h, challenges c 
        where h.hacker_id = c.hacker_id
        group by h.hacker_id, h.name)) = cs and (select count(cs1) from (select h.hacker_id id, h.name name, count(c.challenge_id) cs1
        from hackers h, challenges c 
        where h.hacker_id = c.hacker_id
        group by h.hacker_id, h.name)
        where cs1 = cs
        group by cs1) > 1)
        order by cs desc, id;
    
