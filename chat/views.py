from django.shortcuts import render
import sys
import MeCab


def chat_test(request):
    m = MeCab.Tagger("-Ochasen")
    d = {
        'sentence': m.parse(request.GET.get('sentence'))
        # 'sentence': request.GET.get("sentence")
    }
    return render(request, 'chat.html', d)
