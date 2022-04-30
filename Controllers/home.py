def index(Config,Id=None):
    dictionary = {"title": "rotic",
                  "lable_name": "name:"}
    result = Config['engine'].Engine(Config['engine'],"Views/home.html", dictionary)
    return result