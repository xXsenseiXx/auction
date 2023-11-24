from django.contrib import admin

from .models import User, listings, category, bid, comments, watchlist
# Register your models here.

admin.site.register(User)
admin.site.register(listings)
admin.site.register(category)
admin.site.register(bid)
admin.site.register(comments)
admin.site.register(watchlist) 