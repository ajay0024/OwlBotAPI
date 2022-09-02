from django.urls import path
from . import views

app_name = "owlbot"
urlpatterns = [
    path('', views.index, name='index'),
    path('word/<word>/', views.search_word, name="show_category"),
]
