from django.shortcuts import render
from rest_framework import viewsets
from neon_app.models import Day, Event, About, Staff
from neon_app.serializers import DaySerializer, EventSerializer, AboutSerializer, StaffSerializer
from datetime import date


class DayViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        queryset = Day.objects.all()
        day = self.request.QUERY_PARAMS.get('d', None)
        month = self.request.QUERY_PARAMS.get('m', None)
        year = self.request.QUERY_PARAMS.get('y', None)

        if day is not None and month is not None and year is not None:
            requested_date = date(int(year), int(month), int(day))
            return queryset.filter(date=requested_date)
        return queryset

    serializer_class = DaySerializer

class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

class AboutViewSet(viewsets.ModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer