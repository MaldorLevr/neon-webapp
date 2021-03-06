from huey.contrib.djhuey import crontab, db_periodic_task
from neon_app.models import Day
from icalendar import Calendar
from django.db import IntegrityError
from re import compile
import requests

pro_d_terms = ['Professional', 'Pro-D', 'Development']
holiday_terms = ['Holiday', 'Statutory', 'School Closed']
late_start_terms = ['Late Start']
early_dismissal_terms = ['Early Dismissal']


@db_periodic_task(crontab(minute="*/5"))
def update_from_calendar():
    r = requests.get("http://www.sd44.ca/school/windsor/"
                     "_LAYOUTS/15/scholantis/handlers/ical/"
                     "event.ashx?List=f13b021f-ee41-4705-ab17-1a2f36172f0b")
    cal = Calendar.from_ical(r.text)
    for event in (x for x in cal.subcomponents if x.name == 'VEVENT'):
        day_type = ""
        if any(x in event['summary'] for x in holiday_terms):
            day_type = "holiday"
        elif any(x in event['summary'] for x in late_start_terms):
            day_type = "late-start"
        elif any(x in event['summary'] for x in pro_d_terms):
            day_type = "pro-d"
        elif any(x in event['summary'] for x in early_dismissal_terms):
            day_type = "early-d"
        else:
            day_type = "normal"

        if 'summary' in event:
            rotation_regex = compile("^[0-9], [0-9], [0-9], [0-9]$")
            # check if day is just a rotation
            if rotation_regex.match(event['summary']):
                name = "Normal Day"
            else:
                name = event['summary']
        else:
            name = "Normal Day"

        if 'description' in event:
            announcement = event['description']
        else:
            announcement = ""

        try:
            day = Day(date=event['dtstart'].dt,
                      name=name,
                      day_type=day_type,
                      announcement=announcement)

            day.save()
        except IntegrityError as ex:
            # Log ex here once logging is configured
            pass
