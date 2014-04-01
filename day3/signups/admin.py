from django.contrib import admin

from .models import SignUp

# Register your models here.

class SignUpAdmin(admin.ModelAdmin):
	class Meta:
		model = SignUp
	
	list_display = ('email', 'first_name', 'last_name', 'was_updated_recently')

	list_filter = ['timestamp']

admin.site.register(SignUp, SignUpAdmin)
