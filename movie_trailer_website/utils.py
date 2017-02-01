# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import re
import webbrowser

with open('templates/site-template.html') as template_file:
    # Read and import the external main page HTML file 
    main_page_html = template_file.read()

with open('templates/html-head.html') as html_head_file:
    # Read and import the external HTML head file
    html_head = html_head_file.read()

with open('templates/movie-component.html') as movie_snippet_file:
    # Read and import the external movie snippet HTML file
    movie_snippet_html = movie_snippet_file.read()

with open('templates/main.js') as js_file:
    # Read and import the external JavaScript file
    javascript = js_file.read()




def get_youtube_video_id(youtube_url):
    """Extract the video ID from a YouTube video URL"""
    full_url_match = re.search(r'(?<=v=)[^&#]+', youtube_url)
    shortened_url_match = re.search(r'(?<=be/)[^&#]+', youtube_url)
    id_match = full_url_match or shortened_url_match
    try:
        video_id = id_match.group(0)
    except AttributeError:
        video_id = None
    return video_id


def create_movie_snippet_content(movies):
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        trailer_youtube_id = get_youtube_video_id(movie.youtube_trailer_url)

        # Append the HTML snippet for the movie with its content filled in
        content += movie_snippet_html.format(
            movie_title=movie.title,
            movie_image_url=movie.image_url,
            trailer_youtube_id=trailer_youtube_id,
            movie_summary=movie.summary,
            movie_rating=movie.rating,
        )
    return content


def create_and_open_webpage(movies):
    """
    Generate and open a movie trailers webpage from a list of Movie objects.

    Saves the webpage as 'movie-trailer-website.html'.

    Arguments:
        movies: A list or tuple of `movie_trailer_website.Movie` instances.
    """
    # Create or overwrite the output HTML file
    with open('movie-trailer-website.html', 'w') as output_file:
        webpage_content = main_page_html.format(
            html_head=html_head,
            movie_html_components=create_movie_snippet_content(movies),
            javascript=javascript,
        )
        output_file.write(webpage_content)

    # Get the absolute path of the newly-created output file
    url = os.path.abspath(output_file.name)

    # Open the new webpage! Hopefully, in a new tab.
    webbrowser.open('file://' + url, new=2)
