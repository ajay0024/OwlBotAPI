from django.shortcuts import render, redirect, reverse
import requests


# Create your views here.
def index(request, word="cat"):
    return redirect('word/cat')


def search_word(request, word="cat"):
    print(word)
    if request.method == "POST":
        print(request)
    response = requests.get(f"https://owlbot.info/api/v4/dictionary/{word}",
                            headers={'Authorization': 'Token 9baac545bdccb5ff98dcdb55ecec1613987d4150'})
    response_code = response.status_code
    data = response.json()
    context_dict = {"word": word}
    if response_code != 404 and "definitions" in data.keys():
        context_dict["definitions"] = data["definitions"]
    return render(request, 'owlbot/index.html', context=context_dict)
