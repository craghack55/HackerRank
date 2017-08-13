/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/

select h.hacker_id, h.name from hackers h, (select h.hacker_id, count(h.hacker_id) cc
                                            from hackers h, submissions s, challenges c, difficulty d where
                                            h.hacker_id = s.hacker_id and 
                                            s.challenge_id = c.challenge_id and
                                            d.difficulty_level = c.difficulty_level and
                                            s.score = d.score
    group by h.hacker_id
    having count(h.hacker_id) > 1) r where h.hacker_id = r.hacker_id
    order by cc desc, h.hacker_id asc;