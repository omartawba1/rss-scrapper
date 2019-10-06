from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views

urlpatterns = [
    path('', login_required(views.ScrapperListView.as_view()), name='rss.index'),
    path(r'<int:id>', login_required(views.ScrapperDetailsView.as_view()), name='rss.details'),
    path(r'favourites', login_required(views.FavouritesListView.as_view()), name='favourites.index'),
    path(r'favourites/<int:id>', login_required(views.FavouritesDetailsView.as_view()), name='favourites.details')
]
