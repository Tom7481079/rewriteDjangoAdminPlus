from crm import models
from django.shortcuts import render,HttpResponse,redirect

enabled_admins = {}
class BaseAdmin(object):
	using_add_func = True         #如果需要有单独的添加页面继承时改为false
	using_change_func = True      #如果需要有单独的修改页面继承时改为false
	list_display = []
	readonly_fields = []
	list_filter = []              #显示要过滤的字段（此字段必须是一对多）
	search_fields = []
	actions = ['delete_selected_objs']
	list_per_page = 5
	modelform_exclude_fields = []
	readonly_table = False
	filter_horizontal =[]
	def delete_selected_objs(self, request, selected_ids):
		app_name = self.model._meta.app_label
		table_name = self.model._meta.model_name
		if self.readonly_table:
			errors = {"readonly_table": "table is readonly,cannot be deleted" }
		else:
			errors = {}
		if request.POST.get("delete_confirm") == "yes":
			if not self.readonly_table:     #整张表readonly时不能删除
				objs = self.model.objects.filter(id__in=selected_ids).delete()
			return redirect("/kind_admin/%s/%s/"%(app_name,table_name))   #删除后返回到/kind_admin/crm/customer/页面
		# 这里是通过table_obj_delete.html页面向 /kind_admin/crm/customer/ 的url传送post请求
		return render(request, 'kind_admin/table_obj_delete.html',
		              {'app_name': app_name,
		               'table_name': table_name,
		               'selected_ids': ','.join(selected_ids),
		               'action': request._admin_action})

	def default_form_validation(self):  # clean钩子对整体验证
		''' 每个class_admin都可以重写这个方法来对整体验证'''

def register(model_class,admin_class=BaseAdmin):
	app_name = model_class._meta.app_label
	table_name = model_class._meta.model_name
	if app_name not in enabled_admins:
		enabled_admins[app_name] = {}
	admin_class.model = model_class
	enabled_admins[app_name][table_name] = admin_class

'''
enabled_admins = {'crm':{
   'customer': "<class 'king_admin.kind_admin.CustomerAdmin'>",
   'customerfollowup': "<class 'king_admin.kind_admin.CustomerFollowUpAdmin'>"}
}
'''