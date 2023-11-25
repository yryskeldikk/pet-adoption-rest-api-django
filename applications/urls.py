from django.urls import path, include
from . import views

app_name = "applications"
urlpatterns = [
    path("",views.ApplicationCreateView.as_view(),name='create-application'),
    path("<int:pk>/",views.ApplicationRetrieveUpdateView.as_view(),name='retrieve-update-application'),
    path("all/<str:status>/" ,views.AppplicationListView.as_view(), name = "list-application"),
]