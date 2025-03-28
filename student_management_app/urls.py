from django.urls import path
from .views import home, delete_prof, create_profile


urlpatterns = [
   path('', home, name='home'),
   path('delete_prof/<int:id>/', delete_prof, name='delete_prof'),
   path('create_profile/', create_profile, name='create_profile'),
]



