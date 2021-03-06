# -*- coding: utf-8 -*-
#
# Copyright (C) Pootle contributors.
# Copyright (C) Zing contributors.
#
# This file is a part of the Zing project. It is distributed under the GPL3
# or later license. See the LICENSE file for a copy of the license and the
# AUTHORS file for copyright and authorship information.

from django.views.defaults import (
    page_not_found as django_404,
    permission_denied as django_403,
    server_error as django_500,
)

from .api import APIView
from .base import BasePathDispatcherView, PootleAdminView, PootleJSON
from .browse import BaseBrowseDataJSON, PootleBrowseView
from .export import PootleExportView
from .translate import PootleTranslateView


__all__ = (
    "APIView",
    "BaseBrowseDataJSON",
    "BasePathDispatcherView",
    "PootleJSON",
    "PootleAdminView",
    "PootleBrowseView",
    "PootleExportView",
    "PootleTranslateView",
)


def permission_denied(request, exception):
    return django_403(request, exception, template_name="errors/403.html")


def page_not_found(request, exception):
    return django_404(request, exception, template_name="errors/404.html")


def server_error(request):
    return django_500(request, template_name="errors/500.html")
