from django.urls import path
from rooms import views as room_viwes

app_name = "core"

urlpatterns = [path("", room_viwes.HomeView.as_view(), name="home")]
