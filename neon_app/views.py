from django.shortcuts import render
from rest_framework import viewsets
from neon_app.models import Day
from neon_app.serializers import DaySerializer
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
