from django.shortcuts import render, redirect
from contas.models import Transacao

from django.http import HttpResponse
import datetime
from .form import TransacaoForm


def home(request):
    data = {}
    data['transacoes'] = ['t1', 't2', 't3']

    data['now'] = datetime.datetime.now()
    # variavel python dentro do template html

    # html = "<html><body>It is now %s.</body></html>" % now
    return render(request, 'contas/home.html', data)


# data é um dicionario que ira repassar as infos para o html
# django jinja que faz a implementação no html o python

def listagem(request):
    data = {}
    data['transacoes'] = Transacao.objects.all()
    # Objects é um manager é uma classe de model e traz operações de banco de dados como o all para buscar tudo no BD, FILTER PARA FILTRAR ALGO, last para pegar a ultima transacao do bd, first para pegar a primeira transacao do bd,
    return render(request, 'contas/listagem.html', data)


def nova_transacao(request):
    form = TransacaoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_listagem')
    # voce pode dar nomes aos recursos em url.py. Aqui voce redireciona, pois tem o botão de post e ele retorna na listagem para a pagina de post.

    data = {}
    data['form'] = form
    return render(request, 'contas/form.html', data)


# render está chamando pra tela

def update(request, pk):
    data = {}
    transacao = Transacao.objects.get(pk=pk)
    # filter retorna mais de um objeto e o get retorna um objeto
    form = TransacaoForm(request.POST or None, instance=transacao)

    if form.is_valid():
        form.save()
        return redirect('url_listagem')
    # voce pode dar nomes aos recursos em url.py. Aqui voce redireciona, pois tem o botão de post e ele retorna na listagem para a pagina de post.

    data['form'] = form
    return render(request, 'contas/form.html', data)
# render está chamando pra tela
