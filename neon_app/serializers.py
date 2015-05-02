from rest_framework import serializers
from neon_app.models import Day

class DaySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Day
		fields = ('date', 'day_type', 'name', 'description', 'school_start_time', 'school_end_time')
