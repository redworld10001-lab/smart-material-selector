@app.post("/select")
def select_material(payload: SelectRequest):
    scores = {
        "lightweight": {"Steel": 3, "Aluminum": 8, "Carbon Fiber": 10},
        "strong": {"Steel": 9, "Aluminum": 6, "Carbon Fiber": 8},
        "low_cost": {"Steel": 10, "Aluminum": 6, "Carbon Fiber": 2},
    }

    goal = (payload.goal or "lightweight").strip().lower()
    goal_scores = scores.get(goal, {})

    best_material = None
    best_score = -1

    for m in payload.materials:
        s = goal_scores.get(m, 0)
        if s > best_score:
            best_material = m
            best_score = s

    return {
        "chosen_material": best_material,
        "score": best_score,
        "goal": goal,
        "materials": payload.materials,
        "note": "Demo scoring. Next: use a real materials dataset."
    }
