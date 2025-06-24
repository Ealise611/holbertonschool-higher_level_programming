-- This script lists all genres of the show Dexter using the database hbtn_0d_tvshows.
-- Result should  display tv_genres.name.
-- The tv_shows table contains only one record where title = 'Dexter'.
-- Result must be sorted in ascending order by the genre name.
-- Can only use one SELECT statement.
SELECT tv_genres.name
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name ASC;
