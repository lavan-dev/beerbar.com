from django.contrib import admin
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from beerbar.views import TaskViewSet, CreateuserView
from beerbar import views

router = routers.DefaultRouter()
# router = routers.SimpleRouter()
router.register(r'task', views.TaskViewSet)
# router.register('completed_task', views.CompletedTaskViewSet)
# router.register('due_task', views.DueTaskViewSet)

urlpatterns = [
    url(r'register/$', views.CreateuserView.as_view(), name='user'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^beerbar/', include('beerbar.urls')),

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
