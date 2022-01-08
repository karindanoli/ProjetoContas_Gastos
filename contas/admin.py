from django.contrib import admin

# Register your models here.
from contas.models import Categoria, Transacao

admin.site.register(Categoria)
#vai fazer a tabela no site e vai persistir os dados no bd. Estilo JPA
admin.site.register(Transacao)
