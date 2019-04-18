from django.urls import path
from . import views
urlpatterns = [
    # path('', views.HomeView.as_view, name='home'),
    # path('login', views.loginView, name='login'),
    path('', views.HomeView.as_view(), name="home"),
    path('about', views.AboutView.as_view(), name="about"),
    path('beautifulsoup', views.BeautifullSoup.as_view(), name="beautifulsoup"),
]