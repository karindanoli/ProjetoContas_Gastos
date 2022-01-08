from django.shortcuts import render

from django.http import HttpResponse
import datetime

def home(request):
    data = {}
    data['transacoes'] = ['t1', 't2', 't3']

    data ['now'] = datetime.datetime.now()
    #variavel python dentro do template html

   # html = "<html><body>It is now %s.</body></html>" % now
    return render(request,'contas/home.html', data)

#data é um dicionario que ira repassar as infos para o html
#django jinja que faz a implementação no html o python
