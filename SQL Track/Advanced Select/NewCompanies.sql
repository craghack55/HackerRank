/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/

select company.company_code, company.founder, count(distinct lead_manager.lead_manager_code), 
                              count(distinct senior_manager.senior_manager_code), 
                              count(distinct manager.manager_code), count(distinct employee.employee_code)
                              from company, lead_manager, senior_manager, manager, employee 
                              where company.company_code = lead_manager.company_code and
                                    company.company_code = senior_manager.company_code and
                                    company.company_code = manager.company_code and
                                    company.company_code = employee.company_code 
                                    group by company.company_code, company.founder
                                    order by company.company_code asc;