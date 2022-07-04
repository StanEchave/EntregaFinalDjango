
from django.contrib import admin
from django.urls import path,include

#importo settings y static para las imagenes
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("blogs.urls")),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include("accounts.urls")),

]

#creo la ruta para las imagenes de manera dinamica
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)