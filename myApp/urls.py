
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from myApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.home),
    path('home', views.home),
    path('createPost/' , views.createPost , name='createPost'),
    path('signup/', views.signup),
    # path('loginn/', views.loginn),
    path('', views.loginn),
    path('logoutt/', views.logoutt),
    # path('upload', views.upload),
    path('upload', views.upload),
    #path('createPost/upload' , views.upload),
    path('like-post/<str:id>' , views.likes , name = 'like-post'),
   # path('add_comment/<int:post_id>/', views.add_comment, name='add_comment'),
    path('add_comment/<uuid:post_id>/', views.add_comment, name='add_comment'),
    path('explore',views.explore),
    path('inprogress',views.inProgress),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

