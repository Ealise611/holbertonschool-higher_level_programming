-- This script lists all the cities of California that can be found in the database hbtn_0d_usa.
-- The script should use the database hbtn_0d_usa.
-- The script list cities.id in accending order, not using JOIN keyword.
SELECT id, name FROM cities 
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC;
