from django.urls import path
from . import views

app_name = 'app'
urlpattern = [
    path('',views.index,name='index'),
    path('diag_1',views.get_diag_1,name='diag_1'),
    path('finish',views.finish,name='finish'),
]