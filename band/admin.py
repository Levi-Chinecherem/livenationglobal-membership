# band/admin.py
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import VacationPricing, GeneralMembership, Autograph, Band, Vacation, MembershipType, Membership

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

class VacationAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'email', 'country', 'preferred_destination', 'preferred_dates']
    search_fields = ['user__email', 'name', 'country', 'preferred_destination']
    list_filter = ['preferred_dates']

class AutographAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'email', 'country', 'band', 'preferred_dates']
    search_fields = ['user__email', 'name', 'country', 'band']
    list_filter = ['preferred_dates']

admin.site.register(VacationPricing)
admin.site.register(Autograph, AutographAdmin)
admin.site.register(Vacation, VacationAdmin)
admin.site.register(Band, BandAdmin)
admin.site.register(MembershipType, MembershipTypeAdmin)
admin.site.register(Membership, MembershipAdmin)
admin.site.register(GeneralMembership)
