import xadmin
from xadmin import views
from .models import Goods


class BaseSetting(object):
    enable_themes = False
    use_bootswatch = False


class GlobalSettings(object):
    site_title = "程序后台"
    site_footer = "后台管理系统"
    # menu_style = "accordion"


class GoodsAdmin(object):
    list_display = ['name', 'content']
    exclude = ('is_delete',)

    search_fields = ['name', ]
    list_filter = ["name"]


xadmin.site.register(Goods, GoodsAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
