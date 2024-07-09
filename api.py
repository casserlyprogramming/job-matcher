import urllib.request, json

def get_data(endpoint):
    with urllib.request.urlopen("https://bn-hiring-challenge.fly.dev/{}.json".format(endpoint)) as url:
        return json.load(url)

def get_members():
    return get_data("members")

def get_jobs():
    return get_data("jobs")
