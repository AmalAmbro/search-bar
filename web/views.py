from django.shortcuts import render

from dictionary.models import WordMeaning, Words


def index(request):
    if request.method == 'POST':
        search_word = request.POST.get('word').lower()
        
        word = Words.objects.filter(word = search_word)

        if word:
            data = WordMeaning.objects.filter(word__in=word).order_by('priority')
            
            context = {
                "title":"Search",
                "datas":data,
                "word" : search_word,
            }
                
            return render(request, 'index.html', context=context)
        elif search_word == '':
            data = "Thats an empty string please insert a proper word"
            context = {
                "title":"Search",
                "missing":True,
                "datas":data,
            }
                
            return render(request, 'index.html', context=context)
        else:
            data = f"'{search_word}' is not present in my dictionary, Please add it using the following link!!!"
            context = {
                "title":"Search",
                "missing":True,
                "datas":data,
            }
                
            return render(request, 'index.html', context=context)
    else:
        context = {
            "title":"Search",
        }
        
        return render(request, 'index.html', context=context)

def add(request):
    if request.method == "POST":
        word = request.POST.get('newWords').lower()
        meaning = request.POST.get('addMeanings').lower()
        priority = request.POST.get('priority')

        new_word, created = Words.objects.get_or_create(
            word = word
        )
        print(new_word, created)

        WordMeaning.objects.create(
            word = new_word,
            meaning = meaning,
            priority = priority
        )
        context = {
            "title":"Add New"
        }
        return render(request, 'dict.html', context=context)

    else:
        context = {
            "title":"Add New"
        }
        return render(request, 'dict.html', context=context)
