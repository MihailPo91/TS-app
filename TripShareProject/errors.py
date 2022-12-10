from django.shortcuts import render


def error_403(request, *args, **kwargs):
    return render(request, '403.html')


def error_404(request, *args, **kwargs):
    return render(request, '404.html')


def error_500(request, *args, **kwargs):
    return render(request, '500.html')
