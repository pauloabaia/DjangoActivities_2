from django.core.management.base import BaseCommand
from faker import Faker
from random import randint, uniform
from blog.models import Livro, Editora

class Command(BaseCommand):
    help = 'Comando para gerar vários registros de livros'

    def add_arguments(self, parser):
        parser.add_argument('--count', type=int, default=100, help='Número de livros a criar')

    def handle(self, *args, **options):
        count = options.get('count') or 100
        fake = Faker('pt_BR')

        editoras = list(Editora.objects.all())  # usa apenas as editoras existentes

        created = 0
        for _ in range(count):
            Livro.objects.create(
                ISBN=fake.isbn13(separator=""),
                titulo=fake.sentence(nb_words=4),
                publicacao=fake.date_between(start_date='-10y', end_date='today'),
                preco=round(uniform(10, 300), 2),
                estoque=randint(0, 100),
                editora=fake.random_element(editoras),
            )
            created += 1

        self.stdout.write(self.style.SUCCESS(f'Criados {created} livros.'))
