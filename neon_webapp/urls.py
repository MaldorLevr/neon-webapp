from django.conf.urls import include, url
from django.contrib import admin
from neon_app import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'days', views.DayViewSet, 'Day')
router.register(r'staff', views.StaffViewSet, 'Staff')
router.register(r'about', views.AboutViewSet, 'About')
router.register(r'discover', views.DiscoverViewSet, 'Discover')
router.register(r'vacation', views.VacationViewSet, 'Vacation')
router.register(r'yearstarts', views.YearStartViewSet, 'YearStart')

urlpatterns = [
    # Examples:
    # url(r'^$', 'neon_webapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls, namespace='api')),
    url(r'^register-device/', views.register_token),
    url(r'^send-notification/', views.send_notification),
]
