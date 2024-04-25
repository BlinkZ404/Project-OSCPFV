from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeView.as_view(), name='home-page'),
    path('home/', views.HomeView.as_view(), name='home-page'),
    path('login/', views.login, name='login-page'),
    path('signup/', views.signup, name='signup-page'),
    path('logout/', views.logOut, name='logout'),
    path('profile/', views.profile, name= 'profile-page'),
    path('', include('product.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)