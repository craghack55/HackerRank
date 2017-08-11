set serveroutput on format wrapped;

declare

triangleType varchar(20);

cursor triangle is 
    select A, B, C from triangles;
    
tri triangles%rowtype;

begin

for tri in triangle loop
    case
        when (greatest(tri.A, tri.B, tri.C) = tri.A and tri.A >= tri.B + tri.C) or 
        (greatest(tri.A, tri.B, tri.C) = tri.B and tri.B >= tri.A + tri.C) or 
        (greatest(tri.A, tri.B, tri.C) = tri.C and tri.C >= tri.B + tri.A) then
            DBMS_OUTPUT.put_line('Not A Triangle');

        when tri.A = tri.B and tri.B = tri.C then
            DBMS_OUTPUT.put_line('Equilateral');

        when (tri.A = tri.B and tri.B != tri.C) or 
            (tri.A = tri.C and tri.B != tri.C) or 
            (tri.B = tri.C and tri.B != tri.A) then
                DBMS_OUTPUT.put_line('Isosceles');

        when tri.A != tri.B and tri.B != tri.C and tri.A != tri.C then
            DBMS_OUTPUT.put_line('Scalene');
            
    end case;
end loop;
end;
/
