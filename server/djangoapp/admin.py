from django.contrib import admin
from .models import CarMake, CarModel
<<<<<<< HEAD
=======

>>>>>>> 37f0c8d (fix 1 tl)

# Register your models here.



# CarModelInline class
class CarModelInline(admin.StackedInline):
<<<<<<< HEAD
    model = CarModel 
=======
    model = CarModel
    extra = 5
>>>>>>> 37f0c8d (fix 1 tl)

# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    list_display = ['name']

# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
<<<<<<< HEAD
    fields = ['name', 'description']
    inlines = [CarModelInline]

# Register models here
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel)
=======
    inlines = [CarModelInline]
    list_display = ['name']

# Register models here
admin.site.register(CarModel, CarModelAdmin)
admin.site.register(CarMake, CarMakeAdmin)
>>>>>>> 37f0c8d (fix 1 tl)
