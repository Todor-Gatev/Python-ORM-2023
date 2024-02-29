import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Shoe

print(Shoe.objects.values_list("brand", flat=True).distinct())  # <QuerySet ['nike', 'addidas']>
# print(Shoe.objects.values_list("brand", flat=True))  # <QuerySet ['nike', 'addidas', 'nike']>
# print(Shoe.objects.values_list("brand"))  # <QuerySet [('nike',), ('addidas',), ('nike',)]>
# print(Shoe.objects.values_list("brand", flat=True).distinct().count())  # 2

# Create queries within functions
