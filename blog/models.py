from django.db import models

# Create your models here.

class Blog(models.Model):
	title = models.CharField(max_length=100)
	pub_date = models.DateTimeField()
	body = models.TextField(max_length=1000)
	image = models.ImageField(upload_to='images/')


	def summary(self):
		return self.body[:70]

	def __str__(self):
		return self.title