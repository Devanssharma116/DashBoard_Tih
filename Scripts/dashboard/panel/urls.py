"""
URL configuration for dashboard project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from panel.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('SD/',receipts),
    path ('SDS/',table1),
    path ('table/',table2),
    path('delete/<id>',delete),
    path ('LA/',letureAdd),
    path ('LS/',letureShow),
    path('delete1/<id>',delete1),
    path ('CHA/',courseHAdd),
    path ('CHS/',courseHShow),
    path('deleteH/<id>',deleteH),
    path ('CA/',courseJAdd),
    path ('CS/',courseJShow),
    path('deleteJ/<id>',deleteJ),
    path ('AA/',AssignAdd),
    path ('AS/',AssignShow),
    path('deleteA/<id>',deleteA),
    path ('NA/',NotesAdd),
    path ('NS/',NotesShow),
    path('deleteN/<id>',deleteA),
    path ('TA/',TestAdd),
    path ('TS/',TestShow),
    path('deleteN/<id>',deleteT)
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
