from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from  .models import ContentContainer, FirstContentItem
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
    
@plugin_pool.register_plugin
class FirstContentItemPlugin(CMSPluginBase):
    model = FirstContentItem
    name = _('First Item')
    render_template = 'content/first-item.html'
    cache = False
    require_parent = True
    parent_classes = ['ContentContainerPlugin']

    def render(self, context, instance, placeholder):
        context = super(FirstContentItemPlugin, self).render(context, instance, placeholder)
        return context
