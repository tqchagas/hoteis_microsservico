from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from hoteis import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hoteis/', views.HotelCriarListar.as_view()),
    path('hoteis/<int:pk>/', views.HotelDetalheApagar.as_view())
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
