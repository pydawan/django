"""_mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path



urlpatterns = [
    path('admin/', admin.site.urls),
    # Adicionando as urls `accounts` que o Django já tem prontas.
    # Templates pode ser modificados em `templates/registration`.
    path('accounts/', include('django.contrib.auth.urls')),
    # Rest
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # Aplicativos.
    path('', include('home.urls')),
    path('axios/', include('axios.urls')),
    path('blog/', include('blog.urls')),
    path('gitignore/', include('gitignore.urls')),
    path('jquery/', include('jquery.urls')),
    path('jsfetch/', include('jsfetch.urls')),
    path('jsxmlhttprequest/', include('jsxmlhttprequest.urls')),
    path('leafletjs/', include('leafletjs.urls')),
    path('note/', include('note.urls')),
    path('poll/', include('poll.urls')),
    path('upload/', include('upload.urls')),
    # Configurando arquivos de media, não fazer isso em produção!
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)