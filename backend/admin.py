from django.contrib import admin
from .models import Category,AdminUser,AuthorUser,MemberUser
from forms import CustomUserChangeForm,CustomUserCreationForm
from django.db.models import Q

class BaseCustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ('email', 'gender', 'image_tag', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    search_fields = ('email',)
    ordering = ('email',)

    fieldsets = (
        (None, {'fields': ('first_name', 'last_name', 'email', 'gender', 'password', 'groups')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'email', 'gender', 'password1', 'password2', 'is_staff', 'is_active', 'groups')}
         ),
    )

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        return "-"
    image_tag.short_description = 'Image'

# Filter users by group or role (adjust logic if using roles instead of groups)
@admin.register(AuthorUser)
class AuthorAdmin(BaseCustomUserAdmin):
    def get_queryset(self, request):
        return super().get_queryset(request).filter(groups__name='Author')


@admin.register(MemberUser)
class MemberAdmin(BaseCustomUserAdmin):
    def get_queryset(self, request):
        return super().get_queryset(request).filter(groups__name='Member')


@admin.register(AdminUser)
class AdminUserAdmin(BaseCustomUserAdmin):
    def get_queryset(self, request):
        return super().get_queryset(request).filter(
            Q(groups__name='Admin') | Q(groups=None)
        )

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)
