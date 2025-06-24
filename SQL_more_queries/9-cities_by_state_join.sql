-- This script lists all cities contained in the database hbtn_0d_usa.
-- Result must be sorted in ascending order by cities.id.
-- Each record should display cities.id, cities.name and states.name.
-- Only use one SELECT statement.
SELECT cities.id, cities.name, states.name FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
