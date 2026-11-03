from django import forms

class loginForms(forms.Form):
    
    nome_login = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "ex: João Silva"}),
    min_length=3,
    max_length=100, 
    label='Nome de login', 
    required=True)
   
    senha = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "digite sua senha"}), 
    label='Senha', 
    required=True)


class cadastroForms(forms.Form):
    
    nome_cadastro = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "ex: João Silva"}),
    min_length=3,
    max_length=100,
    label='Nome de login',
    required=True)

    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "ex: joao@gmail.com"}),
    min_length=3,
    max_length=100,
    label='Email',
    required=True)

    senha = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "digite sua senha"}),
    label='Senha',
    required=True)

    confirmacao_senha = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "confirme sua senha"}),
    label='Confirmação de Senha',
    required=True)


