#!C:\Users\Hossein\AppData\Local\Programs\Python\Python38\Python.exe
class TemplateEngine:
    def Engine(self,file,dictionary):
        data = open(file,"r")
        html = data.read()
        for key in dictionary:
            html = html.replace("{"+key+"}",dictionary[key])
        return html


