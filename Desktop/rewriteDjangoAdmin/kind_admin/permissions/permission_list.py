#url type:   0 = related, (代表是相对路径)
#url type:   1 = absolute（代表是绝对路径）

# 用户与权限如何关联
#1. 将perm_dic里的权限名，写到任意表的Meta属性里（必须与权限名相同）
#2. 然后执行 python manage.py makemigrations 命令更新数据库中的表
#3. 更新完成后就可以在我们重写的Django Admin的User表（UserProfile表）中看到可选权限了

perm_dic = {
	'crm.can_access_userprofile_list': {         #可以看到UserProfile表条目列表
		'url_type': 1,                             # 标识url为绝对路径
		'url': '/kind_admin/crm/userprofile/',   # url路径（相对路径就是路径别名）
		'method': 'GET',
		'args': [],         # 接收参数
		# 'args': ['enroll_id','step']
	},
	'crm.can_add_userprofile_get': {           #可以看到UserProfile表的添加页面
		'url_type': 0,                           #0代表使用相对路径名
		'url': 'table_obj_add',                 # url路径（相对路径就是路径别名）
		'method': 'GET',
		'args': [],  # 接收参数
	},
	'crm.can_add_userprofile_post': {         #可以真正添加UserProfile表条目
		'url_type': 0,
		'url': 'table_obj_add',
		'method': 'POST',
		'args': [],
	},
	'crm.can_change_userprofile_get': {
		'url_type': 0,
		'url': 'table_obj_change',
		'method': 'GET',
		'args': [],
	},
	'crm.can_change_userprofile_post': {
		'url_type': 0,
		'url': 'table_obj_change',
		'method': 'POST',
		'args': [],
	},
	'crm.can_delete_userprofile_get': {
		'url_type': 0,
		'url': 'table_obj_delete',
		'method': 'GET',
		'args': [],
	},
	'crm.can_delete_userprofile_post': {
		'url_type': 0,
		'url': 'table_obj_delete',
		'method': 'POST',
		'args': [],
	},
}