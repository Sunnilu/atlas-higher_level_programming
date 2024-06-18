-- list all shows contained in hbtn_0d-tvshows without a genre_linked

SELECT title, tv_show_genres.genre_id FROM tv_shows
LEFT JOIN tv_show_genres ON id=tv_show_genres.show_id
WHERE tv_show_genre.show_id IS NULL
ORDER BY title, tv_show_genres.genre_id;
