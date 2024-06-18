-- list all shows contained in database hbtn_0d_tvshows

SELECT tv_shows.title, genres.genre_name 
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN genres ON tv_show_genres.genre_id = genres.id
ORDER BY tv_shows.title, genres.genre_name;
