def not_found(TemplateEngine,Id=None):
    dictionary = {"Error": "404",
                  "Error_message": "Page not found:("}
    result = TemplateEngine.Engine(TemplateEngine,"Views/error.html", dictionary)
    return result

def method_not_allowed(TemplateEngine,Id=None):
    dictionary = {"Error": "405",
                  "Error_message": "Requested method not allowed:("}
    result = TemplateEngine.Engine(TemplateEngine,"Views/error.html", dictionary)
    return result