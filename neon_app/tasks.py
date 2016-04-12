from huey.contrib.djhuey import crontab, db_periodic_task
from neon_app.models import Day
from icalendar import Calendar
import requests

pro_d_terms = ['Professional', 'Pro-D', 'Development']
holiday_terms = ['Holiday', 'Statutory', 'School Closed']
late_start_terms = ['Late Start']


@db_periodic_task(crontab(minute="*/5"))
def update_from_calendar():
    print("hello")
    r = requests.get("http://www.sd44.ca/school/windsor/"
                     "_LAYOUTS/15/scholantis/handlers/ical/"
                     "event.ashx?List=f13b021f-ee41-4705-ab17-1a2f36172f0b")
    cal = Calendar.from_ical(r.text)
    for event in (x for x in cal.subcomponents if x.name == 'VEVENT'):
        days = Day.objects.filter(name=event['summary']) \
            .filter(date=event['dtstart'].dt)
        if len(days) > 0:
            continue
        day_type = ""
        if any(x in event['summary'] for x in holiday_terms):
            day_type = "holiday"
        elif any(x in event['summary'] for x in late_start_terms):
            day_type = "late-start"
        elif any(x in event['summary'] for x in pro_d_terms):
            day_type = "pro-d"

        if 'summary' in event:
            name = event['summary']
        else:
            name = "Normal Day"

        if 'description' in event:
            announcement = event['description']
        else:
            announcement = ""

        day = Day(date=event['dtstart'].dt,
                  name=name,
                  day_type=day_type,
                  announcement=announcement)

        day.save()
