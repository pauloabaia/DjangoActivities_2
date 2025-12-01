from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path("eco/<str:nome>/", views.HelloViews.eco),
    path("api/", views.HelloViews.api_info),
    path("home/", views.HelloViews.home, name="home"),
    path("contato/", views.HelloViews.contato, name="contato"),
    path("homeT/", views.HelloViews.homeGlobal, name="homeGlobal"),
    path("base/", views.HelloViews.base, name="base"),

    path("autores/new/", views.HelloViews.autor_create, name="autor_create"),
    path("autores/", views.HelloViews.list_autores, name="list_autores"),
    path("autores/<int:id>/edit/", views.HelloViews.autor_edit, name="autor_edit"),
    path("autores/<int:id>/delete/", views.HelloViews.autor_delete, name="autor_delete"),
    path("livros/new/", views.HelloViews.livro_create, name="livro_create"),
    path("livros/", views.HelloViews.list_livros, name="list_livros"),
    path("livros/<int:id>/edit/", views.HelloViews.livro_edit, name="livro_edit"),
    path("livros/<int:id>/delete/", views.HelloViews.livro_delete, name="livro_delete"),
    path("publicacoes/new/", views.HelloViews.publica_create, name="publica_create"),
    path("publicacoes/", views.HelloViews.list_publicacoes, name="list_publicacoes"),
    path("publicacoes/<int:id>/edit/", views.HelloViews.publica_edit, name="publica_edit"),
    path("publicacoes/<int:id>/delete/", views.HelloViews.publica_delete, name="publica_delete"),
    path("editoras/new/", views.HelloViews.editora_create, name="editora_create"),
    path("editoras/", views.HelloViews.list_editoras, name="list_editoras"),
    path("editoras/<int:id>/edit/", views.HelloViews.editora_edit, name="editora_edit"),
    path("editoras/<int:id>/delete/", views.HelloViews.editora_delete, name="editora_delete"),

    path("signup/", views.HelloViews.signup_view, name='signup'), 
    path("signin/", views.HelloViews.signin_view, name='signin'), 
    path("logout/", views.HelloViews.logout_view, name='logout'), 


]
