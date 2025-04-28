from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import User
from .forms import UserCreationForm, UserChangeForm

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('phone_number', 'name', 'last_name', 'email',
                    'photo', 'is_active', 'is_admin', 'is_superuser')
    list_filter = ('is_admin', 'is_active', 'is_superuser')
    fieldsets = (
        (_('Personal info'), {'fields': ('phone_number', 'password', 'name', 'last_name', 'email',
                                         'photo')}),
        (_('Permissions'), {'fields': ('is_active', 'is_admin', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone_number', 'name', 'last_name', 'email',
                       'photo', 'password1', 'password2', 'is_active', 'is_admin', 'is_superuser'),
        }),
    )
    search_fields = ('phone_number', 'email', 'name', 'last_name')
    ordering = ('phone_number',)
    filter_horizontal = ()

    def save_model(self, request, obj, form, change):
        if form.cleaned_data.get('password'):
            raw_password = form.cleaned_data['password']
            if not obj.password.startswith('pbkdf2_'):
                obj.set_password(raw_password)
        super().save_model(request, obj, form, change)

admin.site.register(User, UserAdmin)











# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from .models import User
# from .forms import UserCreationForm, UserChangeForm
#
# class UserAdmin(BaseUserAdmin):
#     form = UserChangeForm
#     add_form = UserCreationForm
#
#     list_display = ('phone_number', 'name', 'last_name', 'email',
#                      'photo', 'is_active', 'is_admin', 'is_superuser')
#     list_filter = ('is_admin', 'is_active', 'is_superuser')
#     fieldsets = (
#         ('Personal info', {'fields': ('phone_number', 'password', 'name', 'last_name', 'email',
#                                        'photo')}),
#         ('Permissions', {'fields': ('is_active', 'is_admin', 'is_superuser')}),
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('phone_number', 'name', 'last_name', 'email',
#                         'photo', 'password1', 'password2', 'is_active', 'is_admin', 'is_superuser'),
#         }),
#     )
#     search_fields = ('phone_number', 'email', 'name', 'last_name')
#     ordering = ('phone_number',)
#     filter_horizontal = ()
#
# admin.site.register(User, UserAdmin)
