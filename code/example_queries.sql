SELECT *
FROM ARTICLE_TAGS
WHERE Tag_name = 'recycle';

SELECT Category_name, COUNT(Tag_name)
FROM TAG_CATEGORY NATURAL JOIN TAG
GROUP BY Category_name;

SELECT *
FROM ARTICLE_TAGS
WHERE Tag_name = 'recycle' OR Tag_name = 'wind turbines' OR Tag_name ='organic';

SELECT *
FROM ARTICLE
WHERE Article_id=
(SELECT Article_id
FROM ARTICLE_TAGS
WHERE Tag_name = 'recycle'
INTERSECT
SELECT Article_id
FROM ARTICLE_TAGS
WHERE Tag_name = 'organic');

SELECT Tag_name
FROM CLASSIFIED_AS
WHERE Article_ID=5;

SELECT *
FROM ARTICLE
WHERE Article_ID=1;
