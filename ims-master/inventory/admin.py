from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import *

#admin.site.register(Product)

@admin.register(Product, Windows, Linux, Network)
class ViewAdmin(ImportExportModelAdmin):
    exclude = ('id', )
