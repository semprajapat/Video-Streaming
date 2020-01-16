from django.urls import path
from .views import VideoPlay

v1 = VideoPlay.as_view({
    'get':'list',
    'post':'create',
})

v2 = VideoPlay.as_view({
    'get':'retrieve',
    'put':'update',
    'delete':'destroy',
})


urlpatterns = [
    path('api/',v1),
    path('api/<int:pk>/',v2)
]
