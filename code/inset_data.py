import psycopg2
from data.py import *

for i in range(len(articles)):
    atricles[3] = "DDDD"
print (articles)

connection = psycopg2.connect(database="", user ="", passwrod="", host ="", port="")

for i in range(len(articles)):
    connection.execute("INSERT INTO ARTICLE (Date_Published, Author, Title, Body), VALUES (articles[i][0], articles[i][1], articles[i][2], articles[i][3])")

for i in range(len(tag_categories)):
    connection.execute("INSERT INTO TAG_CATEGORY (Name) VALUES (tag_categories[i])")

for i in range(len(tags)):
    connection.execute("INSERT INTO TAG (Name, Category_name) VALUES (tags[i][0], tags[i][1])")

for i in range(len(classified_as)):
    connection.execute("INSERT INTO CLASSIFIED_AS (Article_ID, Tag_name) VALUES(classified_as[i][0], classified_as[i][1])")

'''
# Insert into ARTICLE
INSERT INTO ARTICLE (Date_Published, Author, Title, Body)
VALUES ('2017-03-19', 'Georgina Smith', 'Organization does Good Thing', 'Yesterday morning an organization...');

# Insert into TAG
INSERT INTO TAG (Name, Category_name)
	VALUES ("beach cleanup", "climate action");

# Insert into TAG_CATEGORY
INSERT INTO TAG_CATEGORY (Name)
	VALUES ("climate action");

# Insert into CLASSIFIED_AS
INSERT INTO CLASSIFIED_AS (Article_ID, Tag_name)
	VALUES(1, 'beach cleanup');
'''
