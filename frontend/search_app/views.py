import requests
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# --- VUES DE RECHERCHE ---

@login_required(login_url='login')  # Seuls les connectés peuvent voir l'index
def index(request):
    return render(request, 'index.html')

@login_required(login_url='login')
def process_query(request):
    if request.method == "POST":
        query = request.POST.get('query')
      
        try:
            # Appel au backend FastAPI sur le port 8000
            response = requests.post(
                "http://127.0.0.1:8000/api/process", 
                json={"query": query},
                timeout=120  
            )
            return JsonResponse(response.json())
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

# --- VUES D'AUTHENTIFICATION ---

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # Connecte l'utilisateur après inscription
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')