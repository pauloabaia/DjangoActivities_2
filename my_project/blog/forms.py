from django import forms
from .models import Autor, Editora, Livro, Publica
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nome']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nome do autor',
            }),
        }


class EditoraForm(forms.ModelForm):
    class Meta:
        model = Editora
        fields = ['nome']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nome da editora',
            }),
        }


class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['ISBN', 'titulo', 'publicacao', 'preco', 'estoque', 'editora']
        widgets = {
            'ISBN': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ISBN (13 caracteres)'
            }),
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Título do livro'
            }),
            'publicacao': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'preco': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
            }),
            'estoque': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '0'
            }),
            'editora': forms.Select(attrs={'class': 'form-control'}),
        }


class PublicaForm(forms.ModelForm):
    class Meta:
        model = Publica
        fields = ['autor', 'livro']
        widgets = {
            'autor': forms.Select(attrs={'class': 'form-control'}),
            'livro': forms.Select(attrs={'class': 'form-control'}),
        }

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True,
    widget=forms.EmailInput(attrs={'placeholder' : 'email@exemplo.com', 'class' : 'input-text'}))

    class Meta:
        model = get_user_model()
        fields = {'username', 'email', 'password2'}

    def clean_email(self):
        email = self.cleaned_data.get('email')
        User = get_user_model()
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError('tem dono pae')
        return email    


class SignInForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Username' , 'class': 'input-text'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Senha' , 'class': 'input-text'}))

