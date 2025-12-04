from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import View
from django.http import JsonResponse
from datetime import date
from .forms import AutorForm, EditoraForm, LivroForm, PublicaForm, SignUpForm, SignInForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.http import url_has_allowed_host_and_scheme

from django.http import HttpResponseNotAllowed



# Create your views here.
class HelloViews(View):

    def get(self,request):
        return HttpResponse("Hello, my fella! Welcome to my blog")
    
    def eco (request, nome):
        return HttpResponse(f"Hello, dear {nome}!")
    
    def api_info(request):
        data = {"curso": "Django", "nivel":"iniciante"}
        return JsonResponse(data)
    
    def home(request):
        from .models import Autor, Editora, Livro, Publica
        
        contexto = {
            "total_autores": Autor.objects.count(),
            "total_editoras": Editora.objects.count(),
            "total_livros": Livro.objects.count(),
            "total_publicacoes": Publica.objects.count(),
        }
        return render(request, "blog/home.html", contexto)
    
    def contato (request):
        return render(request, "blog/contato.html")
    
    def homeGlobal (request):
        return render(request, "global/home.html")
    
    def base (request):
        return render(request, "global/base.html")    
    
    def autor_create(request):
        if request.method == 'POST':
            form = AutorForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect ('blog:list_autores')
        else:
            form = AutorForm()
        return render(request, 'blog/autor_form.html', {'form': form})
    
    def list_autores(request):
        from .models import Autor
        autores = Autor.objects.all()
        return render(request, 'blog/autor_list.html', {'autores': autores})
    
    def autor_edit(request, id):
        from .models import Autor
        autor = get_object_or_404(Autor, pk=id)
        if request.method == 'POST':
            form = AutorForm(request.POST, instance=autor)
            if form.is_valid():
                form.save()
                return redirect('blog:list_autores')
        else:
            form = AutorForm(instance=autor)
        return render(request, 'blog/autor_form.html', {'form': form, 'autor': autor})
    
    def editora_create(request):
        if request.method == 'POST':
            form = EditoraForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect ('blog:list_editoras')
        else:
            form = EditoraForm()
        return render(request, 'blog/editora_form.html', {'form': form})
    
    def list_editoras(request):
        from .models import Editora
        editoras = Editora.objects.all()
        return render(request, 'blog/editora_list.html', {'editoras': editoras})
    
    def editora_edit(request, id):
        from .models import Editora
        editora = get_object_or_404(Editora, pk=id)
        if request.method == 'POST':
            form = EditoraForm(request.POST, instance=editora)
            if form.is_valid():
                form.save()
                return redirect('blog:list_editoras')
        else:
            form = EditoraForm(instance=editora)
        return render(request, 'blog/editora_form.html', {'form': form, 'editora': editora})
    
    @login_required
    @permission_required('blog.add_livro')
    def livro_create(request):
        if request.method == 'POST':
            form = LivroForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect ('blog:list_livros')
        else:
            form = LivroForm()
        return render(request, 'blog/livro_form.html', {'form': form})
    
    def list_livros(request):
        from .models import Livro
        from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

        livros = Livro.objects.all().order_by('preco')
        page = request.GET.get('page', 1)
        paginator = Paginator(livros, 5)  # 5 livros por página
        try:
            livros = paginator.page(page)
        except PageNotAnInteger:
            livros = paginator.page(1)
        except EmptyPage:
            livros = paginator.page(paginator.num_pages)
        return render(request, 'blog/livro_list.html', {'livros': livros})
    
    @login_required
    @permission_required('blog.change_livro')
    def livro_edit(request, id):
        from .models import Livro
        livro = get_object_or_404(Livro, pk=id)
        if request.method == 'POST':
            form = LivroForm(request.POST, instance=livro)
            if form.is_valid():
                form.save()
                return redirect('blog:list_livros')
        else:
            form = LivroForm(instance=livro)
        return render(request, 'blog/livro_form.html', {'form': form, 'livro': livro})
    
    def publica_create(request):
        if request.method == 'POST':
            form = PublicaForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect ('blog:list_publicas')
        else:
            form = PublicaForm()
        return render(request, 'blog/publica_form.html', {'form': form})
    
    def list_publicacoes(request):
        from .models import Publica
        publicas = Publica.objects.all()
        return render(request, 'blog/publica_list.html', {'publicas': publicas})
    
    def publica_edit(request, id):
        from .models import Publica
        publica = get_object_or_404(Publica, pk=id)
        if request.method == 'POST':
            form = PublicaForm(request.POST, instance=publica)
            if form.is_valid():
                form.save()
                return redirect('blog:list_publicacoes')
        else:
            form = PublicaForm(instance=publica)
        return render(request, 'blog/publica_form.html', {'form': form, 'publica': publica})

    # Delete views (confirmation + POST to delete)
    
    def autor_delete(request, id):
        from .models import Autor
        autor = get_object_or_404(Autor, pk=id)
        if request.method == 'POST':
            autor.delete()
            return redirect('blog:list_autores')
        return render(request, 'blog/autor_confirm_delete.html', {'autor': autor})

    def editora_delete(request, id):
        from .models import Editora
        editora = get_object_or_404(Editora, pk=id)
        if request.method == 'POST':
            editora.delete()
            return redirect('blog:list_editoras')
        return render(request, 'blog/editora_confirm_delete.html', {'editora': editora})

    @permission_required('blog.delete_livro')
    def livro_delete(request, id):
        from .models import Livro
        livro = get_object_or_404(Livro, pk=id)
        if request.method == 'POST':
            livro.delete()
            return redirect('blog:list_livros')
        return render(request, 'blog/livro_confirm_delete.html', {'livro': livro})

    def publica_delete(request, id):
        from .models import Publica
        publica = get_object_or_404(Publica, pk=id)
        if request.method == 'POST':
            publica.delete()
            return redirect('blog:list_publicacoes')
        return render(request, 'blog/publica_confirm_delete.html', {'publica': publica})
    


    def signup_view(request):
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect('blog:home')
        else:
            form = SignUpForm()
        return render(request, 'blog/sign_up.html', {'form': form})
    

    def signin_view(request):
        if request.method == 'POST':
            form = SignInForm(request=request, data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                next_url = request.POST.get('next') or request.GET.get('next')
                if next_url and url_has_allowed_host_and_scheme(next_url, allowed_hosts={request.get_host()}):
                    return redirect(next_url)
                return redirect('blog:list_autores')
        else:
            form = SignInForm()
        return render(request, 'blog/sign_in.html', {'form': form})

    
    def logout_view(request):
        if request.method != 'POST':
            return HttpResponseNotAllowed(['POST'])
        logout(request)
        return redirect('blog:home')