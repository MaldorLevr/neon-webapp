from django.contrib import admin
from neon_app.models import Day, Block, Event, About, Staff, Discover, Vacation, YearStart, DeviceToken

# Register your models here.

admin.site.register(Event)
admin.site.register(Block)
admin.site.register(Day)
admin.site.register(About)
admin.site.register(Staff)
admin.site.register(Discover)
admin.site.register(Vacation)
admin.site.register(YearStart)
admin.site.register(DeviceToken)
