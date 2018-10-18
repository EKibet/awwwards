from django.contrib import admin
from .models import PostedSite,Votes,UsabilityRating,ContentRating,DesignRating
# Register your models here.

admin.site.register(PostedSite)
admin.site.register(ContentRating)
admin.site.register(UsabilityRating)
admin.site.register(DesignRating)
admin.site.register(Votes)
