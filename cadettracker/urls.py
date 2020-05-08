from django.contrib import admin
from django.urls import include, path


from . import views

app_name='cadettracker'
urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('company/<company_id>/', views.company, name='company'),
    path('modify/', views.modifysupplies, name='modifysupplies'),
    path('reg/<reg_id>/', views.reg, name='reg'),

]
