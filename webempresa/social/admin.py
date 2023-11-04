from django.contrib import admin
from .models import Link

# Register your models here.
class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated') # Para que el usuario no pueda editar los campos

    def get_readonly_fields(self, request, obj=None): # Para que el usuario no pueda editar los campos
        if request.user.groups.filter(name="Personal").exists(): # Si el usuario pertenece al grupo Personal
            return ('key', 'name')  # Puede editar los campos created y updated
        else:
            return ('created', 'updated') # Si no pertenece al grupo Personal, no puede editar los campos created y updated

admin.site.register(Link, LinkAdmin)