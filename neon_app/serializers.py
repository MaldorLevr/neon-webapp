from rest_framework import serializers
from neon_app.models import Day, Event, Block, Staff, About, Discover, Vacation, YearStart

class YearStartSerializer(serializers.ModelSerializer):
    date = serializers.DateField(format="20%y-%m-%dT00:00-07:00")

    class Meta:
        model = YearStart
        fields = ('date',)

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('name', 'time', 'info')

class BlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Block
        fields = ('start_time', 'end_time', 'rotation')

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ('name', 'type', 'title', 'email', 'website')

class DiscoverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ('name', 'type', 'website')

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ('about', 'support_email')

class VacationSerializer(serializers.ModelSerializer):
    start_date = serializers.DateField(format="20%y-%m-%dT00:00-07:00")
    end_date = serializers.DateField(format="20%y-%m-%dT00:00-07:00")

    class Meta:
        model = Vacation
        fields = ('name', 'start_date', 'end_date')

class DaySerializer(serializers.ModelSerializer):
    day_blocks = BlockSerializer(many=True, read_only=True)
    day_events = EventSerializer(many=True, read_only=True)
    date = serializers.DateField(format="20%y-%m-%dT00:00-07:00")

    class Meta:
        model = Day
        fields = ('date', 'day_type', 'name', 'announcement', 'day_blocks', 'day_events', 'school_start_time', 'school_end_time')
