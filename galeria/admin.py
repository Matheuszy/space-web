from django.contrib import admin
from galeria.models import Fotografia

class ListandoFotografia(admin.ModelAdmin):
    list_diplay = ("id", "nome", "legenda")

    list_display_links = ("id", "nome")
    search_fields = ("nome",)
    list_per_page = 10
    
    list_editable = ("legenda",)
    list_filter = ("categoria")

admin.site.register(Fotografia)


