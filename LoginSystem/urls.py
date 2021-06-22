from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url('home/', views.home, name="home"),
    path('logout/', views.logout, name="logout"),
    path('report/', views.report, name="report"),
    path('calendar/report/', views.view_query_show_report),

    path('calendar/', views.calendar, name="calendar"),
    path('calendar/view', views.view_query_event, name="view_query_event"),
    path('calendar/result/', views.view_query_show_event),
    path('calendar/get_event/', views.view_query_get_event, name="get_event"),

    path('calendar/delete/<int:pk>/', views.delete_event, name='delete_event'),
    path('calendar/update/<int:pk>/', views.update, name='update_event'),
    path('calendar/register/', views.calendar_register, name="calendar_register"),
    path('calendar/login/', views.calendar_login, name="calendar_login"),

    path('add_regulator/', views.add_regulator, name="add_regulator"),
    path('add_frequency/', views.add_frequency, name="add_frequency"),
    path('add_tax_payer/', views.add_tax_payer, name="add_tax_payer"),
    path('add_form_return/', views.add_form_return, name="add_form_return"),
    path('cal_data/', views.cal_data, name="cal_data"),

    path('check/', views.default_data, name="check"),
    path('all_event/', views.all_event, name="all_event"),

]
