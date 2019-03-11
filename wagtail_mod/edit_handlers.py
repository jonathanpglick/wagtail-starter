from django.utils.translation import ugettext_lazy
from wagtail.utils.decorators import cached_classmethod
from wagtail.admin.edit_handlers import TabbedInterface, ObjectList

@cached_classmethod
def get_edit_handler(cls):
    """
    Get the EditHandler to use in the Wagtail admin when editing this page type.
    """
    if hasattr(cls, 'edit_handler'):
        return cls.edit_handler.bind_to_model(cls)

    # construct a TabbedInterface made up of content_panels, promote_panels
    # and settings_panels, skipping any which are empty
    tabs = []

    if cls.content_panels:
        tabs.append(ObjectList(cls.content_panels, heading=ugettext_lazy('Content')))
    if cls.promote_panels:
        #MOD: Changed heading of `promote_panels` to `SEO`.
        tabs.append(ObjectList(cls.promote_panels, heading=ugettext_lazy('SEO')))
    if cls.settings_panels:
        tabs.append(ObjectList(cls.settings_panels, heading=ugettext_lazy('Settings'), classname="settings"))

    edit_handler = TabbedInterface(tabs, base_form_class=cls.base_form_class)
    return edit_handler.bind_to_model(cls)
