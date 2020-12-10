# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from .models import Board


# Create your views here.


def Home(request):
    boards = Board.objects.all()  # getting all the boards in the page
    boards_names = list()

    for board in boards:
        boards_names.append(board.name)
    # context= {
    #     'boards':boards,
    # }

    # context={
    #     'boards_names':boards_names,
    # }

    return render(request, 'home.html', {'boards': boards})
