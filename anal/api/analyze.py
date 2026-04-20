from fastapi import APIRouter
from services.steam_api import get_reviews
from services.similarity import analyze_need
# from services.similarity impo


router = APIRouter()

@router.post("/analyze")
def analyze(data: dict):
    user_need=data["need"]
    game_id = data["game_id"]

    score = analyze_need(user_need, game_id)

    return {"need_match_score":score}