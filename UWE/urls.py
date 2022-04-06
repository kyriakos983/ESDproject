"""UWE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from UWE import views
from UWE.views import UpdateMovieView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home, name="home"),
    path('', include('allAccounts.urls')),
    path('about_us', views.about_us, name='about_us'),
    path('films', views.MoviesView, name='films'),
    path('offers&discounts', views.DiscountView, name='offers&discounts'),
    path('add-movie', views.addMovie, name='add-movie'),
    path('add-club', views.addClub, name='add-club'),
    path('delete_movie/<movie_id>', views.delete_movie, name='delete_movie'),
    path('<str:id>/update_movie_details/',UpdateMovieView.as_view(), name='update_movie_details'),
    path('product/<str:name>/<int:id>', views.movie_details, name='movieDetails'),
    path('<int:pk>/update_profile_page/',UpdateMovieView.as_view(), name='update-movie-details'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)