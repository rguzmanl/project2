# Flask Application -- Movies Database

### Description.

This project uses the Flask module to run samples of items from a data base (csv file) in a web page. It contains one basic route that displays a message and the number of movies records in the database. The second route is a little bit more elaborate and it displays a sample of ten random movies pulled from the data base.

## What's in the project folder?

List of files:
* movies_clean.csv
* movies_tools.py
* README.md
* requirements.txt
* SI507_project2.py
* database_diagram.jpg

## How does the project work?

This application depends on the interaction between the two python files in the project folder.

### Class Movie.
* In **movies_tools.py** we open the movies data base in **movies_clean.csv**
* Then we create a class Movie with a few instance variables and a string method.
* In the bottom of this file there are a two chunks of code that can be used for testing the class Movie.
  * The first piece of code creates one random instance of the class Movie.
  * The second piece is a little more elaborate and it is used in the Flask route. It creates ten random instances of the class Movie.

### Flask application.
* In **SI507_project2.py** we import **movies_tools.py** so we can use any object and variables created there.
* The first route displays a simple line of text (*in h1 html format*) that tells us the number of movie records in the data base. For this we use the format method and invoke/use the variable *lines_count* created in **movies_tools.py**
* The second route invokes the class Movie from **movies_tools.py** and creates ten random instances of movies. It displays the ten instances as a string but with the use of **<br>** it is shown as a list in the web page.

## How to run the program?
* In order to run the tests in **movies_tools.py** you just need to uncomment the lines of code at the bottom.
* To run the Flask application go to the project folder using git bash or other terminal. Type the following command *python SI507_project2.py runserver*.
* Copy the line *http://127.0.0.1:5000/* and paste in your browser. This will open the firs basic route.
* Adding */movies/ratings* will run the second route which displays the ten random movies sample.
  * http://127.0.0.1:5000/movies/ratings
