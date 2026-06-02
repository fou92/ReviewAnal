from dotenv import load_dotenv
from openai import OpenAI
from services.steam_api import get_reviews

import os

load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=OPENAI_API_KEY)


def response_gpt(need, reviews):
    MODEL = "gpt-5.4-nano"

    review_prompt = ""
    for review in reviews:
        review_prompt += review+"\n"

    prompt = need+"\n\n"+review_prompt

    response = client.responses.create(
        model=MODEL,
        instructions="당신은 이 게임이 취향에 맞을지 고민하는 사용자에게 결정을 할 수 있도록 도와주는 입장이다."
                    "당신은 사용자에게서 리뷰 목록 그리고 사용자가 원하는 취향이 써져있는 텍스트로 두가지를 파라미터로 받을 것이다"
                    "사용자의 취향을 고려해서 추천할만한 이유 1-2줄 분량, 해당 게임의 강점을 #태그 형식으로 5개 정도 제시,"
                    "주의할 점으로 사용자가 안 좋아할만한 요소 1-2줄 분량으로 일러두기 그리고 리뷰를 종합하여 3줄 내외의 총평을 내리면 된다"
                     "답변은 다음과 같은 형식으로 대답하면 된다.\n\n\n"
                     "추천 이유:\n"
                     "당신이 대답해야하는 추천할만한 이유(1줄-2줄)\n"
                     "좋은 평가:\n"
                     "#당신이 #제시할 #5가지 #정도의 #태그(5가지 정도)\n"
                     "주의할 점:\n"
                     "당신이 일러둬야할 단점(1줄-2줄)\n\n"
                     "당신이 내려야할 총평(3줄 내외)",
        input=prompt
    )

    return {"desc":response.output_text}
