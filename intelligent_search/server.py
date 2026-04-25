import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from core.container import Container
from graph.workflow import Workflow

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

<<<<<<< HEAD
# On construit l'application LangGraph une seule fois au démarrage
search_engine = Workflow().build()
=======
# ✅ Correct initialization
container = Container()
search_engine = Workflow(container).build()

>>>>>>> 83d3c4e7083e566ae1954be9725b7a8b591966dc

class SearchRequest(BaseModel):
    query: str


@app.post("/api/process")
async def process_search(request: SearchRequest):
    try:
        result = search_engine.invoke({
            "user_query": request.query
        })

        final_report = result.get("final_report", "Erreur : Rapport vide.")

        return {"report": final_report}

    except Exception as e:
        print(f"Erreur lors de l'exécution : {e}")
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)