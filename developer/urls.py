from django.urls import path

from . import views
from .views import DevDetailVue, IndexView

app_name = 'developer'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>/', DevDetailVue.as_view(), name='detail'),
    path('create/', views.create, name='create'),
    path('delete/<int:id>', views.delete, name='delete')
]