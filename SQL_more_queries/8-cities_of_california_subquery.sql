-- list al the cities of California in database hbtn_0d_usa.

CREATE id, name FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = California)
ORDER BY id;
