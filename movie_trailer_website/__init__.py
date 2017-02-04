# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import webbrowser

from movie_trailer_website.utils import create_and_open_webpage

__all__ = [
    'create_and_open_webpage', 'Media', 'Movie',
]


class Media(object):
    """
    Base class representing a media object.

    Attributes:
        title (str): The title of the work.
        summary (str): A brief summary of the work.
        image_url (str): URL of the image of the media.
    """
    def __init__(self, title, summary, image_url):
        self.title = title
        self.summary = summary
        self.image_url = image_url

    # The "formal" string representation of the media object
    def __repr__(self):
        return '<{0}: {1}>'.format(self.__class__.__name__, self.title)

    # Informal, "short" string representation of the media object
    def __str__(self):
        return self.title


class Movie(Media):
    """
    A representation of a motion picture film (movie). Inherits from `Media`.

    Attributes:
        VALID_RATINGS (tuple): List of valid MPAA movie ratings.
        title (str): The movie's title.
        summary (str): A brief plot summary of the movie.
        image_url (str): URL of the image of the movie's poster or cover art.
        youtube_trailer_url (str): URL of the movie's trailer on YouTube.
        rating (str): The movie's MPAA rating. See VALID_RATINGS.
    """
    VALID_RATINGS = ('G', 'PG', 'PG-13', 'R')

    def __init__(self, title, summary, image_url, youtube_trailer_url, rating):
        super(Movie, self).__init__(title, summary, image_url)

        # `self.rating` is actually a property encapsulating the "true"
        # instance variable, which is `self._rating`. This is done to check
        # whether the rating is valid before setting it.
        self.rating = rating
        self.youtube_trailer_url = youtube_trailer_url

    @property
    def rating(self):
        """Return the film's rating."""
        return self._rating  # a "private" variable - the actual rating

    @rating.setter
    def rating(self, value):
        """Setter method for validating what gets stored in `_rating`"""

        # Throw an error if the suppied rating is not a valid one
        if value not in self.VALID_RATINGS:
            error_msg = "Invalid rating. Acceptable values are: {}"
            valid_ratings_list = ', '.join(r for r in self.VALID_RATINGS)
            raise ValueError(error_msg.format(valid_ratings_list))
        self._rating = value

    def show_trailer(self):
        """Open the movie's trailer on YouTube in a web browser."""
        webbrowser.open(self.youtube_trailer_url)
