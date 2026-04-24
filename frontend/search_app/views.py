import requests
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import SearchHistory  # Import du modèle pour l'historique

# --- VUES DE RECHERCHE ---

@login_required(login_url='login')
def index(request):
    # On récupère tout l'historique de l'utilisateur connecté
    history = SearchHistory.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'index.html', {'history': history})

@login_required(login_url='login')
def process_query(request):
    if request.method == "POST":
        query = request.POST.get('query')
      
        try:
            # 1. Appel au backend FastAPI (Port 8000)
            response = requests.post(
                "http://127.0.0.1:8000/api/process", 
                json={"query": query},
                timeout=120  
            )
            data = response.json()

            if "report" in data:
                # 2. Sauvegarde automatique dans la base de données Django
                history_entry = SearchHistory.objects.create(
                    user=request.user,
                    query=query,
                    report=data["report"]
                )
                
                # On renvoie le rapport ET l'ID de la sauvegarde pour mettre à jour la sidebar en JS
                return JsonResponse({
                    "report": data["report"], 
                    "id": history_entry.id,
                    "query": query
                })
            
            return JsonResponse(data)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

@login_required(login_url='login')
def get_history_detail(request, history_id):
    """Récupère un ancien rapport sans solliciter le backend FastAPI"""
    item = get_object_or_404(SearchHistory, id=history_id, user=request.user)
    return JsonResponse({
        "query": item.query,
        "report": item.report,
        "date": item.created_at.strftime("%d/%m/%Y %H:%M")
    })

# --- VUES D'AUTHENTIFICATION ---

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
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
@login_required(login_url='login')

def delete_history(request, history_id):
    if request.method == "POST":
        # On s'assure que l'entrée appartient bien à l'utilisateur connecté
        item = get_object_or_404(SearchHistory, id=history_id, user=request.user)
        item.delete()
        return JsonResponse({"status": "success"})
    return JsonResponse({"error": "Invalid request"}, status=400)
def logout_view(request):
    logout(request)
    return redirect('login')