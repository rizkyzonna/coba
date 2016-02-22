from django.contrib import admin
#from django.contrib import admin.site
from .models import Choice, Question
#from .models import Judul, Artikel

class ChoiceInline(admin.StackedInline):
	model = Choice
	extra = 3
class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,			{'fields':['question_text']}),
		('Date information',	{'fields':['pub_date'],'classes':['collapse']}),
	]
	list_display = ('question_text','pub_date','was_published_recently')
	list_filter = ['pub_date']
	search_fields = ['question_text'] 
	inlines = [ChoiceInline]

#class JudulAdmin(admin.ModelAdmin):
#		fieldsets = [
#			(None, {'fields':['judul_text']}),
#			('Date information', {'fields':['pub_date'],'classes':['collapse']}),
#			]
#		list_display=('judul_text','pub_date','recent_published')
#		list_filter =['pub_date']
#		search_fields=['judul_text']
#		inlines=[ChoiceInline]

				
admin.site.register(Question, QuestionAdmin)
# Register your models here.
