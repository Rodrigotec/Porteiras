from django.shortcuts import render, redirect


from .forms import cadastrocriar


def home(request):
    return render(request, 'index.html')


def contate(request):
    form = cadastrocriar(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(home)
    return render(request, 'contate-nos.html',{'form':form})


def login(request):
    return render(request, 'login.html')


# def contate(request):
#     return render(request, 'contate-nos.html')


def informatica(request):
    return render(request, 'p_informatica.html')


def galeria(request):
    return render(request, 'galeria.html')
