# from rest_framework import permissions
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi

from django.urls import path
from . import views


# schema_view = get_schema_view(
#    openapi.Info(
#     # title과 default_version은 필수 인자
#       title="우리반 API",
#       default_version='v1',
#    ),
#    public=True,
#    permission_classes=[permissions.AllowAny],
# )


urlpatterns = [
    path('articles/', views.article_list),
    path('articles/<int:article_pk>/', views.article_detail),
    path('comments/', views.comment_list),
    path('comments/<int:comment_pk>/', views.comment_detail),
    path('articles/<int:article_pk>/comments/', views.comment_create),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0)),
]
