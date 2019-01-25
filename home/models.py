from django.db import models
from wagtail.core.models import Page
from wagtail_mod.edit_handlers import get_edit_handler


class HomePage(Page):
    get_edit_handler = get_edit_handler
