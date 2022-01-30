from django.conf.urls.static import static
from django.urls import path

from PescarModern import settings
from . import views

app_name = 'magazine'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('istoric/', views.about, name='istoric'),
    path('reviste/', views.magazine_all, name='magazines'),
    path('<slug:slug>', views.magazine_detail, name='pdf_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
