from django.contrib import admin

# Register your models here.
from .models import FAQ, Images, Files

class ImagesInline(admin.StackedInline):
    model = Images
    extra = 1


class FilesInline(admin.StackedInline):
    model = Files
    extra = 1


class FAQAdmin(admin.ModelAdmin):
    inlines = [ImagesInline, FilesInline]


admin.site.register(FAQ, FAQAdmin)
