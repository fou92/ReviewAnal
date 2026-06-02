from traceback import print_exc
import requests





def get_reviews(url, num_of_reviews=100, batch=10):

    app_id = url_to_id(url)
    api_url = f"https://store.steampowered.com/appreviews/{app_id}"
    params = {
        "json": 1,
        "num_per_page": batch,
        "language": "korean",
        "filter": "recent",
        "purchase_type": "all",
        "cursor": "*",
    }
    review_list = []

    try:
        for _ in range(0,num_of_reviews,batch):
            res = requests.get(api_url, params=params)
            data = res.json()
            reviews = [review["review"] for review in data["reviews"]]
            review_list.extend(reviews)
            params["cursor"] = data["cursor"]
        rest = num_of_reviews%batch
        if rest == 0:
            return review_list
        params["num_per_page"] = rest
        res = requests.get(api_url, params=params)
        data = res.json()
        reviews = [review["review"] for review in data["reviews"]]

        review_list.extend(reviews)
        return review_list
    except Exception as e:
        print_exc()
        return {"error": f"{str(e)} in get_reviews"}


def get_appdetail_data(app_id):
    try:
        api_url = "https://store.steampowered.com/api/appdetails"
        params = {"appids": app_id, "l": "korean"}
        response = requests.get(api_url, params=params)
        data = response.json()
        return data[str(app_id)]["data"]
    except Exception as e:
        print_exc()
        return {"error": f"{str(e)} in get_appdetail_data"}

def url_to_id(url):
    return url.split("app")[-1].split("/")[1]