import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# C'est ici que la magie opère : on importe ton travail
from graph.workflow import Workflow 

app = FastAPI()

# Autoriser la communication entre le Port 5000 et le Port 8000
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_methods=["*"],
    allow_headers=["*"],
)

# On construit l'application LangGraph une seule fois au démarrage
# Exactement comme tu le faisais dans main.py
search_engine = Workflow().build()

class SearchRequest(BaseModel):
    query: str

@app.post("/api/process")
async def process_search(request: SearchRequest):
    try:
        # 1. On reçoit l'input du front (Port 5000)
        user_input = request.query
        
        # 2. On l'envoie à ton moteur (comme le faisait ton main.py)
        result = search_engine.invoke({
            "user_query": user_input
        })
        
        # 3. On extrait le rapport final
        final_report = result.get("final_report", "Erreur : Rapport vide.")
        
        # 4. On le renvoie au front pour l'affichage
        return {"report": final_report}
        
    except Exception as e:
        print(f"Erreur lors de l'exécution : {e}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    # Le serveur écoute sur le port 8000
    uvicorn.run(app, host="0.0.0.0", port=8000)