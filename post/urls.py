from django.urls import path
from .import views


urlpatterns = [
    path('detail/<int:volunteer_id>',views.detail,name="detail"),
    path('apply',views.apply,name='apply'),
    path('update/<int:volunteer_id>/',views.update,name='update'),
    path('delete/<int:volunteer_id>/',views.delete,name='delete'),
]