-- list all genres not linked to the show Dexter.
SELECT tv_genres.name FROM (
	(tv_genres JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id)
	JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
) WHERE tv_genres.name NOT IN (
	SELECT tv_genres.name FROM (
        	(tv_shows JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id)
        	JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
	) WHERE tv_shows.title = 'Dexter'
) GROUP BY tv_genres.name ORDER BY tv_genres.name;
