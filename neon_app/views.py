from django.shortcuts import render
from rest_framework import viewsets
from neon_app.models import Day, Event, About, Staff, Discover, Vacation, YearStart, DeviceToken
from neon_app.serializers import DaySerializer, EventSerializer, AboutSerializer, StaffSerializer, DiscoverSerializer, VacationSerializer, YearStartSerializer
from datetime import date
from django.http import HttpResponse
import json


def register_token(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        if body["app_id"] == "xenon_id_placeholder":
            android_tokens = body["_push"]["android_tokens"]
            ios_tokens = body["_push"]["ios_tokens"]
            if body["unregister"]:
                # unregister stuff
                for token in ios_tokens:
                    db_token = DeviceToken.objects.get(token=token, os="ios")
                    db_token.active = False
                    db_token.save()
                for token in android_tokens:
                    db_token = DeviceToken.objects.get(token=token, os="android")
                    db_token.active = False
                    db_token.save()
            else:
                # resgister stuff
                for token in ios_tokens:
                    db_token = DeviceToken(token=token, os="ios")
                    db_token.save()
                for token in android_tokens:
                    db_token = DeviceToken(token=token, os="android")
                    db_token.save()
        elif body["token_invalid"]:
            # invalidate token
    else:
        response = HttpResponse("Invalid method")
        response.status_code = 405
        return response


class DayViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        queryset = Day.objects.all()
        day = self.request.query_params.get('d', None)
        month = self.request.query_params.get('m', None)
        year = self.request.query_params.get('y', None)

        if day is not None and month is not None and year is not None:
            requested_date = date(int(year), int(month), int(day))
            return queryset.filter(date=requested_date)
        return queryset

    serializer_class = DaySerializer


class YearStartViewSet(viewsets.ModelViewSet):
    queryset = YearStart.objects.all()
    serializer_class = YearStartSerializer


class VacationViewSet(viewsets.ModelViewSet):
    queryset = Vacation.objects.all()
    serializer_class = VacationSerializer


class DiscoverViewSet(viewsets.ModelViewSet):
    queryset = Discover.objects.all()
    serializer_class = DiscoverSerializer


class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer


class AboutViewSet(viewsets.ModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
