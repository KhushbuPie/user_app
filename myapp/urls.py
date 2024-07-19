from django.urls import path
from .views import PersonListCreate, PersonDetail

urlpatterns = [
    path('persons/', PersonListCreate.as_view(), name='person-list-create'),
    path('persons/<int:pk>/', PersonDetail.as_view(), name='person-detail'),
]
