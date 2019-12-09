from django.contrib import admin
from .models import Feed, Record, Favor_feed

class FeedAdmin(admin.ModelAdmin):
    list_display = ('fname', 'fitem', 'fmat', 'fnut', 'fusage1', 'fusage2', 'fusage3', 'flegalname')

class RecordAdmin(admin.ModelAdmin):
    list_display = ('pet', 'feed', 'water', 'amount', 'time')

class FavorFeedAdmin(admin.ModelAdmin):
    list_display = ('master', 'feed', 'created_on')

admin.site.register(Feed, FeedAdmin)
admin.site.register(Record, RecordAdmin)
admin.site.register(Favor_feed, FavorFeedAdmin)
