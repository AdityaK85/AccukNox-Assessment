from django.urls import path
from .views_api import *

urlpatterns = [
    path('user_login/', user_login ),
    path('user_signup/', user_signup ),
    path('get_user_by_email/', get_user_by_email ),
    path('get_user_by_name/', get_user_by_name ),
    path('send_frnd_request/', send_frnd_request ),
    path('accept_reject_request/', accept_reject_request ),
    path('my_requests/', my_requests ),
    path('my_requests/', my_requests ),
]