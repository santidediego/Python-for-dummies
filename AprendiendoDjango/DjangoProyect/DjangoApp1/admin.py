from django.contrib import admin
from DjangoApp1.models import Bares, Tapas

# Add in this class to customized the Admin Interface
class BaresAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('nombre',)}


admin.site.register(Bares, BaresAdmin)
admin.site.register(Tapas)
