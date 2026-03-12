CREATE TABLE actors (
    actors_id INT PRIMARY KEY,
    name VARCHAR(50),
    surname VARCHAR(50),
    age INT,
    sex CHAR(1)
);

CREATE TABLE directors (
    director_id INT PRIMARY KEY,
    name VARCHAR(50),
    surname VARCHAR(50),
    age INT,
    sex CHAR(1)
);

CREATE TABLE movies (
    movie_id INT PRIMARY KEY,
    name_movie VARCHAR(100),
    release INT,
    budjet BIGINT,
    director_id INT,
    FOREIGN KEY (director_id) REFERENCES directors(director_id)
);

CREATE TABLE actors_movies (
    actors_movies_id INT PRIMARY KEY,
    movies_id INT,
    actors_id INT,
    FOREIGN KEY (movies_id) REFERENCES movies(movie_id),
    FOREIGN KEY (actors_id) REFERENCES actors(actors_id)
);

CREATE TABLE bank_accounts (
    bank_account_id INT PRIMARY KEY,
    director_id INT NULL,
    actors_id INT NULL,
    account_number VARCHAR(20),
    FOREIGN KEY (director_id) REFERENCES directors(director_id),
    FOREIGN KEY (actors_id) REFERENCES actors(actors_id)
);

INSERT INTO actors VALUES
(1,'Arnold','Schwarzenegger',75,'m'),
(2,'Bruce','Willis',67,'m'),
(3,'Tom','Cruise',60,'m'),
(4,'Brad','Pitt',53,'m'),
(5,'Will','Smith',54,'m'),
(6,'Leonardo','DiCaprio',48,'m'),
(7,'Tom','Hanks',66,'m'),
(8,'Johnny','Depp',59,'m'),
(9,'Harrison','Ford',80,'m'),
(10,'Sandra','Bullock',58,'f'),
(11,'Halle','Berry',56,'f'),
(12,'Julia','Roberts',55,'f'),
(13,'Kate','Winslet',47,'f'),
(14,'Angelina','Jolie',47,'f');

INSERT INTO directors VALUES
(1,'James','Cameron',68,'m'),
(2,'Steven','Spilberg',75,'m'),
(3,'Robert','Zemeckis',70,'m'),
(4,'Doug','Liman',57,'m'),
(5,'Brian','De Palma',82,'m'),
(6,'John','Woo',76,'m'),
(7,'Tim','Berton',64,'m'),
(8,'Jan','De Bont',79,'m'),
(9,'Alejandro','Agresti',61,'m'),
(10,'Garry','Marshal',82,'m'),
(11,'Steven','Sodeberg',59,'m'),
(12,'Michael','Bay',57,'m'),
(13,'Barry','Sonnenfeld',69,'m'),
(14,'Simon','Kinberg',49,'m'),
(15,'Christopher','Nolan',52,'m'),
(16,'Martin','Scorsese',80,'m'),
(17,'Stanley','Kubrick',70,'m'),
(18,'Woody','Allen',87,'m');

INSERT INTO movies VALUES
(1,'Titanic',1997,200000000,1),
(2,'Catch me if you can',2002,52000000,2),
(3,'Forrest Gump',1994,55000000,3),
(4,'Terminator 2',1991,102000000,1),
(5,'Mr. & Mrs. Smith',2005,110000000,4),
(6,'Indiana Jones 3',1989,48000000,2),
(7,'Mission impossible 1',1996,80000000,5),
(8,'Mission impossible 2',2000,125000000,6),
(9,'Charlie and the Chocolate Factory',2005,150000000,7),
(10,'Speed',1994,25000000,8),
(11,'Lake House',2006,40000000,9),
(12,'Pretty women',1990,190000000,10),
(13,'Ocean’s eleven',2001,184000000,11),
(14,'Larry Crowne',2011,30000000,NULL),
(15,'Bad boys 1',1995,19000000,12),
(16,'Bad boys 2',2003,130000000,12),
(17,'Men in black',1997,90000000,13),
(18,'The Martian',2015,108000000,14),
(19,'Interstellar',2014,165000000,15);


INSERT INTO actors_movies VALUES
(1,1,6),
(2,1,13),
(3,2,6),
(4,2,7),
(5,3,7),
(6,4,1),
(7,5,4),
(8,5,14),
(9,6,9),
(10,7,3),
(11,8,3),
(12,9,8),
(13,10,10),
(14,11,10),
(15,12,12),
(16,13,4),
(17,13,12),
(18,14,7),
(19,14,12),
(20,15,5),
(21,16,5),
(22,17,5),
(23,18,NULL),
(24,19,NULL);

