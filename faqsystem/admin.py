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
    exclude = ['author']
    list_display = ('question_text', 'answer_text', 'author')

    def delete_queryset(self, request, queryset):
        for obj in queryset:
            if obj.author == request.user:
                obj.delete()

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)

    def delete_model(self, request, obj):
        if obj.author == request.user:
            super().delete_model(request, obj)


admin.site.register(FAQ, FAQAdmin)
