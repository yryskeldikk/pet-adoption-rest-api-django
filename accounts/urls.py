from django.urls import path, include
from . import views


app_name = "accounts"
urlpatterns = [
    path("register/",views.AccountCreateView.as_view(),name='create-account'),
    path('<int:pk>/', views.AccountRetrieveUpdateDestroyView.as_view(), name = 'account-retrieve-update-destory'),
    path('all/', views.AccountListView.as_view(), name = "account-list"),
]
