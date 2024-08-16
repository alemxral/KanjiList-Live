
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.urls import path
from django.views.generic.detail import DetailView
from backend.models import Kanji
from django.http import HttpResponse
from django.views import View
from backend.html_converter import convert_to_html_table
import sys
import os
import django


# Set up Django environment
sys.path.append('C:/Users/pc/pyprojects/KanjiList')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'KanjiList.settings')
django.setup()

# Views for rendering pages
def home(request):
    return render(request, 'home.html')


def goku(request):
    return render(request, 'goku.html')

def privacy(request):
    return render(request, 'privacy.html')

def FAQ(request):
    return render(request, 'FAQ.html')

def kanjijlptlevel(request):
    return render(request, 'kanji-list-by-jlpt-level.html')

def kanjigradelevel(request):
    return render(request, 'kanji-list-by-grade.html')

def kanjifreqlevel(request):
    return render(request, 'kanji-list-by-freq.html')

def spot(request):
    return render(request, 'spot.html')



class KanjiDetailView(View):

    def get(self, request, *args, **kwargs):
        # Get the 'id' from the URL
        id_request = self.kwargs.get('id')

        if id_request is None:
            return JsonResponse({'error': 'ID not provided'}, status=400)

        # Query the database for the Kanji with the given id
        kanji = get_object_or_404(Kanji, id=id_request)
        table_data = convert_to_html_table(kanji.table_data) 
        print(table_data)

        # Prepare the context with all the required variables
        context = {
            'id': kanji.id,
            'kanji_symbol': kanji.kanji_symbol,
            'kun': kanji.kun,
            'on': kanji.on,
            'meaning': kanji.meaning,
            'table_data': table_data,
        }

        # Render the HTML template with the context
        return render(request, 'base.html', context)
