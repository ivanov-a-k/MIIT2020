from django.contrib import admin
admin.site.site_header = "База данных"
admin.site.site_title = "База данных библиотеки"
admin.site.index_title = "Добро пожаловать в базу данных библиотеки"

from .models import Series, City, Publishing, Room, Shelf, Author, Book, AuthorBook

admin.site.register(Series)
admin.site.register(City)
admin.site.register(Publishing)
admin.site.register(Room)
admin.site.register(Shelf)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(AuthorBook)

