from django.contrib import admin

# Register your models here.

from django.contrib import admin
from ordered_model.admin import OrderedTabularInline, OrderedInlineModelAdminMixin
from quiz_app.models import *



class PizzaToppingsTabularInline(OrderedTabularInline):
    model = Answer_Choice
    fields = ('answer_choice', 'order','score' ,'move_up_down_links',)
    readonly_fields = ('order', 'move_up_down_links',)
    ordering = ('order',)
    extra = 1


class PizzaAdmin(OrderedInlineModelAdminMixin, admin.ModelAdmin):
    model = Question
    list_display = ('name', )
    inlines = (PizzaToppingsTabularInline, )

admin.site.register(Answer_Choice)

# admin.site.register(Question)
admin.site.register(Question, PizzaAdmin)