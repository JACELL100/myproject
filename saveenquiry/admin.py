from django.contrib import admin
from saveenquiry.models import saveenquiry

class saveenquiryAdmin(admin.ModelAdmin):
    list_display=('name','email','phone','websiteLink','message')
    
admin.site.register(saveenquiry,saveenquiryAdmin)   
# Register your models here.
