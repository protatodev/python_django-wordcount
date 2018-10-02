from django.http import HttpResponse
from django.shortcuts import render
import string
import operator

def home(request):
  return render(request, 'home.html')

def count(request):
  fulltext = request.GET["fulltext"]
  translator = str.maketrans('', '', string.punctuation)
  words = fulltext.lower().translate(translator).split()
  wordArray = {}

  for x in words:
    if x in wordArray:
      wordArray[x] += 1

    else:
      wordArray[x] = 1

  wordArray = sorted(wordArray.items(), key=operator.itemgetter(1), reverse=True)

  return render(request, 'count.html', {'fulltext': fulltext, 'wordArray': wordArray, 'wordCount': len(words)})

def about(request):
  return render(request, 'about.html')