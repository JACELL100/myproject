"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from myproject import views
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePage),
    path('about-us/', views.aboutUs),
    path('course/', views.Course),
    path('course/<int:courseid>', views.courseDetails),
    path('logineco/', views.Login, name='login'),
    path('userformeco/', views.userform),
    path('submitform/', views.submitform, name='submitform'),
    path('calculator/', views.calculator),
    path('evenodd/',views.evenodd),
    path('marksheet/',views.marksheet),
    path('services/',views.services),
    path('newsdetails/<slug>',views.newsdetails),
    path('saveenquiry/',views.saveEnquiry,name="saveenquiry"),
]


if settings.DEBUG:
    urlpatterns+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)