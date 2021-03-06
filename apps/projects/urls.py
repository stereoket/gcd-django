# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from django.conf import settings
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',
    url(r'^issues_with_several_covers/$', 'apps.projects.views.issues_with_several_covers',
        name='issues_with_several_covers'),
    url(r'^story_reprint_inspection/$', 'apps.projects.views.story_reprint_inspection',
        name='story_reprint_inspection'),
    url('$',  direct_to_template,
        { 'template': 'projects/index.html' }, name='projects_toc'),
)

