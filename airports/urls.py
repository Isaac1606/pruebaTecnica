from django.contrib import admin
from django.urls import path
from .views import orginal_table, table_with_native_name

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/original_table/', orginal_table, name='original_table'),
    path('api/table_with_native_name/', table_with_native_name, name='table_with_native_name'),
]