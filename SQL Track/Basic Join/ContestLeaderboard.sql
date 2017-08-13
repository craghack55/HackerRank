/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/

select h.hacker_id, name, sum(sm) ss from hackers h,
    (select s.hacker_id, max(score) sm from submissions s 
    group by s.challenge_id, s.hacker_id) r
    where h.hacker_id = r.hacker_id group by h.hacker_id, name having sum(sm) > 0 order by ss desc, h.hacker_id asc;