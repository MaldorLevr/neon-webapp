from django.db import models


class About(models.Model):
    about = models.TextField()
    support_email = models.CharField(max_length=100)


class Staff(models.Model):
    name = models.CharField(max_length=100)
    #type should be: teacher, admin, support, other
    type = models.CharField(max_length=100)
    title = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    website = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=100)
    time = models.TimeField(blank=True, null=True)
    info = models.TextField(blank=True, null=True)

    def __str__(self):
        return "{0} : {1}".format(self.name, self.time)


class Block(models.Model):
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    rotation = models.SmallIntegerField(blank=True, null=True)

    def __str__(self):
        return "{0} : {1}".format(self.start_time, self.rotation)


class YearStart(models.Model):
    date = models.DateField()

    def __str__(self):
        return self.date.__str__()


class Vacation(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name


class Discover(models.Model):
    name = models.CharField(max_length=100)
    # type should be: academic, athletic, art, other
    type = models.CharField(max_length=100)
    website = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class Day(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=100)
    announcement = models.TextField(blank=True, null=True)
    day_type = models.CharField(max_length=20, default="normal")
    school_start_time = models.TimeField(blank=True, null=True)
    day_blocks = models.ManyToManyField('Block', blank=True)
    day_events = models.ManyToManyField('Event', blank=True)
    school_end_time = models.TimeField(blank=True, null=True)

    def __str__(self):
        return "{0} : {1}".format(self.date, self.name)


class DeviceToken(models.Model):
    token = models.CharField(max_length=100)
    os = models.CharField(max_length=40)
    active = models.BooleanField(default=True)

    def __str__(self):
        return "{0}: {1}".format(self.token, self.os)
