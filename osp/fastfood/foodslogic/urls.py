from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from .views import HomeListView, FoodCreateView, FoodEditView, MyProjectLoginView, RegisterUserView, MyProjectLogout

urlpatterns = [
    path('', HomeListView.as_view(), name="home"),
    path('create', FoodCreateView.as_view(), name="create"),
    path('edit/<int:pk>', FoodEditView.as_view(), name="edit"),
    path('login', MyProjectLoginView.as_view(), name="login"),
    path('register', RegisterUserView.as_view(), name="register"),
    path('logout', MyProjectLogout.as_view(), name="logout"),
]

urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)