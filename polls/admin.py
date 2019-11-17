from django.contrib import admin
from .models import Countries, Choice #this line added
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class CountryAdmin(admin.ModelAdmin):
    fieldsets = [
            (None,               {'fields': ['country_text']}),
            ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
                ]
    inlines = [ChoiceInline]

admin.site.register(Countries, CountryAdmin)

