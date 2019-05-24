from django.contrib import admin
from .models import *
from django_admin_hstore_widget.forms import HStoreFormField
from django import forms

# Register your models here.
# admin.site.register(ParseTask)


class ParseTasksAdminForm(forms.ModelForm):
    extra_data = HStoreFormField()

    def __init__(self, *args, **kwargs):
        super(ParseTasksAdminForm, self).__init__(*args, **kwargs)
        self.fields['login'].required = False
        self.fields['password'].required = False
        self.fields['extra_data'].required = False
        # self.fields['user'].required = False

    # def save(self, commit=True):
    #     self.instance.user = self.request.user
    #     return super().save(commit)

    class Meta:
       model = ParseTask
       exclude = ('result',)


@admin.register(ParseTask)
class ParseTaskAdmin(admin.ModelAdmin):
    form = ParseTasksAdminForm
