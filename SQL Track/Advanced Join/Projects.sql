select root, end_date from
(select start_date, end_date, connect_by_root start_date as root, level as duration 
 from projects 
 where connect_by_isleaf = 1 connect by prior end_date = start_date) 
 where root not in (select end_date from projects) 
 order by duration, root;

/*CREATE TYPE pObject AS OBJECT (sd date, ed date, days number);

CREATE TYPE pt AS TABLE OF pObject;

set serveroutput on format wrapped;

declare 

idx NUMBER := 1;
prevStart date := NULL;
prevEnd date := NULL;

t pt;
t1 pt;

BEGIN

FOR rec IN (select a.start_date startDate, b.end_date endDate
from projects a, projects b
where a.end_date = b.start_date
order by startDate)

LOOP

if prevStart is null then
    prevStart := rec.startDate;
    prevEnd := rec.endDate;
elsif rec.endDate - prevEnd = 1 then
    prevEnd := rec.endDate;
else
    t.extend(1);
    t(idx) := pObject(prevStart, prevEnd, prevEnd - prevStart);
    idx := idx + 1;
    prevStart := rec.startDate;
    prevEnd := rec.endDate;
end if;

END LOOP;

SELECT CAST(MULTISET(SELECT * FROM TABLE(t)
 ORDER BY 3, 1) as pObject)
 INTO t1
 FROM dual;

for i in 1..t1.count
loop
dbms_output.put_line(t1(i).sd || ' ' || t1(i).ed);
end loop;

END;
/
*/