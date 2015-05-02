from django.db import models

# Create your models here.

class Block(models.Model):
	start_time = models.TimeField(blank=True, null=True)
	end_time = models.TimeField(blank=True, null=True)

class Day(models.Model):
	date = models.DateField()
	name = models.CharField(max_length=100)
	day_type = models.CharField(max_length=20, default="normal")
	description = models.TextField(blank=True, null=True)
	school_start_time = models.TimeField(blank=True, null=True)
	block_1 = models.ForeignKey('Block', related_name='block_1', blank=True, null=True)
	block_2 = models.ForeignKey('Block', related_name='block_2', blank=True, null=True)
	block_3 = models.ForeignKey('Block', related_name='block_3', blank=True, null=True)
	block_4 = models.ForeignKey('Block', related_name='block_4', blank=True, null=True)
	school_end_time = models.TimeField(blank=True, null=True)

	def __str__(self):
		return "{0} : {1}".format(self.date, self.name)
