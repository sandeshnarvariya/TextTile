# I have created this file - Sandesh
from django.http import HttpResponse
from django.shortcuts import render


def index(request):  # request argument is complesory
    return render(request, 'index.html') 




def analyze(request):
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')



    if removepunc == "on":
     ## Remove Panctuation charctor programe
        punctuations = '''`~!@#$%^&*()-+={}[]"';:/?.>,<''' 
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {
            "purpose":"removed Punctuation",
            "analyzed_text": analyzed 
        }
        return render(request, 'analyze.html', params)

    elif(fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        
        params = {
            "purpose":"Changed to Uppercase",
            "analyzed_text": analyzed 
        }
        #Analyze the taxt
        return render(request, 'analyze.html', params)
    
    elif(extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index]== " " and djtext[index+1]==" "):
                analyzed = analyzed + char
        
        params = {
            "purpose":"Remove Extra Space",
            "analyzed_text": analyzed 
        }
        #Analyze the taxt
        return render(request, 'analyze.html', params)

    elif(newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n":
                analyzed = analyzed + char
        
        params = {
            "purpose":"Remove New Line",
            "analyzed_text": analyzed 
        }
        #Analyze the taxt
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse("Error")
    ## end program
