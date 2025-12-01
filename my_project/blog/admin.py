from django.contrib import admin
from .models import Autor, Editora, Livro, Publica

# Register your models here.

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome']
    search_fields = ['nome']

@admin.register(Editora)
class EditoraAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome']
    search_fields = ['nome']

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin): 
    list_display = ['id', 'titulo', 'ISBN', 'publicacao', 'preco', 'estoque', 'editora']
    search_fields = ['titulo', 'ISBN']

@admin.register(Publica)
class PublicaAdmin(admin.ModelAdmin):
    list_display = ['id', 'autor', 'livro']
    search_fields = ['autor__nome', 'livro__titulo']




