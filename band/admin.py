# band/admin.py
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Band, MembershipType, Membership

admin.site.site_title = _('LiveNationGlobal Admin')
admin.site.site_header = _('LiveNationGlobal Administration')
admin.site.index_title = _('Site Administration')

class MembershipInline(admin.TabularInline):
    model = Membership
    extra = 1

class MembershipTypeInline(admin.TabularInline):
    model = MembershipType
    extra = 1

class BandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [MembershipTypeInline]

class MembershipTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'band', 'price')

class MembershipAdmin(admin.ModelAdmin):
    list_display = ('user', 'band', 'membership_type', 'payment_type', 'country', 'state', 'city', 'address')
    search_fields = ('user__email', 'band__name', 'membership_type__name', 'payment_type', 'country', 'state', 'city')

admin.site.register(Band, BandAdmin)
admin.site.register(MembershipType, MembershipTypeAdmin)
admin.site.register(Membership, MembershipAdmin)
