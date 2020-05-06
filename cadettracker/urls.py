from django.contrib import admin
from django.urls import include, path


from . import views

app_name='cadettracker'
urlpatterns = [
    #path('', views.index, name='index'),
    path('admin/', admin.site.urls),
]
