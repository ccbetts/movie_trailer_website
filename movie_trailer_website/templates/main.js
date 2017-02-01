// Add auto-playing YouTube movie trailer embed to modal upon clicking on a movie.
// Also add movie title, summary, and MPAA rating.
$(document).on('click', '.movie-clickable', function(event) {
  var trailerYouTubeID = $(this).data('youtube-trailer-id');
  var movieTitle = $(this).data('movie-title');
  var movieSummary = $(this).data('movie-summary');
  var movieRating = $(this).data('movie-rating');
  var sourceURL = 'http://www.youtube.com/embed/'+trailerYouTubeID+'?autoplay=1&html5=1&modestbranding=1&showinfo=0&rel=0';

  $('#embed-container').empty().append($('<iframe></iframe>', {
    'class': 'embed-responsive-item',
    'allowfullscreen': '',
    'src': sourceURL,
  }));
  
  $('#modal-movie-title').empty().html('<i>'+movieTitle+'</i> – Theatrical Trailer');
  $('#modal-movie-summary').empty().html(movieSummary);
  $('#modal-movie-rating').empty().html(movieRating);
});

// Remove all data (including video) from modal upon closing it
$(document).on('hidden.bs.modal', '#trailer-video-container', function(event) {
  $('#embed-container').empty();
  $('#modal-movie-title').empty();
  $('#modal-movie-summary').empty();
  $('#modal-movie-rating').empty();
});