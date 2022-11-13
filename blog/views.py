from django.shortcuts import render


def blog_main(request):
    return render(request, 'blog/blog_main.html')
