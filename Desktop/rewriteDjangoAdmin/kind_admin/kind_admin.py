from kind_admin.register_admin import BaseAdmin
from kind_admin.register_admin import register
from kind_admin.register_admin import enabled_admins
from django.shortcuts import render,HttpResponse,redirect
from crm import models

class UserProfileAdmin(BaseAdmin):
	using_add_func = False
	list_display = ['email','name','is_admin','enroll']
	list_filter = ['name','user_type_id',]
	actions = ['delete_selected_objs','my_action']
	readonly_fields = ('password',)
	modelform_exclude_fields = ["last_login",]
	filter_horizontal = ('user_permissions',)
	search_fields = ['name','email',]
	modelform_exclude_fields = ['last_login','groups','roles','is_superuser']

	def my_action(self, request, selected_ids):
		print('selected_ids',selected_ids)
		return HttpResponse('this my_action')

	# 在前端显示数据库中不存在的字段
	def enroll(self):
		if self.instance == 1:
			link_name = "报名新课程"
		else:
			link_name = "报名"
		return '''<a href="/crm/customer/%s/enrollment/"> %s </a>''' %(self.instance.id,link_name)
	enroll.display_name = "报名链接"

	def clean_name(self):  # clean_字段名 是字段钩子（每个字段都有对应的这个钩子）
		print("name clean validation:", self.cleaned_data["name"])
		if not self.cleaned_data["name"]:
			self.add_error('name', "cannot be null")
		else:
			return self.cleaned_data["name"]

	def rewrite_add_page(self,request,app_name,table_name,model_form_class):
		errors = {}
		if request.method == 'POST':
			_password1 = request.POST.get("password")
			_password2 = request.POST.get("password2")
			if _password1 == _password2:
				if len(_password2) > 5:
					form_obj = model_form_class(request.POST)
					if form_obj.is_valid():
						obj = form_obj.save()
						print('obj',obj,type(obj))
						obj.set_password(_password1)  #
						obj.save()
					return redirect(request.path.replace("/add/", '/'))
				else:
					errors['password_too_short'] = "muset not less than 6 letters"
			else:
				errors['invalid_password'] = "passwords are not the same"
		form_obj = model_form_class()
		return render(request, 'kind_admin/rewrite_add_user_page.html',
		              {'form_obj': form_obj,
		               'app_name': app_name,
		               'table_name': table_name,
		               'table_name_detail': self.model._meta.verbose_name_plural,
		               'admin_class': self,
		               'errors': errors,
		               })
register(models.UserProfile,UserProfileAdmin)
