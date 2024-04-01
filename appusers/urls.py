from django.urls import path
from .views import ViewHome, ViewAddClient, ViewArchived, ViewServiceEdit
urlpatterns = [
    path('', ViewHome, name="home"),
    path('addclient/<str:name>/<str:phonenumber>/<str:price>/<str:description>', ViewAddClient, name="addclient"),
    path('archived', ViewArchived,name='archived'),
    path('serviceedit/<str:status>/<int:id>', ViewServiceEdit,name='serviceedit')
]