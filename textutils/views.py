# from string import whitespace
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    djtext =  (request.POST.get('text','default'))
    removepunc =  (request.POST.get('removepunc','off'))
    fullcaps =  (request.POST.get('fullcaps','off'))
    whitespace =  (request.POST.get('whitespace','off'))
    num = request.POST.get('num','off')
    alph = request.POST.get('alph','off')
    # analyzed = djtext

    
    if removepunc == "on":
        punctuations = '''!()-[]}{;:'"\,<>./?@#$%^&*_~'''
        analyzed =""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params={
        'analyzed_text':analyzed,
        }   
        djtext=analyzed
        # return render(request, 'analyze.html', params)
   


    if fullcaps == "on":
        analyzed=""
        analyzed = djtext.upper()
        params={
        'analyzed_text':analyzed
        }
        djtext=analyzed
        # return render(request, 'analyze.html', params)
    


    if whitespace == "on":
        analyzed=""
        whitespace = " "
        for char in djtext:
            if char not in whitespace:
                analyzed = analyzed + char
        params={
         'analyzed_text':analyzed
        }
        djtext=analyzed
        # return render(request, 'analyze.html', params)



    if num == "on":
        analyzed=""
        for char in djtext:
            if not char.isdigit():
                analyzed = analyzed + char
        params={
         'analyzed_text':analyzed
        }
        djtext=analyzed
        # return render(request, 'analyze.html', params)


    if alph == "on":
        analyzed=""
        for char in djtext:
            if not char.isalpha():
                analyzed = analyzed + char
        params={
         'analyzed_text':analyzed
        }
        djtext=analyzed
        # return render(request, 'analyze.html', params)


    if whitespace=="off" and fullcaps== "off" and removepunc =="off" and num == "off"  and alph=="off":
        return error(request)
    

    
    if (request.POST.get('text','default')) in "  ":
        return error(request)

    return render(request, 'analyze.html', params)

def error(request):
    return render(request, 'error.html')