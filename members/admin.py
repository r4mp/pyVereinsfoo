from django.contrib import admin
from .models import Member, Address

class MemberAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['member_id']}

class AddressAdmin(admin.ModelAdmin):
#    prepopulated_fields = {'slug': ['id']}
    pass

admin.site.register(Member, MemberAdmin)
admin.site.register(Address, AddressAdmin)
