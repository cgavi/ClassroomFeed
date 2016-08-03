from django.shortcuts import render

def post_list(request):
    return render(request, 'classblog/post_list.html', {})
