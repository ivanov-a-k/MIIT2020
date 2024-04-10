from django.db import models

class Series(models.Model):
    title_series = models.CharField(max_length=255)
    note = models.TextField(default='', blank=True)

    def __str__(self):
        return f"{self.title_series}"

    class Meta:
        verbose_name = "Серия книг"
        verbose_name_plural = "Серии книг"

class City(models.Model):
    city = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.city}"

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"

class Publishing(models.Model):
    id_city = models.ForeignKey(City, on_delete=models.CASCADE)
    publishining_office = models.CharField(max_length=255)
    note = models.TextField(default='', blank=True)

    def __str__(self):
        return f"{self.publishining_office}"

    class Meta:
        verbose_name = "Издатель"
        verbose_name_plural = "Издатели"
class Room(models.Model):
    room_name = models.CharField(max_length=255)
    note = models.TextField(default='', blank=True)

    def __str__(self):
        return f"{self.room_name}"

    class Meta:
        verbose_name = "Комната"
        verbose_name_plural = "Комнаты"

class Shelf(models.Model):
    id_room = models.ForeignKey(Room, on_delete=models.CASCADE)
    number_shelf = models.PositiveSmallIntegerField()
    note = models.TextField(default='', blank=True)

    def __str__(self):
        return f"№{self.number_shelf} {self.id_room}"

    class Meta:
        verbose_name = "Полка"
        verbose_name_plural = "Полки"

class Author(models.Model):
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, default='', blank=True)
    last_name = models.CharField(max_length=255)
    birth_date = models.DateField()
    death_date = models.DateField(default='', blank=True)
    note = models.TextField(default='', blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"

class Book(models.Model):
    title_book = models.CharField(max_length=255)
    year_of_publishing = models.PositiveSmallIntegerField()
    edition = models.PositiveSmallIntegerField()
    isbn = models.CharField(max_length=17)
    number_of_copies = models.PositiveSmallIntegerField()
    volume = models.PositiveSmallIntegerField()
    id_publishing = models.ForeignKey(Publishing, on_delete=models.CASCADE)
    id_shelf = models.ForeignKey(Shelf, on_delete=models.CASCADE)
    id_series = models.ForeignKey(Series, on_delete=models.CASCADE)
    id_author = models.ForeignKey(Author, on_delete=models.CASCADE)
    note = models.TextField(default='', blank=True)

    def __str__(self):
        return f"{self.id_author}, \"{self.title_book}\", {self.id_publishing} Изд. {self.edition}, {self.year_of_publishing} г. - {self.volume} стр."

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

class AuthorBook(models.Model):
    id_author = models.ForeignKey(Author, on_delete=models.CASCADE)
    id_book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id_book}"

    class Meta:
        verbose_name = "Автор-книга"
        verbose_name_plural = "Авторы-книги"