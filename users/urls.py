from django.conf.urls import url
from users.views import UserRegistrationView


urlpatterns = [
    url('', UserRegistrationView.as_view()),
    ]