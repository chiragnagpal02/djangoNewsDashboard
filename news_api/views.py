from django.shortcuts import render
import requests
API_KEY = '1ec33832bb424bee9d5f39dd9aba6204'

# Create your views here.
def main(request):
    url = f'https://newsapi.org/v2/top-headlines?country=in&apiKey={API_KEY}'
    response = requests.get(url)
    data = response.json() 
    articles = data['articles']

    context = {
        'articles': articles
    }

    return render(request, "news_api/main.html", context)