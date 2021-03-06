from django.contrib import admin
from django.contrib import messages
from django.utils.timezone import now
from django.db.models import F

# Register your models here.
from .models import FAQ, Images, Files, Feedback, ReplyImages, ReplyFiles

class ImagesInline(admin.StackedInline):
    model = Images
    extra = 1


class FilesInline(admin.StackedInline):
    model = Files
    extra = 1


class FAQAdmin(admin.ModelAdmin):
    inlines = [ImagesInline, FilesInline]
    exclude = ['author', 'clicks']
    list_display = ('question_text', 'answer_text', 'author', 'topped', 'clicks')
    ordering = [F('topped').asc(nulls_last=True), '-clicks']

    def delete_queryset(self, request, queryset):
        for obj in queryset:
            if obj.author == request.user:
                obj.delete()
            elif request.user.is_superuser:
                obj.delete()
                messages.success(request, "You are SUPERUSER nothing can stop you.")
            else:
                messages.set_level(request, messages.ERROR)
                messages.error(request, obj.question_text + " created by " + obj.author.get_username() + ". Only the author can edit or delete it.")

    def save_model(self, request, obj, form, change):
        if obj.author is None or obj.author == request.user:
            obj.author = request.user
            super().save_model(request, obj, form, change)
        elif request.user.is_superuser:
            obj.author = request.user
            super().save_model(request, obj, form, change)
            messages.success(request, "You are SUPERUSER nothing can stop you.")
        else:
            messages.set_level(request, messages.ERROR)
            messages.error(request, obj.question_text + " created by " + obj.author.get_username() + ". Only the author can edit or delete it.")

    def delete_model(self, request, obj):
        if obj.author == request.user:
            super().delete_model(request, obj)
        elif request.user.is_superuser:
            super().delete_model(request, obj)
            messages.success(request, "You are SUPERUSER nothing can stop you.")
        else:
            messages.set_level(request, messages.ERROR)
            messages.error(request, obj.question_text + " created by " + obj.author.get_username() + ". Only the author can edit or delete it.")


class ReplyImagesInline(admin.StackedInline):
    model = ReplyImages
    extra = 1


class ReplyFilesInline(admin.StackedInline):
    model = ReplyFiles
    extra = 1


class FeedbackAdmin(admin.ModelAdmin):
    inlines = [ReplyImagesInline, ReplyFilesInline]
    list_display = ('feedback', 'feedback_date', 'reply_date', 'author')
    readonly_fields = ['author', 'feedback']
    ordering = ['reply_date', 'feedback_date']

    def save_model(self, request, obj, form, change):
        obj.reply_date = now()
        super().save_model(request, obj, form, change)

admin.site.register(FAQ, FAQAdmin)
admin.site.register(Feedback, FeedbackAdmin)
