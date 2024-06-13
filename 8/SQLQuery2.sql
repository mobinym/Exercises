CREATE DATABASE dbMovie
GO
use dbMovie
GO
----------------------CREATE GENRE MOVIE--------------------------------------------------------------------------
----------------------جدول ژانر فیلم ها ------------------------------------------------------------------------
CREATE Table GenreMovie(
		GenreCode Tinyint PRIMARY KEY IDENTITY(1,1) NOT NULL,
		GenreName Nvarchar(30) NOT NULL 
		)
INSERT INTO GenreMovie([GenreName]) 
			VALUES (N'ترسناک'),
			       (N'درام'),
				   (N'جنگی'),
				   (N'علمی تخیلی'),
				   (N'کمدی'),
				   (N'ماجراجویی'),
				   (N'تریلر')

SELECT * FROM GenreMovie

------------------------CREATE MOVIE-------------------------------------------
-----------------------جدول فیلم ها ------------------------------------------
CREATE TABLE Movie(
	MovieCode TINYINT PRIMARY KEY NOT NULL,
	MovieName Nvarchar(30) NOT NULL,
	ProductionYear int NOT NULL,
	UNIQUE(MovieName),
	[DESCRIPTION] Nvarchar(max) NULL,
	IMDB DECIMAL(2,1) NOT NULL,
	GenreCode Tinyint NOT NULL, 
	FOREIGN KEY (GenreCode) REFERENCES GenreMovie(GenreCode)
)

INSERT INTO MOVIE(MovieCode,[MovieName], ProductionYear, [DESCRIPTION], [IMDB], [GenreCode])
values(1,'ALIEN', 1979, NULL, 8.2, 1),
	  (2,'Halloween', 1978,'Halloween is a 1978 American independent slasher film directed, co-written, and scored by John Carpenter.', 7.7, 1),
	  (3,'Totally Killer',2023,'hirty-five years after the shocking murders of three teens, an infamous killer returns on Halloween night to claim a fourth victim', 6.6, 5),
	  (4,'Against the Ice',2022,'Exploring Greenlands vast landscape for a lost map, two men must fight to survive. Based on the true story of Denmarks 1909 polar expedition.', 6.5, 6),
	  (5,'The Matrix',1999,'Neo, a computer programmer and hacker, has always questioned the reality of the world around him. His suspicions are confirmed when Morpheus, a rebel leader, contacts him and reveals the truth to him.',8.7,4),
	  (6, 'The Wolf of Wall Street' , 2013 , NULL , 8.2 , 2),
	  (7,'Jaws', 1975, 'A giant great white shark arrives on the shores of a New England beach resort and wreaks havoc with bloody attacks on swimmers.', 8.0, 1),
      (8,'Psycho', 1960, 'A Phoenix secretary embezzles $40,000 from her employers client, goes on the run, and checks into a remote motel run by a young man under the domination of his mother.', 8.5, 1),
      (9,'The Godfather', 1972, 'The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.', 9.2, 2),
      (10,'The Dark Knight', 2008, 'When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice.', 9.0, 4),
	  (11,'Inception', 2010, 'A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O.', 8.8, 4),
      (12,'Fight Club', 1999, 'An insomniac office worker and a devil-may-care soap maker form an underground fight club that evolves into much more.', 8.8, 2),
      (13,'Pulp Fiction', 1994, 'The lives of two mob hitmen, a boxer, a gangster and his wife, and a pair of diner bandits intertwine in four tales of violence and redemption.', 8.9, 2),
      (14,'Forrest Gump', 1994, 'The presidencies of Kennedy and Johnson, the Vietnam War, the Watergate scandal and other historical events unfold from the perspective of an Alabama man with an IQ of 75, whose only desire is to be reunited with his childhood sweetheart.', 8.8, 2)

SELECT * FROM MOVIE
-----------------------CREATE USERS---------------------------------------------------------------
-----------------------جدول کاربران-------------------------------------------------------------
CREATE TABLE USERS(
			UserID TINYINT PRIMARY KEY IDENTITY(1,1) NOT NULL,
			UserName Nvarchar(30) NOT NULL ,
			[Password] int NOT NULL ,
			[Age] int NOT NULL,
			MobileNumber VARCHAR(14) NULL,
			ISactive CHAR(3) NOT NULL ,
			MovieCode TINYINT NOT NULL ,
			FOREIGN KEY (MovieCode) REFERENCES Movie(MovieCode),
			CHECK([MobileNumber] like '0[0-9][0-9]-[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]')
			)
