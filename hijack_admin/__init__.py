# -*- coding: utf-8 -*-
__version__ = '2.1.10'  # pragma: no cover

import django

if django.VERSION < (3, 2):
    default_app_config = 'hijack_admin.apps.HijackAdminConfig'
