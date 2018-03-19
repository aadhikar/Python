import media, movie_builder;

toy_story = media.Movie("Toy Story",
						"A cowboy doll is profoundly threatened and jealous when a new spaceman figure supplants him as top toy in a boy's room.",
						"https://lumiere-a.akamaihd.net/v1/images/c3c2b4a3323c4a71929cd5fc76bcda4df7157175.jpeg?region=0%2C0%2C1024%2C320",
						"https://www.youtube.com/watch?v=k1B9ij4noks&feature=youtu.be");

# print "{0}".format(toy_story.title);
# print "{0}".format(toy_story.storyline);
# toy_story.show_trailer();

avatar = media.Movie("Avatar (2009)",
					"A paraplegic marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.",
					"https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg",
					"http://www.imdb.com/title/tt0499549/videoplayer/vi531039513?ref_=tt_ov_vi");

# print "{0}".format(avatar.title);
# print "{0}".format(avatar);
# avatar.show_trailer();

mi6_fallout = media.Movie("Mission: Impossible - Fallout (2018)",
						"Ethan Hunt and his IMF team, along with some familiar allies, race against time after a mission gone wrong.",
						"http://thewordofward.co.uk/wp-content/uploads/2018/02/fallout.jpg",
						"https://youtu.be/wb49-oV0F78");

# print "{0}".format(mi6_fallout.title);
# print "{0}".format(mi6_fallout.storyline);
# mi6_fallout.show_trailer();

movies_list = [toy_story];
movies_list.append(avatar);
movies_list.append(mi6_fallout);


# movie_builder.open_movies_page(movies_list);
print "{0}".format(media.Movie.MOVIE_RATINGS);
print "__doc__ {0}".format(media.Movie.__doc__);
print "__name__ {0}".format(media.Movie.__name__);
print "__module__ {0}".format(media.Movie.__module__);
print "__dict__ {0}".format(media.Movie.__dict__);
print "__bases__ {0}".format(media.Movie.__bases__);