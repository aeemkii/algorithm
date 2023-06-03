from django.urls import path
from .views import QuestionView, CategoryView, ServicesView, AboutUsView, TeamView, InformationView, ContactsView

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
   
   path('docs/', schema_view.with_ui("swagger")),    
    
   path('questions_list/', QuestionView.as_view()),
   path('categories_list/', CategoryView.as_view()),
   path('services_list/', ServicesView.as_view()),
   path('aboutus_list/', AboutUsView.as_view()),
   path('team_list/', TeamView.as_view()),
   path('information_list/', InformationView.as_view()),
   path('contacts_list/', ContactsView.as_view()),

]
