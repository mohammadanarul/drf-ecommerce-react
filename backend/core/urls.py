from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('accounts.urls')),
    path('', include('store.urls')),
    path('category/', include('category.urls')),
]


# handler400 = 'views.bad_request'
# handler403 = 'views.permission_denied'
# handler404 = 'views.page_not_found'
# handler500 = 'views.server_error'

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += path('__debug__/', include(debug_toolbar.urls)),