# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Board(models.Model):
    name = models.CharField(max_length=35, unique=True)
    description = models.CharField(max_length=500)

    # def __init__(self):
    #     return self.name


# boardList = Board.objects.all()
# for board in boardList:
#     print(board.name)
#     print(board.description)


class Topic(models.Model):
    subject = models.CharField(max_length=75)
    last_updated = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, related_name='topics', on_delete=models.CASCADE)
    starter = models.ForeignKey(User, related_name='topics', on_delete=models.CASCADE)


class Post(models.Model):
    message = models.TextField(max_length=5000)
    topic = models.ForeignKey(Topic, related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete=models.CASCADE)
