from django.urls import path
from django.conf.urls import url
from . import views
from.views import AddLike,AddDislike
urlpatterns=[
    path('inside',views.inside,name="inside"),
    path('',views.home,name="home"),
    path('allposts2',views.allposts2,name="allposts2"),
    path('Post/<int:pk>/like/', AddLike.as_view(), name='like'),
    path('Post/<int:pk>/dislike/', AddDislike.as_view(), name='dislike'),
]
