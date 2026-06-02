from services.similarity import analyze_need
from services.steam_api import get_reviews, get_appdetail_data, url_to_id
from api.cache import save_reviews


def similarity_analyze(url, need):
    try:
        reviews = get_reviews(url)
        app_id = url_to_id(url)
        save_reviews(app_id,reviews)

        if len(reviews) == 0:
            return {"score": 0}

        scores = analyze_need(need, reviews)
        descending_sorted = sorted(scores, reverse=True)
        cut = int(len(descending_sorted)*0.2)
        top_20_percent = descending_sorted[:cut]


        top_mean = mean(top_20_percent)
        rest_mean = mean(descending_sorted[cut:])

        score = top_mean*0.6+rest_mean*0.4


        appdetail = get_appdetail_data(int(app_id))
        title = appdetail["name"]
        imgurl = appdetail["header_image"]

        return {"score": score, "title": title, "imgurl": imgurl}
    except Exception as e:
        return {"error": f"{str(e)} in similarity_analyze"}

def mean(lst):
    return float(sum(lst))/len(lst)