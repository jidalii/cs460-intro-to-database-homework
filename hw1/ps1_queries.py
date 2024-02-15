#
# CS 460: Problem Set 1, SQL Programming Problems
#

#
# For each problem, use a text editor to add the appropriate SQL
# command between the triple quotes provided for that problem's variable.
#
# For example, here is how you would include a query that finds the
# names and years of all movies in the database with an R rating:
#
sample = """
    SELECT name, year
    FROM Movie
    WHERE rating = 'R';
"""

#
# Problem 4. Put your SQL command between the triple quotes found below.
#
problem4 = """
    SELECT name, pob, dob
    FROM Person
    WHERE name = 'Michelle Yeoh' 
        OR name = 'Jamie Lee Curtis';
"""

#
# Problem 5. Put your SQL command between the triple quotes found below.
# 10
problem5 = """
    SELECT name, Oscar.year
    FROM Movie, Oscar
    WHERE id = movie_id 
        AND type = 'BEST-PICTURE' 
        AND Oscar.year BETWEEN 2010 AND 2019
    ORDER BY Oscar.year DESC;
"""

#
# Problem 6. Put your SQL command between the triple quotes found below.
# 2
problem6 = """
    SELECT O.year, M.name
    FROM Oscar O, Movie M
    WHERE O.movie_id = M.id
        AND O.type = 'BEST-DIRECTOR' 
        AND O.person_id = (
            SELECT id
            FROM Person
            WHERE name = 'Steven Spielberg'
        );
"""
        
#
# Problem 7. Put your SQL command between the triple quotes found below. 541
#
problem7 = """
    SELECT COUNT(DISTINCT movie_id)
    FROM Person P, Actor A
    WHERE P.id = A.actor_id
        AND P.pob NOT LIKE '%USA';
"""

#
# Problem 8. Put your SQL command between the triple quotes found below.
#
problem8 = """
    SELECT name, runtime
    FROM Movie
    WHERE genre LIKE '%N%' 
        AND runtime = (
            SELECT MAX(runtime)
            FROM Movie
            WHERE genre LIKE '%N%'
        );       
"""

#
# Problem 9. Put your SQL command between the triple quotes found below.
#
problem9 = """
    SELECT M.name, COUNT(O.type)
    FROM Movie M, Oscar O
    WHERE M.id = O.movie_id 
    GROUP BY M.name, M.year
    HAVING COUNT(O.type) >=5;
"""

#
# Problem 10. Put your SQL command between the triple quotes found below.
# 8
problem10 = """
    SELECT DISTINCT name, pob
    FROM Person, Director
    WHERE id = director_id AND pob LIKE '%France' ;
"""

#
# Problem 11. Put your SQL command between the triple quotes found below.
#
problem11 = """
    SELECT M.earnings_rank, M.name, O.type
    FROM Movie M LEFT OUTER JOIN Oscar O ON M.id = O.movie_id
    WHERE M.earnings_rank <=25;
"""

#
# Problem 12. Put your SQL command between the triple quotes found below.
# 56
problem12 = """
    SELECT COUNT(*)
    FROM Oscar O, Movie M
    WHERE M.id = O.movie_id
        AND O.type = 'BEST-PICTURE'  
        AND M.runtime > (
                    SELECT AVG(runtime)
                    FROM Movie
        );          
"""

#
# Problem 13. Put your SQL command between the triple quotes found below.
# 188
problem13 = """
    SELECT O.type, P.name, M.name
    FROM Oscar O LEFT OUTER JOIN Person P ON O.person_id = P.id 
        LEFT OUTER JOIN Movie M ON O.movie_id = M.id
    WHERE O.year = 1993;
"""

#
# Problem 14. Put your SQL command between the triple quotes found below.
# 
problem14 = """
    SELECT COUNT(DISTINCT person_id)
    FROM Oscar
    WHERE type LIKE 'BEST-SUPPORTING%'
        AND person_id NOT IN (
            SELECT person_id
            FROM Oscar
            WHERE type = 'BEST-ACTOR' OR type = 'BEST-ACTRESS'
    );          
"""

#
# Problem 15. Put your SQL command between the triple quotes found below.
#
problem15 = """
    INSERT INTO Actor VALUES ('0614165', '0468569')
"""
