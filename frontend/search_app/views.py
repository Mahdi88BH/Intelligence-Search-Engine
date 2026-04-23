import requests
from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    return render(request, 'index.html')

def process_query(request):
    if request.method == "POST":
        query = request.POST.get('query')
        
        # On appelle le backend FastAPI sur le port 8000
        try:
            response = requests.post(
                "http://127.0.0.1:8000/api/process", 
                json={"query": query},
                timeout=120  # L'IA prend du temps à chercher
            )
            return JsonResponse(response.json())
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)