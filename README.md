# Project #1: Movie Trailer Website
**by Christopher Betts**

For Udacity's [Full Stack Web Developer Nanodegree program](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004).

---

## Project Description
A Python program that generates a one-page website titled **Fresh Tomatoes** (*[get it?](https://www.rottentomatoes.com/)*) in the form of an HTML file which displays the cover art/poster of a number of movies. Clicking on a movie will play its theatrical trailer as well as show a short summary and the movie's MPAA rating.

## Requirements
[Python](https://www.python.org/) (version 2.6 or higher) is required to run this project.

## Project Contents
- **templates** -- directory containing partial HTML and JavaScript template files that Python reads in order generate the final HTML file.
- **\_\_init\_\_.py** -- contains the class `Movie`,  which is used to store movie information. To demonstrate inheritance, `Movie` inherits from a base class of `Media`.
- **utils.py** -- contains the main logic that generates the HTML file. The entry point is the function `create_and_open_webpage`.
- **demo.py** -- the main Python script to run, which does the instantiating and calls the appropriate functions.

## How to Run
Clone this repository to any location on your computer, or download this project as a ZIP file and extract it.

Navigate to the project directory. It should be at `movie_trailer_website/movie_trailer_website`. You should see a file called **demo.py.**

From the command line, run the following:
```console
python demo.py
```

Your default web browser should open the newly-generated web page in a new tab.

## Miscellaneous
This project borrows from the code used in the "Make Classes: Movie Website" lesson in Udacity's *Programming Foundations with Python* course, but extensive changes were made. For example, the HTML template is not initially stored in Python but is instead read and imported into Python from external files.
