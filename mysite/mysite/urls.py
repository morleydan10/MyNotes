"""
URL configuration for mysite project.

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
from django.contrib import admin
from django.urls import path, include
from notes import views

urlpatterns = [
    # admin path
    path("admin/", admin.site.urls),

    # user paths
    path("notes/", views.notes_list),
    path('notes/<int:pk>/', views.note_detail),
    path('notes/login/', views.login_form)
]


# When you first start the development server, you will most likely get a 404 error message.  To get the correct view, make sure the http has the corresponding url from above (in this case, http://127.0.0.1.8000/notes/)