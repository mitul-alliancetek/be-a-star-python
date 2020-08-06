from django.conf.urls import url
from django.urls import include, path

from users.views import UserRegistrationAPIView

urlpatterns = [
    path('users/', include('users.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path("rest-auth/registration/", UserRegistrationAPIView.as_view(), name="registration"),
]