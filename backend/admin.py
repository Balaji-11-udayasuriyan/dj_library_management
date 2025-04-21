from django.contrib import admin
from .models import Category,AdminUser,AuthorUser,MemberUser,CustomUser,BookAuthor,Book
from backend.forms import CustomUserChangeForm,CustomUserCreationForm
from django.db.models import Q

from django.contrib.auth.admin import UserAdmin


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

class BookAuthorInline(admin.TabularInline):
    model = BookAuthor
    extra = 1  # Show 1 empty row to add new relationships

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        if db_field.name == 'author':
            # Filter only users in the "Author" group
            kwargs["queryset"] = CustomUser.objects.filter(groups__name='Author')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

    inlines = [BookAuthorInline]

    list_display = ('title', 'category', 'publication_date', 'copies_owned', 'image_tag',)

    search_fields = ('title',)

    list_filter = ('category', 'publication_date')

    def image_tag(self, obj):
        return format_html('<img src = "{}" width = "150" height="150" />'.format(obj.cover_image.url))

    image_tag.short_description = 'Image'


# Utility function to filter only members
def get_member_queryset():
    return CustomUser.objects.filter(groups__name='Member')

