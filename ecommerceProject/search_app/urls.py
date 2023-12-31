from django.urls import path
from .import views
from django.conf.urls.static import static
from ecommerceProject import settings

app_name = 'search_app'
urlpatterns = [
    path('', views.searchResult, name='search')
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
