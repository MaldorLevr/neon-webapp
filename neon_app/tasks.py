from huey.contrib.djhuey import crontab, db_periodic_task
from neon_app.models import Day
from icalendar import Calendar
import requests


@db_periodic_task(crontab(minute="*"))
def update_from_calendar():
    r = requests.get('http://www.sd44.ca/school/windsor/_LAYOUTS/15/scholantis/handlers/ical/event.ashx?List=f13b021f-ee41-4705-ab17-1a2f36172f0b')
    cal = Calendar.from_ical(r.text)
    for event in (x for x in cal.subcomponents if x.name == 'VEVENT'):
        days = Day.filter(name=event['summary'])
        if len(days) > 0:
            continue
        if 'Statutory' in event['summary']:
            
