from django.contrib import admin
from accounts.models import UserProfile

# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_infos', 'city', 'phone', 'website')
    list_filter = ('phone', 'city',)
    fields = ('user', 'description')

    def user_infos(self, descr):
        return descr.description

    def get_queryset(self, request):
        getquery = super(UserProfileAdmin, self).get_queryset(request)
        getquery = getquery.order_by('user')
        return getquery

    user_infos.short_description = 'info'


admin.site.register(UserProfile, UserProfileAdmin)
