from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.create_goal, name='create_goal'),
    path('secondgoal/', views.create_goal_two, name='create_goal_two'),
    path('thirdgoal/', views.create_goal_three, name='create_goal_three'),
    path('details/', views.daily_details, name='daily_details'),
    path('details_two/', views.daily_details_two, name='daily_details_two'),
    path('details_three/', views.daily_details_three, name='daily_details_three'),
    path('show/', views.show, name='show'),
    path('goalfull/', views.goalfull, name='goalfull'),
    path('partner/', views.create_accountability_partners, name='partner'),
    path('showpartner/', views.show_partner, name='showpartner'),
    path('partnererror/', views.partner_error, name='partnererror'),
    path('goalreminder/', views.failed_goal_list, name='goalreminder'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
