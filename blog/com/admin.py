
from django.contrib import admin
from .models import Nomera

#class NomeraAdmin(admin.ModelAdmin):
   # list_display = ('user_name', 'email', 'is_approved')  # добавить is_approved в список

#admin.site.register(Nomera, NomeraAdmin)

admin.site.register(Nomera)

# Register your models here.
