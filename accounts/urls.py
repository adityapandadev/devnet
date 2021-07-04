
from django.urls import path, include

from accounts import views

from django.conf.urls import url
from .views import ExploreView

urlpatterns = [
    path('register/', views.register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    url('profile',views.profile, name = 'profile'),
    path('explore', ExploreView.as_view(), name = "explore"),
    path('send_request/<int:userID>/', views.send_request, name = 'send request'),
    path('accept_request/<int:requestID>/',views.accept_request, name = 'accept request')


]



