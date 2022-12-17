import datetime

from django.shortcuts import render
import logging

logger = logging.getLogger('django.server')


def error_403(request, *args, **kwargs):
    logger.error(f'{datetime.datetime.now()} -- error 403 -- url: {request.path} -- user: {request.user}')
    return render(request, '403.html')


def error_404(request, *args, **kwargs):
    logger.error(f'{datetime.datetime.now()} -- error 404 -- url: {request.path} -- user: {request.user}')
    return render(request, '404.html')


def error_500(request, *args, **kwargs):
    logger.error(f'{datetime.datetime.now()} -- error 500 -- url: {request.path} -- user: {request.user}')
    return render(request, '500.html')
