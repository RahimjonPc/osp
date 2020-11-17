from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from .views import HomeDetailView, delete

app_name = 'foods'

urlpatterns = [
    path('order/<int:pk>', HomeDetailView.as_view(), name="order"),
    path('delete/<int:pk>', delete, name="delete"),
]

urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)