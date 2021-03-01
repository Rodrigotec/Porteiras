from django.shortcuts import render, redirect
from  django.contrib import messages


from .forms import cadastrocriar


def home(request):
    return render(request, 'index.html')


def contate(request):
    form = cadastrocriar(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Mensagem enviada com sucesso!')
    return render(request, 'contate-nos.html',{'form':form})


def login(request):
    return render(request, 'login.html')


# def contate(request):
#     return render(request, 'contate-nos.html')


def informatica(request):
    return render(request, 'p_informatica.html')


def galeria(request):
    return render(request, 'galeria.html')
