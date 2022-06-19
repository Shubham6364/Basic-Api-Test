from django.db import models

# Create your models here.

class Api(models.Model):
	name = models.CharField(max_length=255)

	class Admin:
		pass

	def __unicode__(self):
		return u'%s %s' % (name)


