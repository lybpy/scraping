import xadmin
from xadmin.views import BaseAdminPlugin, ListAdminView
from django.template import loader


class ListImportExcelPlugin(BaseAdminPlugin):
    import_excel = False

    def init_request(self, *args, **kwargs):
        return bool(self.import_excel)

    def block_top_toolbar(self, context, nodes):
        nodes.append(loader.render_to_string('xadmin/excel/model_list.toolbar.import.html',context=locals(),request=self.request))


xadmin.site.register_plugin(ListImportExcelPlugin, ListAdminView)
