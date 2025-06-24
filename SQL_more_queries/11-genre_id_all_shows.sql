-- This script lists all shows contained in the database hbtn_0d_tvshows.
-- Each record should display: tv_shows.title - tv_show_genres.genre_id.
-- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id.
-- If a show has no genre, display NULL.
-- Can only use one SELECT statement.
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres on tv_show.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
