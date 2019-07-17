from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig


class MyAdminConfig(AdminConfig):
    default_site = 'store.admin.MyAdminSite'


class StoreConfig(AppConfig):
    name = 'store'
