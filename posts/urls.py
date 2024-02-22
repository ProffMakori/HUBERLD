
from django.contrib import admin
from django.urls import path
from posts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/', views.create_post, name='create_post'),
    path('<int:post_id>/', views.post_detail, name='post_detail'),

]
