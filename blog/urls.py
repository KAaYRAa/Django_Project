
from django.urls import path
from .views import *


urlpatterns = [
    path("", start_page ,name="start-page"),
    path("posts/",posts , name="posts"),
    path("posts/<slug:slug>",post_detail, name="post-detail"),
]
