from django.http import HttpResponse
from django.shortcuts import render
import operator
def home(request):
#    return HttpResponse('hello')
#    return render(request,'home.html',{'hithere': 'This is me'})
    return render(request,'home.html')
def About(request):
    return render(request,'About.html')
def count(request):
    fulltext=request.GET['fulltext']
    word_list=fulltext.split()
    word_dictionary = {}
    
    for word in word_list:
        if word in word_dictionary:
            word_dictionary[word]+=1
        else:
            word_dictionary[word]=1
    sorted_words=sorted(word_dictionary.items(),key=operator.itemgetter(1), reverse=True)       
        
#    print(fulltext)
    return render(request,'count.html',{'fulltext':fulltext,'count':len(word_list),'sorted_words':sorted_words})

#def eggs(request):
#    return HttpResponse('<h1>Eggs are great</h1>')

