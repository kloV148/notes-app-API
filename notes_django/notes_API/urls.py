from django.urls import path
from .views import NoteViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = "notes_API"

urlpatterns = [
    # login and register
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # note api
    path('notes/', NoteViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('notes/<int:pk>', NoteViewSet.as_view({
        'get': 'retrieve',
        'patch': 'partial_update',
        'delete': 'destroy'
    })),
]
