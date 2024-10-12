from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from  .models import ContentContainer
from django.utils.translation import gettext_lazy as _

@plugin_pool.register_plugin
class ContentContainerPlugin(CMSPluginBase):
    model = ContentContainer
    name = _('Content Container')
    render_template = 'content/content-container.html'
    cache = False
    allow_children = True

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context
