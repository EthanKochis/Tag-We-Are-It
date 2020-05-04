# Tag We Are It

This was a semester-long group project for my Database Systems course.

Collaborators with links to their GitHub accounts:
* [Derek Kneisel](https://github.com/Derek-Kneisel)
* [Ethan Kochis](https://github.com/EthanKochis)
* [Alec Lopez](https://github.com/lopeza19)
* [Tomer Singal](https://github.com/Singalt16)

Tag We Are It implements a tagging system for a set of articles, and tags are grouped into tag categories.

Specfically, this system aims to augment the website [SRHub.org](www.srhub.org) with this tagging system.  The articles that are shown in this project are from that website.

## How to Install

1. Install the following software on your system:

    * [PostgreSQL](https://www.postgresql.org/download/)
    * [Python 3](https://www.python.org/downloads/)
    * [Python library psycopg2](https://www.psycopg.org/docs/install.html])
    * [Python library flask](https://flask.palletsprojects.com/en/1.1.x/installation/)
    * [Python library flask-cors](https://flask-cors.readthedocs.io/en/latest/)

1. Now, edit the *code/database.ini* file to include the infromation needed to access your PostgreSQL database.  This file includes the username and password you want this program to access your database with.
    * **NOTE: Do not push this file back to the repository, as it will contain sensitive information.**

1. After cloning the repository, navigate to the *code* folder in a terminal and run the *init_db.sh* script.

    * This script will create the project database with its tables and views, and initialize the database with 10 articles.
    
        * Note that if you change the name of the database in the *code/database.ini* file, you need to change it in this file too.
1. Run this command to launch the flask server: *FLASK_APP="backend.py" flask run*
1. In your GUI file explorer, navigate to the *code* folder and open the *index.html* file.  You should now see the home page: 

<p align="center">
  <img src="./img/Home Page.png" alt="Image of Home Page" width="80%">
</p>


## Usage

Click around!  The tags are clickable, as are the options in the top right of the page.
