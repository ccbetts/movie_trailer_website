# -*- coding: utf-8 -*-
from __future__ import unicode_literals

try:
    from movie_trailer_website import Movie, create_and_open_webpage
except ImportError:
    # quick & dirty way of making Python recognize movie_trailer_website 
    # as a package in the event of an ImportError
    import sys
    from os.path import abspath, dirname

    # add the top-level 'movie_trailer_site' directory to the
    # $PATH / %PATH% environment variable
    sys.path.append(dirname(dirname(abspath(__file__))))
    
    from movie_trailer_website import Movie, create_and_open_webpage

hacksaw_ridge = Movie(
    title='Hacksaw Ridge',
    summary=(
        'The true story of the first conscientious objector to win '
        'the Medal of Honor.'
        ),
    image_url='https://upload.wikimedia.org/wikipedia/en/8/8a/Hacksaw_Ridge_poster.png',  # noqa
    youtube_trailer_url='https://www.youtube.com/watch?v=s2-1hz1juBI',
    rating='R',
)

pacific_rim = Movie(
    title='Pacific Rim',
    summary=(
        '2-pilot teams use giant fighting robots to defend earth '
        'from interdimensional giant monsters.'
        ),
    image_url='https://upload.wikimedia.org/wikipedia/en/f/f3/Pacific_Rim_FilmPoster.jpeg',  # noqa
    youtube_trailer_url='https://www.youtube.com/watch?v=5guMumPFBag',
    rating='PG-13',
)

rogue_one = Movie(
    title='Rogue One: A Star Wars Story',
    summary=(
        'A group of spies from the Rebel Alliance embark on a '
        'dangerious mission to steal the Death Star plans.'
        ),
    image_url='https://upload.wikimedia.org/wikipedia/en/d/d4/Rogue_One%2C_A_Star_Wars_Story_poster.png',  # noqa
    youtube_trailer_url='https://www.youtube.com/watch?v=sC9abcLLQpI',
    rating='PG-13',
)

tropic_thunder = Movie(
    title='Tropic Thunder',
    summary=(
        "Some actors attempt to make a movie set in the Vietnam "
        "War, but fail to realize that they're in an actual war."
    ),
    image_url='https://upload.wikimedia.org/wikipedia/en/d/d6/Tropic_thunder_ver3.jpg',  # noqa
    youtube_trailer_url='https://www.youtube.com/watch?v=T-6YhRZowgc',
    rating='R',
)

forrest_gump = Movie(
    title='Forrest Gump',
    summary=(
        'A slow-witted but kind man witnesses or influences many of '
        'the defining events of the latter half of the 20th century.'
        ),
    image_url='https://upload.wikimedia.org/wikipedia/en/6/67/Forrest_Gump_poster.jpg',  # noqa
    youtube_trailer_url='https://www.youtube.com/watch?v=bLvqoHBptjg',
    rating='PG-13',
)

groundhog_day = Movie(
    title='Groundhog Day',
    summary=(
        'An arrogant TV weatherman is forced to re-live the same '
        'day over and over until he becomes a better person.'
        ),
    image_url='https://upload.wikimedia.org/wikipedia/en/b/b1/Groundhog_Day_%28movie_poster%29.jpg',  # noqa
    youtube_trailer_url='https://www.youtube.com/watch?v=tSVeDx9fk60',
    rating='PG',
)

movies = [
    hacksaw_ridge,
    pacific_rim,
    rogue_one,
    tropic_thunder,
    forrest_gump,
    groundhog_day,
]

create_and_open_webpage(movies)
