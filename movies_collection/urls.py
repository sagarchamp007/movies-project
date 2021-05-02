from django.urls import path, re_path
from movies_collection.views import MoviesView, CollectionView


from . import views

urlpatterns = [
    path('movies/', MoviesView.as_view()),
    path('collection/', CollectionView.as_view()),
    path('collection/<uuid:c_uuid>/', CollectionView.as_view())
    # re_path(r'^collection/$', CollectionView.as_view()),
    # re_path(r'^collection/(?P<c_uuid>\w+)/$', CollectionView.as_view())


]