from django.shortcuts import render, redirect
from usuarios.forms import loginForms, cadastroForms
from django.contrib.auth.models import User

def login(request):
    forms = loginForms()
    return render(request, 'usuarios/login.html', {"form": forms})


def cadastro(request):
    forms = cadastroForms()

    if request.method == 'POST':
        forms = cadastroForms(request.POST)
        if forms.is_valid():
            if forms["confirmacao_senha"].value() != forms["senha"].value() :
                return redirect('cadastro')
        
            nome=forms["nome_cadastro"].value()
            email=forms["email"].value()
            senha=forms["senha"].value()

            usuario = User.objects.filter(username=nome).exists()
            if usuario:
                return redirect('cadastro')
            usuario = User.objects.create_user(username=nome, email=email, password=senha)
            usuario.save()
        return redirect('login')

    return render(request, 'usuarios/cadastro.html', {"form": forms})