from django.contrib import admin
from main_app.models import Book, Exercise

admin.site.register(Book)


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    pass
