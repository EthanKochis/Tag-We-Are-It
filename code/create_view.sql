CREATE VIEW ARTICLE_TAGS AS
	SELECT * FROM ARTICLE
NATURAL JOIN CLASSIFIED_AS
NATURAL JOIN TAG
