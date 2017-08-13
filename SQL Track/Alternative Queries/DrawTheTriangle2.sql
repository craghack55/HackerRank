/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/

set serveroutput on format wrapped;
declare r number := 19;

begin
    FOR Lcntr IN 0..r
    LOOP
    DBMS_OUTPUT.put_line(rpad('*', 1 + Lcntr * 2, ' *'));
    END LOOP;
end;

/