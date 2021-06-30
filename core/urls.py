from django.contrib import admin
from django.urls import path, include

from tracker.tasks import get_data
from tracker.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="Home page"),
    path('api/v1/', include("tracker.api.v1.urls")),
    path('api/v2/', include("tracker.api.v2.urls")),


]

get_data(repeat=120, verbose_name="get_data")
