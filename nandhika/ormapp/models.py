from django.db import models
from django.contrib import admin
class Book_Details(models.Model):
  chapters_name=models.CharField(max_length=50);
  book_name=models.CharField(max_length=25);
  author=models.CharField(max_length=30);
  pages=models.IntegerField();
  year=models.IntegerField();
  Book_serial_no=models.IntegerField(primary_key=True)
class Book_DetailsAdmin(admin.ModelAdmin):
  list_display=("chapters_name","book_name","author","pages","year","Book_serial_no");


