from django.db import models

# Model relationships
#==================================
#Many to Many relationships are:
#	DJs and Genres
# 	DJs and Cities
#	DJs and Events
# 	Events and Venues
#==================================
#One to Many relationships are:
#	DJ to Messages
#	City to Venues
	
class DJ(models.Model):
	dj_name = models.CharField(max_length=75)
	email = models.EmailField(max_length=254)
	username = models.CharField(max_length=75)
	password = models.CharField(max_length=10)

class Event(models.Model):
	event_date = models.DateTimeField('date of event')
	event_time = models.DateTimeField('time of event')
	dj_id = models.ForeignKey(DJ)
	venue_id = models.ForeignKey(Venue)

class City(models.Model):
	city_name = models.CharField(max_length=75)
	state = models.CharField(max_length=75)
	dj_id = models.ForeignKey(DJ)

class Genre(models.Model):
	genre_name = models.CharField(max_length=100)
	dj_id = models.ForeignKey(DJ)

class Message(models.Model):
	message = models.TextField
	email = models.EmailField(max_length=254)
	dj_id = models.ForeignKey(DJ)

class Venue(models.Model): 
	address = models.CharField(max_length=250)
	age_restriction = models.CharField(max_length=10)
	city_id = models.IntegerField(default=)


