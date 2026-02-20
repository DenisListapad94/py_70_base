
# SELECT directors.name, directors.surname, count(movies.movie_id)
# FROM directors
# INNER JOIN movies ON directors.director_id = movies.director_id
# WHERE directors.age > 30
# GROUP BY directors.director_id
# HAVING count(movies.movie_id) > 1