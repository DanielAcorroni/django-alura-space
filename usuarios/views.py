from django.shortcuts import render, redirect
from usuarios.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User
from django.contrib import auth, messages


def login(request):
    form = LoginForms()

    if request.method == "POST":
        form = LoginForms(request.POST)

        if form.is_valid():
            nome = form["nome_login"].value()
            senha = form["senha"].value()

            usuario = auth.authenticate(request, username=nome, password=senha)

            if usuario is not None:
                auth.login(request, usuario)
                messages.success(
                    request, f"Login de {nome} efetuado com sucesso!"
                )
                return redirect("index")
            else:
                messages.error(request, "Usuário ou senha inexistentes!")
                return redirect("login")

    return render(request, "usuarios/login.html", {"form": form})

# Create your views here.