INSERT INTO bank_accounts VALUES
(1,NULL,1,'1264567'),
(2,NULL,2,'1296567'),
(3,NULL,3,'1234567'),
(4,NULL,4,'1294167'),
(5,NULL,5,'1594567'),
(6,NULL,6,'1794567'),
(7,NULL,7,'1994567'),
(8,NULL,8,'2294567'),
(9,NULL,9,'1294567'),
(10,NULL,10,'2297667'),
(11,NULL,11,'3994567'),
(12,NULL,12,'4294567'),
(13,NULL,13,'5294567'),
(14,NULL,14,'6294567'),
(15,1,NULL,'7294567'),
(16,2,NULL,'8294567'),
(17,3,NULL,'9294567'),
(18,4,NULL,'1294561'),
(19,5,NULL,'1294562'),
(20,6,NULL,'1294563'),
(21,7,NULL,'1294564'),
(22,8,NULL,'1294565'),
(23,9,NULL,'1294566'),
(24,10,NULL,'1294567'),
(25,11,NULL,'1294568'),
(26,12,NULL,'1294569'),
(27,13,NULL,'1294521'),
(28,14,NULL,'1294537'),
(29,15,NULL,'1294547'),
(30,16,NULL,'1294557'),
(31,17,NULL,'1294557'),
(32,18,NULL,'1294577');

ALTER TABLE bank_accounts
ADD COLUMN finance INTEGER

select name_movie , name || ' ' || surname as director_name
from directors as d
INNER JOIN movies as m
on d.director_id = m.director_id
order by budjet DESC
limit 10


select
	a.surname as actors_name,
	m.name_movie
from actors as a
left join actors_movies as am
on a.actors_id = am.actors_id
left join movies as m
on am.movies_id = m.movie_id
where m.movie_id is null
union
select
	d.surname as director_name,
	m.name_movie
from directors as d
left join movies as m
on d.director_id = m.director_id
where m.director_id is null


SELECT
	m.name_movie,
	a.name || ' ' || a.surname as full_name
from movies as m
join actors_movies as am
on m.movie_id = am.movies_id
join actors as a
on am.actors_id = a.actors_id
where budjet > 150000000


select
	distinct d.name || ' ' || d.surname as director_full_name
from directors as d
join movies as m
on d.director_id = m.director_id
where m.release < 2000


ALTER TABLE bank_accounts
ADD COLUMN finance INTEGER




-- At line 1:
INSERT INTO movies (movie_id, name_movie, release, budjet, director_id)
SELECT
    100 + d.director_id,
    'Film of ' || d.name,
    2025,
    50000000,
    d.director_id
FROM directors d
LEFT JOIN movies m
    ON d.director_id = m.director_id
WHERE m.movie_id IS NULL;
-- Result: запрос успешно выполнен. Заняло 1мс, 3 строк изменено
-- ВЫПОЛНЕНИЕ ВСЕ В 'SQL 1*'
--
-- At line 1:
INSERT INTO movies (movie_id, name_movie, release, budjet, director_id)
SELECT
    200 + a.actors_id,
    'Solo film of ' || a.name,
    2025,
    30000000,
    NULL
FROM actors a
LEFT JOIN actors_movies am
    ON a.actors_id = am.actors_id
WHERE am.movies_id IS NULL;
-- Result: запрос успешно выполнен. Заняло 0мс, 2 строк изменено
-- ВЫПОЛНЕНИЕ ВСЕ В 'SQL 1*'
--
-- At line 1:
INSERT INTO actors_movies (actors_movies_id, movies_id, actors_id)
SELECT
    300 + a.actors_id,
    200 + a.actors_id,
    a.actors_id
FROM actors a
LEFT JOIN actors_movies am
    ON a.actors_id = am.actors_id
WHERE am.movies_id IS NULL;




update movies
set rating = CASE
    when name_movie = 'Titanic' then 9.2
    when name_movie = 'Forrest Gump' then 8.7
    when name_movie = 'Interstellar' then 8.6
    when name_movie = 'The Martian' then 8.0
    else 7.0
end;


select
    d.name || ' ' || d.surname as director_full_name,
    m.name_movie,
    m.release,
    m.rating
from movies m
join directors d
    on m.director_id = d.director_id
where m.release < 2000
  and m.rating < (
        select avg(rating)
        from movies
        where release < 2000
  );



select
    a.actors_id,
    a.name,
    a.surname,
    count(distinct a2.actors_id) as known_actors_count
from actors a
join actors_movies am1
    on a.actors_id = am1.actors_id
join actors_movies am2
    on am1.movies_id = am2.movies_id
join actors a2
    on am2.actors_id = a2.actors_id
where a.actors_id <> a2.actors_id
group by a.actors_id, a.name, a.surname
having count(distinct a2.actors_id) >= 2;