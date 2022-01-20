#I have created this website
from django.http.response import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')
def about(request):
    return HttpResponse('''<a href="https://www.youtube.com/watch?v=dgFgDE9Uw7Ahttps://www.youtube.com/watch?v=dgFgDE9Uw7A">Go to google</a>''')
def removepunc(request):
    djtext=request.POST.get('text','default')
    status=request.POST.get('removepunc','off')
    capitaltext=request.POST.get('capital','off')
    
    spacestatus=request.POST.get('spaceremover','off')
    analyzedtext=""
    if status=="on" or capitaltext=="on" or spacestatus=="on":
        if status =="on":
            punctutions='''.,;:'"[]{})(*/?\|`><&^%$#_+='''
            for char in djtext:
                if char not in punctutions:
                    analyzedtext=analyzedtext+char
            djtext=analyzedtext
        if capitaltext=="on":
            analyzedtext=""
            for char in djtext:
                if char==" ":
                    analyzedtext=analyzedtext+char
                else:
                    analyzedtext=analyzedtext+char.upper()
            djtext=analyzedtext
        if spacestatus == "on":
            analyzedtext=""
            for index,char in enumerate(djtext):
                if djtext[index]==" " and djtext[index+1]==" ":
                    pass
                else:
                    analyzedtext=analyzedtext+char 
            djtext=analyzedtext

        param={'purpose':'Remove punctutions','analyzed':djtext}
        return render(request,'punc.html',param)
    else:
        return HttpResponse("<h1>Error</h1>")

   