set serveroutput on format wrapped;

DECLARE
    counter NUMBER;
    k NUMBER;
    result varchar2(1000);
BEGIN
  result := '';
  FOR n IN 2..1000 LOOP   
    counter := 0;
    k := floor(n/2);
    FOR i IN 2..k LOOP
        IF (mod(n, i) = 0 ) THEN
            counter := 1;
        END IF;
    END LOOP;
    IF (counter = 0) THEN
       result := result || n ||'&';
    END IF;
  END LOOP;
  DBMS_OUTPUT.put_line(substr(result, 1, length(result) - 1));
END;

/