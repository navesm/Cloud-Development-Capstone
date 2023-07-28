from django.contrib import admin
from .models import CarMake, CarModel


# Register your models here.

# CarModelInline class
class CarModelInline(admin.StackedInline):
    model = CarModel

# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'car_make', 'car_type', 'year', 'dealer_id']
    search_fields = ['name', 'car_make__name', 'car_type', 'year', 'dealer_id']
    list_filter = ['car_type', 'year']
    list_select_related = ['car_make']

# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name', 'description']
    inlines = [CarModelInline]


# Register models here
admin.site.register(CarModel, CarModelAdmin)
admin.site.register(CarMake, CarMakeAdmin)