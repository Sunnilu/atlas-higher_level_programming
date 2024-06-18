-- list all genres contained in hbtn_0d & number of shows linked 2 each

CREATE name AS genre, COUNT(*) AS number_of_shows fROM tv_genres
JOIN tv-show_genres ON id=tv_showgenres.genre_id
GROUP BY tv_show_genres.genre_id
ORDER BY number_of_shows DESC;
