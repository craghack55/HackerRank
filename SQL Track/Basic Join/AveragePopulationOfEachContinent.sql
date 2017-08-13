select country.continent, floor(avg(city.population)) from country inner join city on city.countrycode = country.code 
    group by country.continent;