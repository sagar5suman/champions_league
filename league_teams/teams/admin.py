from django.contrib import admin
from .models import Club
# Register your models here.

class ClubAdmin(admin.ModelAdmin):    
    list_display = ('name', 'state', 'is_super_qualifier', 'group', 'stored_at')
    list_filter = ('state', 'is_super_qualifier', 'group', 'stored_at')
    search_fields = ('state', )
    list_per_page = 16
    actions = ('set_clubs_to_not_super_qualifier', 'set_clubs_to_super_qualifier')
    fields = (('name', 'state'), 'group', 'is_super_qualifier')
    
    def set_clubs_to_not_super_qualifier(self, request, queryset):
        count = queryset.update(is_super_qualifier=False)
        if count == 1:
            self.message_user(request, 'A club has been marked as not super qualified!')
        else:
            self.message_user(request, f'{count} clubs have been marked as not super qualified!')

    set_clubs_to_not_super_qualifier.short_description = 'Mark clubs as not super qualified'

    def set_clubs_to_super_qualifier(self, request, queryset):
        count = queryset.update(is_super_qualifier=True)
        if count == 1:
            self.message_user(request, 'A club has been marked as super qualified!')
        else:
            self.message_user(request, f'{count} clubs have been marked as super qualified!')
    
    set_clubs_to_super_qualifier.short_description = 'Mark clubs as super qualified'

admin.site.register(Club, ClubAdmin)