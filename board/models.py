from os import write
from django.db import models

# Create your models here.

from django.utils import timezone

class Board(models.Model):
    board_title = models.CharField(max_length=50)
    board_writer = models.CharField(max_length=30)
    board_content = models.TextField()
    board_regdate = models.DateTimeField(auto_now=timezone.now)
    board_readcount = models.IntegerField(default=0)

    def __str__(self):
        return '%s. %s(%d)' % (self.board_title, self.board_writer, self.board_readcount)
    def incrementReadCount(self):
        self.board_readcount += 1
        self.save()
