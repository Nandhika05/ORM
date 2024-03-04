# Ex02 Django ORM Web Application
## Date: 28/02/2024

## AIM
To develop a Django application to store and retrieve data from a Book database using Object Relational Mapping(ORM).

## Entity Relationship Diagram

![alt text](<Screenshot 2024-03-04 143208.png>)
Include your ER diagram here

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
model.py

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

admin.py

from django.contrib import admin
from .models import Book_Details,Book_DetailsAdmin
admin.site.register(Book_Details,Book_DetailsAdmin)

```
## OUTPUT


![OUTPUT](<Screenshot 2024-02-28 042201.png>)


## RESULT
Thus the program for creating a database using ORM hass been executed successfully
