from django.conf.urls import patterns, include, url
from django.contrib import admin
from neon_app import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'days', views.DayViewSet, 'Day')

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'neon_webapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls, namespace='api'))
)
