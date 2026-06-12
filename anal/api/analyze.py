from services.similarity import analyze_need
from services.steam_api import get_reviews, get_appdetail_data, url_to_id
from api.cache import save_reviews


def similarity_analyze(url, need, prefs):
    try:
        reviews = get_reviews(url)
        app_id = url_to_id(url)
        # save_reviews(app_id,reviews)

        pref_percent = {}
        for key,val in prefs.items():
            if val >= 0:
                pref_percent[key] = val/5

        if len(reviews) == 0:
            return {"score": 0}

        if bool(need.strip()):
            scores = analyze_need(need, reviews)
            score = calculate_score(scores)
        else:
            score = None

        pref_need = {"story":"스토리가 좋은 게임",
                     "difficulty": "도전적인 난이도의 게임",
                     "action": "전투와 액션이 재미있는 게임",
                     "strategy": "전략이 중요한 게임",
                     "free": "자유도가 높은 게임",
                     "calm": "힐링이 되는 게임"
                     }

        pref_score = {}
        for key in pref_percent.keys():
            sim = calculate_score(analyze_need(pref_need[key], reviews))
            weight = pref_percent[key]
            category_score = sim*(0.5+weight/2)
            pref_score[key] = category_score


        appdetail = get_appdetail_data(int(app_id))
        title = appdetail["name"]
        imgurl = appdetail["header_image"]

        return {"score": score, "title": title, "imgurl": imgurl, "pref": pref_score}
    except Exception as e:
        return {"error": f"{str(e)} in similarity_analyze"}

def mean(lst):
    return float(sum(lst))/len(lst)

def calculate_score(lst):
    descending_sorted = sorted(lst, reverse=True)
    cut = int(len(descending_sorted) * 0.2)
    top_20_percent = descending_sorted[:cut]

    top_mean = mean(top_20_percent)
    rest_mean = mean(descending_sorted[cut:])

    score = top_mean * 0.6 + rest_mean * 0.4
    return score