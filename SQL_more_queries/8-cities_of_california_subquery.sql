-- list al the cities of California in database hbtn_0d_usa.

SELECT id, name 
FROM cities
JOIN states ON cities.state_id = states.id
WHERE states.name = 'California'
ORDER BY cities.id;
