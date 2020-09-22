from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from thingstodo import views                            # add this

router = routers.DefaultRouter()
router.register(r'todos', views.TodoView, 'thingstodo')     # add this

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include(router.urls))                # add this
]