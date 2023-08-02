from django.urls import path

from src.apps.api import views

# from .views import CommentCreateAPIView , UserPostListView, EditProfile



from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)   
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="PyNET.KG Api",
        default_version='v1',
        description="PyNET.KG Api",
        contact=openapi.Contact(email="ilgamkhisam@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)

urlpatterns = [
    path('', schema_view.with_ui("swagger")),
    path('singup/', views.RegisterUser.as_view(), name="singup" ),
    path('login/', views.MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('products/', views.ProductView.as_view(), name='product-list'),   
    path('products/product/<int:pk>/', views.ProductDetailView.as_view(), name='product-details'),
    path('add_to_favorite/<int:product_id>/', views.AddToFavorite.as_view(), name='add_to_favorite'),
    path('remove_from_favorite/<int:product_id>/', views.RemoveFromFavorite.as_view(), name='remove_from_favorite'),
]