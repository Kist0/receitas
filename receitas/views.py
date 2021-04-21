from django.shortcuts import render

def index(request):

    receitas = {
        1:'Lasanha',
        2:'Bolo de cenoura',
        3:'Sorvete'
    }

    dados = {
        'nome_das_receitas' : receitas
    }

    return render(request, 'index.html', dados)

def receita(request):
    return render(request, 'receita.html')