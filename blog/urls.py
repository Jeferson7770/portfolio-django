from django.urls import path
from blog import views

urlpatterns = [
    path('', views.PostView.as_view(), name='index'),       # direto na raiz (/)
    path('home/', views.PostView.as_view(), name='home'),   # (/home/)
    path("<slug:slug>/", views.PostDetail.as_view(), name='post_detail')
]