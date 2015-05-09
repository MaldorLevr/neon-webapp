from rest_framework import serializers
from neon_app.models import Day, Event, Block

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('name', 'time', 'info')

class BlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Block
        fields = ('start_time', 'end_time', 'rotation')

class DaySerializer(serializers.ModelSerializer):
    day_blocks = BlockSerializer(many=True, read_only=True)
    day_events = EventSerializer(many=True, read_only=True)

    class Meta:
        model = Day
        fields = ('date', 'day_type', 'name', 'announcement', 'day_blocks', 'day_events', 'school_start_time', 'school_end_time')
