from django.urls import path

from imagesizer.views import main, load_image, retrieve_image

urlpatterns = [
    path('main', main, name='main'),
    path('load_image', load_image, name='load_image'),
    path('retrieve_image/<str:title>', retrieve_image, name='retrieve_image'),
]
