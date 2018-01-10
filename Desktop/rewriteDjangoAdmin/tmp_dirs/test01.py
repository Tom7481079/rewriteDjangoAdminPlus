# 导入我们自己写的 通用权限管理组件
from kind_admin.permissions import permission

@permission.check_permisssion
def display_table_obj(request,app_name,table_name):
	pass

@permission.check_permisssion
def table_obj_add(request,app_name,table_name):
	pass

@permission.check_permisssion
def table_obj_change(request,app_name,table_name,obj_id):
	pass

@permission.check_permisssion
def table_obj_delete(request,app_name,table_name,obj_id):
	pass

