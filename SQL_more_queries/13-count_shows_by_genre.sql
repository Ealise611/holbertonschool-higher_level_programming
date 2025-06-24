-- This script lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
-- Results should display <TV show genre> - <number of shows linked to this genre>.
-- First column must be called genre.
-- Second column must be called number_of_shows.
-- Don't display a genre that doesn't have any shows linked.
-- Result must be sorted in descending order by number of shows linked.
-- Can only use one SELECT statement.
SELECT tv_genres.name AS genre,
       COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.id
HAVING COUNT(tv_show_genres.show_id) > 0
ORDER BY number_of_shows DESC;
