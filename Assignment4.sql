CREATE DATABASE movie_db;
USE movie_db;

CREATE TABLE Movies (
    MovieID INT PRIMARY KEY,
    Title VARCHAR(100),
    Genre VARCHAR(50),
    ReleaseYear INT,
    Rating DECIMAL(3,1),
    BoxOfficeRevenue BIGINT,
    Director VARCHAR(100)
);

INSERT INTO Movies VALUES
(1,'Inception','Sci-Fi',2010,8.8,830000000,'Christopher Nolan'),
(2,'Titanic','Romance',1997,7.8,2200000000,'James Cameron'),
(3,'The Godfather','Crime',1972,9.2,134000000,'Francis Ford Coppola'),
(4,'Avatar','Sci-Fi',2009,7.9,2840000000,'James Cameron'),
(5,'Interstellar','Sci-Fi',2014,8.6,677000000,'Christopher Nolan'),
(6,'Parasite','Thriller',2019,8.6,264000000,'Bong Joon Ho'),
(7,'The Dark Knight','Action',2008,9.0,1000000000,'Christopher Nolan'),
(8,'Schindler''s List','Drama',1993,9.0,322000000,'Steven Spielberg'),
(9,'The Shawshank Redemption','Drama',1994,9.3,283000000,'Frank Darabont'),
(10,'Pulp Fiction','Crime',1994,8.9,213000000,'Quentin Tarantino');

-- 1
SELECT * FROM Movies
WHERE Director='Christopher Nolan';

-- 2
SELECT DISTINCT Genre FROM Movies;

-- 3
SELECT * FROM Movies
ORDER BY Rating DESC
LIMIT 5;

-- 4
SELECT * FROM Movies
WHERE ReleaseYear < 2000;

-- 5
SELECT Genre, COUNT(*) AS TotalMovies
FROM Movies
GROUP BY Genre;

-- 6
SELECT SUM(BoxOfficeRevenue) AS TotalRevenue
FROM Movies
WHERE Genre='Sci-Fi';

-- 7
SELECT Title
FROM Movies
WHERE Rating > 8.5 AND Rating < 9.0;

-- 8
SELECT Title
FROM Movies
WHERE Title LIKE '%The%';

-- 9
SELECT *
FROM Movies
ORDER BY BoxOfficeRevenue DESC
LIMIT 1;

-- 10
SELECT AVG(Rating) AS AverageRating
FROM Movies
WHERE ReleaseYear > 2000;