INSERT INTO USERS([UserName],[Age],[Password],[MobileNumber], [ISactive], [MovieCode])
VALUES (N'علی رضایی',18,596455,'098-9120125694','YES',1),
	   (N'محمد حسینی',20,45862,'098-9120125694','NO',2),
	   (N'سارا عظیمی',48,66910,'098-9120125694','YES',2),
	   (N'احمد محسنی',45,18822,'098-9120125694','YES',11),
	   (N'میلاد فراهانی',65,92956,'098-9120125694','NO',2),
	   (N'اکبر طالبزاده',45,9865,'098-9120125694','YES',4),
	   (N'زهرا عزتی',83,21562,'098-9120125694','YES',4),
	   (N'مبین یعقوبی مقدم',98,23265,'098-9120125694','YES',2),
	   (N'رضا تقی زاده',45,12666,'098-9120125694','YES',12),
	   (N'میلاد عبادی پور',56,52646,'098-9120125694','YES',2),
	   (N'اکرم فراهانی',65,62125,'098-9120125694','NO',2),
	   (N'کوروش زینلی',98,56421,'098-9120125694','NO',10),
	   (N'محمد یعقوبی',12,4548,'098-9120125694','YES',6),
	   (N'مهسا فدایی',12,54998,'098-9120125694','YES',14),
	   (N'ساناز اکرمی',46,54454,'098-9120125694','NO',4),
	   (N'بهار کرامتی',15,4787,'098-9120125694','YES',1)

SELECT * FROM USERS
------------------------------------------------------------------------------------------

---------INNER JOIN-----------------------------------------------------------------------
SELECT * 
FROM USERS U INNER JOIN Movie M
ON U.MovieCode = M.MovieCode




---------------------------------------------------------------------------------------------
--فیلم هایی که توسط هیچ شخصی دیده نشده است----------------------------------------------

SELECT M.MovieCode,M.MovieName
FROM USERS U FULL JOIN Movie M
ON U.MovieCode = M.MovieCode
WHERE U.UserID IS NULL




------------------------------------------------------------------------------------------
--فیلم هایی که بیش از دو بازدید داشتند -----------------------------------------------

SELECT M.MovieCode,M.MovieName,COUNT(U.USERID) AS UserCount
FROM USERS U INNER JOIN Movie M
ON U.MovieCode = M.MovieCode
GROUP BY M.MovieCode,M.MovieName
HAVING COUNT(U.UserID) > 2





---------------------------------------------------------------------------------------------
--نام سه فیلم برتر از نظر تعداد مشاهده کاربر  ------------------------------------------

SELECT TOP 3 M.MovieCode, M.MovieName, COUNT(U.UserID) as UserCount
FROM Movie M JOIN Users U
ON M.MovieCode = U.MovieCode
GROUP BY M.MovieCode, M.MovieName
ORDER BY COUNT(U.UserID) DESC


---------------------------------------------------------------------------------------------
--پر بازدید ترین ژانر فیلم ها ------------------------------------------------------------

SELECT G.GenreCode,G.GenreName , COUNT(U.UserID) as UserCount
FROM USERS U INNER JOIN Movie M
ON U.MovieCode = M.MovieCode INNER JOIN GenreMovie G
ON M.GenreCode = G.GenreCode
GROUP BY G.GenreCode,G.GenreName
ORDER BY COUNT(U.UserID) DESC




---------------------------------------------------------------------------------------------
--حذف فیلم های با ژانر کمدی---------------------------------------------------------------

DELETE
FROM Movie 
WHERE GenreCode IN (
						SELECT GenreCode FROM GenreMovie 
						WHERE GenreName = N'کمدی'
					)


---------------------------------------------------------------------------------------------
--فعال کردن همه کاربران -------------------------------------------------------------------
	
SELECT * 
FROM USERS

UPDATE USERS
SET ISactive = 'YES'
WHERE ISactive = 'NO'

--------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------
DROP TABLE GenreMovie
DROP TABLE Movie
DROP TABLE USERS