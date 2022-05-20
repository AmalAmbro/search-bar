from django.shortcuts import render


def index(request):

    words = {
        "abstract" : ["Theoretical","Notional","Intellectual"],
        "competence" : ["Capability","Proficiency","Ability"],
        "bystander " : ["Observer","Watcher","Onlooker"],
        "dash" : ["Shatter","Destroy","Ruin"],
        "stress" : ["Underscore","Accentuate","Point up"],
        "perish" : ["Violent","Destroy","Decay"],
        "definite" : ["Certain","Sure","Accurate"],
        "describe" : ["Portray","Explain","Illustrate"],
        "laugh" : ["Chuckle"],
        "ideal" : ["Good","Model","Visionary"],

    }
    
    if request.method == 'POST':

        word = request.POST.get('word')

        if word :
            word=word.lower()

        synonyms = ""
        if word in words.keys():
            synonyms = words[word]
            context =  {
                "title":"Dictionary | Search",
                "synonyms" : synonyms,
                "synonym_length" : True,
                "subheading":"Synonyms"
            }
                
        else:
            synonyms = "No such word in my dictionary"
            context =  {
                "title":"Dictionary | Search",
                "synonyms" : synonyms,
                "synonym_length" : False,
                "subheading":"Synonyms"
            }
        print("We got a request for the word : ", word)


        return render(request, 'index.html', context=context)

    else:
        context =  {
                "title":"Dictionary | Search",
                "synonyms" : "",
                "synonym_length" : False,
                "subheading":""
            }
        return render(request, 'index.html', context=context)
        

