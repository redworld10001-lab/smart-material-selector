from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="Smart Material Selector", version="0.1.0")


@app.get("/health")
def health_check():
    return {"status": "ok", "service": "smart-material-selector"}


class SelectRequest(BaseModel):
    # مثال بسيط: المستخدم يرسل أسماء مواد + اختيار اختياري "هدف"
    materials: List[str]
    goal: Optional[str] = None


@app.post("/select")
def select_material(payload: SelectRequest):
    # مؤقتًا: نرجّع أول مادة كـ “أفضل اختيار”
    chosen = payload.materials[0] if payload.materials else None
    return {
        "chosen_material": chosen,
        "goal": payload.goal,
        "note": "Demo selector (temporary). Next step: replace with real scoring logic."
    }
