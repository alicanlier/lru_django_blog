from django.contrib import admin
from bookmark.models import Bookmark 

# Register your models here.
# 관리자가 관리할 DB로 등록
@admin.register(Bookmark) #decorator of python (like annotation of java): registering to admin site
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('id','title','url')

#Instead of @admin.register(Bookmark) decoration, you can do the following:
#admin.site.register(Bookmark,BookmarkAdmin)