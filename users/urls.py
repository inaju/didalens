from django.urls import path, include
from . import views
urlpatterns = [
   path('account/', include('django.contrib.auth.urls')),
   path('signup/', views.Signup.as_view(), name='signup')
]