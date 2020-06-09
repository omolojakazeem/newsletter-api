from django.contrib import admin
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import path, include
from django.views.generic import RedirectView
from rest_framework import permissions
from rest_framework_swagger.views import get_swagger_view
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Team Superman Newsletter API ",
        default_version='v1',
        description="Developed by Team Superman - For HNGi7 Task 2.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/subscriber/', include('subscriber.urls')),
    path('api/v1/newsletter/', include('newsletter.urls')),
    path('api/v1/dispatch/', include('dispatch.urls')),
    path('api/v1/accounts/', include('user.urls')),

    path('swagger(<format>\.json|\.yaml\)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('documentation/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('images/favicon.png')))

]
