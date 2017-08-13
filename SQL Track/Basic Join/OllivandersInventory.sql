/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/

/*select w.id, p.age, r.mc, w.power from wands w, wands_property p, 
    (select p.age age, min(w.coins_needed) mc, w.power pwr from wands w, wands_property p where
        w.code = p.code and
        p.is_evil = 0
        group by p.age, w.power) r
    where p.age = r.age
    and w.power = r.pwr
    and w.coins_needed = r.mc
    order by w.power desc, p.age desc;*/
    
select id, age, coins_needed, power from wands w1, wands_property wp1 
    where w1.code = wp1.code and coins_needed =( 
        select min(coins_needed) from wands w 
        where w.code = wp1.code and w.power = w1.power and wp1.is_evil = 0 group by power,age) 
        order by power desc, age desc;