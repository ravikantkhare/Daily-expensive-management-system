"""
URL configuration for diems project.

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
from myapp import views as v1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',v1.signup),
    path('login',v1.login),
    path('signsave',v1.signupsave),
    path('loginsave',v1.loginsave),
    path('home',v1.dashbord),
    path('Addexpence',v1.Addexpence),
    path('ExpenceSAve',v1.ExpenceSAve),
    path('Addincome',v1.Addincome),
    path('incomesave',v1.IncomeSAve),
    path('AllInCome',v1.AllIncome),
    path('Allexpence',v1.Allexpence),
    path('logout',v1.logout),
    
]
