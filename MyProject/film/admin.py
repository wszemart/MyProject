from django.contrib import admin
from .models import Film, FilmDetail, FilmMain, FilmDate


# Register your models here.
class FilmAdmin(admin.ModelAdmin):
    model = Film
    list_display = ['get_detail_title', 'get_main_genre', 'get_date_day']

    def get_detail_title(self, obj):
        return obj.detail.title

    def get_main_genre(self, obj):
        return obj.main.genre

    def get_date_day(self, obj):
        return obj.date.day

    get_detail_title.admin_order_field = "title"
    get_detail_title.short_description = "Title"

    get_main_genre.admin_order_field = "genre"
    get_main_genre.short_description = "Genre"

    get_date_day.admin_order_field = "day"
    get_date_day.short_description = "Day"


admin.site.register(Film, FilmAdmin)
admin.site.register(FilmDetail)
admin.site.register(FilmMain)
admin.site.register(FilmDate)


