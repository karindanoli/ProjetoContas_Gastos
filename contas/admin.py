from django.contrib import admin

# Register your models here.
from contas.models import Categoria

admin.site.register(Categoria)
#vai fazer a tabela no site e vai persistir os dados no bd. Estilo JPA
