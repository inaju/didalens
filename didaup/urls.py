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
    path('partner/<int:user_id>/', views.create_accountability_partners, name='partner_link'),
    path('showpartner/', views.show_partner, name='showpartner'),
    path('partnererror/', views.partner_error, name='partnererror'),
    path('goalreminder/', views.failed_goal_list, name='goalreminder'),
    path('ask_a_friend/', views.ask_a_friend, name='ask_a_friend'),
    path('ask_a_friend/<int:user_id>/', views.ask_a_friend, name='ask_a_friend_link'),
    path('thankyou/', views.thank_you, name='thank_you'),
    path('fakeemail/', views.send_test_email, name='fake_email'),
    path('aboutdidalens/', views.about_didalens, name='fake_email'),
    path('detailserror/', views.details_error, name='details_error'),
    path('makegoalfalse/', views.make_goal_false, name='make_goal_false'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
