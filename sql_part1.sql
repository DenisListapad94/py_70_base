CREATE TABLE actors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    age INTEGER,
    sex TEXT CHECK(sex IN ('male', 'female')),
    country TEXT,
    name TEXT NOT NULL,
    last_name TEXT NOT NULL
);

alter table actors
add column salary integer

CREATE TABLE actors_new (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    age INTEGER CHECK(age >= 0),
    sex TEXT CHECK(sex IN ('male','female')),
    country TEXT,
    name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    salary INTEGER
);
INSERT INTO actors_new (id, age, sex, country, name, last_name, salary)
SELECT id, age, sex, country, name, last_name, salary FROM actors;
DROP TABLE actors;
ALTER TABLE actors_new RENAME TO actors;

alter table actors
drop salary

insert into actors (age, sex, country, name, last_name) values
(35, 'male', 'USA', 'John', 'Smith'),
(28, 'female', 'Canada', 'Emily', 'Johnson'),
(42, 'male', 'UK', 'Michael', 'Brown'),
(30, 'female', 'Australia', 'Olivia', 'Davis'),
(50, 'male', 'Germany', 'Thomas', 'Müller'),
(25, 'female', 'France', 'Chloe', 'Lefevre'),
(37, 'male', 'Italy', 'Luca', 'Rossi'),
(29, 'female', 'Spain', 'Sofia', 'García'),
(45, 'male', 'Japan', 'Hiroshi', 'Tanaka'),
(33, 'female', 'South Korea', 'Ji-eun', 'Kim'),
(40, 'male', 'Russia', 'Alexey', 'Ivanov'),
(26, 'female', 'Brazil', 'Isabela', 'Silva'),
(38, 'male', 'Mexico', 'Carlos', 'Hernandez'),
(31, 'female', 'India', 'Ananya', 'Patel'),
(48, 'male', 'China', 'Li', 'Wei'),
(27, 'female', 'Netherlands', 'Emma', 'de Vries'),
(36, 'male', 'Sweden', 'Erik', 'Lindberg'),
(32, 'female', 'Norway', 'Ingrid', 'Hansen'),
(41, 'male', 'Argentina', 'Matias', 'Gomez'),
(29, 'female', 'South Africa', 'Thandi', 'Nkosi'),
(34, 'male', 'Turkey', 'Ahmet', 'Yilmaz'),
(30, 'female', 'Greece', 'Eleni', 'Papadopoulos'),
(39, 'male', 'Egypt', 'Omar', 'Hassan'),
(28, 'female', 'New Zealand', 'Charlotte', 'Wilson'),
(44, 'male', 'Poland', 'Piotr', 'Kowalski');

INSERT INTO actors (name, last_name) VALUES
('Liam', 'Turner'),
('Sophia', 'Morris'),
('Ethan', 'Reed'),
('Mia', 'Foster'),
('Noah', 'Cole');

update actors
set country = 'Unknown'
where country is null

update actors
set age = age + 2
where sex = 'female' and age > 40

select name, last_name
from actors
where sex = 'female' and age < 35 and country = 'France'
order by name

select name, last_name, age
from actors
where sex = 'male'
order by age
limit 5

select count(name), min(age) as min_age, max(age) as max_age, avg(age) as avg_age
from actors

select country
from actors
where sex ='male'
group by country
having count(country) between 5 and 10

select sex, floor(avg(age))
from actors
group by sex