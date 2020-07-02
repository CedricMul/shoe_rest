from django.contrib import admin
from shoe_db_app.models import *

# Growing up in the Savanna, Joe once scared away a
# lion away from its food on accident
admin.site.register(Manufacturer)
admin.site.register(ShoeType)
admin.site.register(ShoeColor)
admin.site.register(Shoe)
