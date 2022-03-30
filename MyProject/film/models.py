from django.db import models

class FilmMain(models.Model):
    genre = models.CharField(max_length=16)

class FilmDetail(models.Model):
    FILM_COUNTRY = [
        ("USA", "United States"),
        ("UK", "United Kingdom"),
        ("DE", "Germany"),
    ]
    country = models.CharField(max_length=3, choices=FILM_COUNTRY, default='country')
    premiere = models.DateField()
    # time = models.CharField(max_length=10)
    director = models.CharField(max_length=32, default='director')
    title = models.CharField(max_length=32, default='title')


class FilmDate(models.Model):
    DAY_OF_THE_WEEK = [
        ("Monday", "Monday"),
        ("Tuesday", "Tuesday"),
        ("Wednesday", "Wednesday"),
        ("Thursday", "Thursday"),
        ("Friday", "Friday"),
        ("Saturday", "Saturday"),
        ("Sunday", "Sunday"),
            ]
    day = models.CharField(max_length=15, choices=DAY_OF_THE_WEEK, default='day')

    SEANS_HOUR = [
        ("10", "10"),
        ("18", "18"),
            ]
    hour = models.CharField(max_length=15, choices=SEANS_HOUR, default='hour')


class Film(models.Model):
    main = models.ForeignKey(FilmMain, on_delete=models.CASCADE)
    detail = models.OneToOneField(FilmDetail, on_delete=models.PROTECT)
    date = models.OneToOneField(FilmDate, on_delete=models.PROTECT)

    def delete(self):
        super(Film, self).delete()
        self.detail.delete()
        self.date.delete()


    def __str__(self):
        return f"{self.main.genre} "

        # return f"{self.detail.title} "





# Create your models here.
