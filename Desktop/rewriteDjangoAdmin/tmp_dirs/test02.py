# 显示表字段名字 与 点击字段名进行排序
@register.simple_tag
def build_table_header_column(column,admin_class,filter_conditions,search_filter_text,orderby_key,):
    filters = ''
    for k,v in filter_conditions.items():
        filters += "&%s=%s"%(k,v)
    if orderby_key:
        if orderby_key.startswith('-'):
            sort_icon = '''<span class="glyphicon glyphicon-menu-up" aria-hidden="true"></span>'''
        else:
            sort_icon = '''<span class="glyphicon glyphicon-menu-down" aria-hidden="true"></span>'''
        if orderby_key.strip('-') == column:
            orderby_key = orderby_key
        else:
            orderby_key = column
            sort_icon = ''
    else:
        sort_icon = ''
        orderby_key = column
    try:    #这里的try是因为显示数据库未定义字段时会报错
        column_verbose_name = admin_class.model._meta.get_field(column).verbose_name.upper()
        ele = '''<th><a href="?o={orderby_key}&_q={search_filter_text}&{filters}">{column_verbose_name}</a>{sort_icon}</th>'''\
            .format(orderby_key=orderby_key,filters=filters,column_verbose_name=column_verbose_name,sort_icon=sort_icon,search_filter_text=search_filter_text)
    except FieldDoesNotExist as e:  # 在前端显示数据库中不存在的字段
        column_verbose_name = getattr(admin_class, column).display_name.upper()
        ele = ''' <th><a href="javascript:void(0);">%s</a></th>''' % column_verbose_name
    return mark_safe(ele)