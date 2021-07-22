from django.urls import path

from . import views

app_name = "app"

urlpatterns = [
    path('form/', views.add_agenda, name="add_agenda"),
    path('list/<list_id>', views.list_agenda, name='list_agenda'),
    path('delete/<list_id>', views.delete_agenda, name='delete_agenda'),
    path('calendar/', views.calendar, name = 'calendar'),
]