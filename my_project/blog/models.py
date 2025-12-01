from django.db import models

# Create your models here.

class Autor(models.Model):
    id = models.AutoField(primary_key=True) 
    nome = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"

class Editora(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Editora"
        verbose_name_plural = "Editoras"

class Livro(models.Model):
    id = models.AutoField(primary_key=True)
    ISBN = models.CharField(max_length=13, unique=True)
    titulo = models.CharField(max_length=200)
    publicacao = models.DateField()
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    estoque = models.IntegerField()
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name = "Livro"
        verbose_name_plural = "Livros"

class Publica(models.Model):
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.autor.nome} - {self.livro.titulo}"
    
    class Meta:
        verbose_name = "Publicação"
        verbose_name_plural = "Publicações"
        unique_together = ('autor', 'livro')
        
