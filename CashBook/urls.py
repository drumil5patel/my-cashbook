"""CashBook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from CashBook1 import views

urlpatterns = [
    path('admin/',admin.site.urls),
    path('blank_page/',views.blank_page),
    path('',views.home),

    path('accounts/',views.accounts),
    path('create-account/',views.create_account),
    path('add-account/',views.add_account),
    path('delete-account/<int:id>',views.delete_account),
    path('edit-account/<int:id>',views.edit_account),
    path('save-account/',views.save_account),
    path('data-tables/<int:id>',views.data_tables),
    path('create-entry/<int:id>',views.create_entry),
    path('add-entry/',views.add_entry),
    path('delete-entry/<int:id>',views.delete_entry),
    path('edit-entry/<int:id>',views.edit_entry),
    path('save-entry/',views.save_entry),

    path('reports/',views.reports),
    path('show-reports/',views.show_reports),
]