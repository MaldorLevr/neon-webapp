from rest_framework import viewsets
from neon_app.models import Day, Event, About, Staff, Discover, Vacation, YearStart, DeviceToken
from neon_app.serializers import DaySerializer, EventSerializer, AboutSerializer, StaffSerializer, DiscoverSerializer, VacationSerializer, YearStartSerializer
from datetime import date
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
import json
import requests
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import user_passes_test


@csrf_exempt
def register_token(request):
    if request.method == 'POST':
        tokens = DeviceToken.objects.filter(token=request.body)
        print(request.body)
        if len(tokens) < 1:
            db_token = DeviceToken(token=request.body)
            db_token.save()
            response = HttpResponse("OK")
            response.status_code = 200
            return response
        else:
            response = HttpResponse("Device Token already exists")
            response.status_code = 400
            return response
    else:
        response = HttpResponse("Invalid method")
        response.status_code = 405
        return response


@user_passes_test(lambda u: u.is_superuser)
def send_notification(request):
    if request.method == 'POST':
        tokens = DeviceToken.objects.filter(active=True)
        token_array = []

        for token in tokens:
            token_array.append(token.token)

        title = request.POST['title']
        message = request.POST['message']

        headers = \
            {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + settings.IONIC_API_KEY,
            }
        contents = \
            {
                'tokens': token_array,
                'profile': "build",
                'notification':
                {
                    'title': title,
                    'message': message,
                }
            }
        requests.post('https://api.ionic.io/push/notifications',
                      headers=headers,
                      data=json.dumps(contents))
        print(json.dumps(contents))
        return redirect('/send-notification/')
    else:
        return render(request, 'notification_form.html')


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
