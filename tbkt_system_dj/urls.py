#coding: utf-8
from django.conf import settings
from django.conf.urls import include, url, patterns

urlpatterns = patterns('',
    url(r'^apidoc/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.APIDOC_DIR}),  # 接口文档
)

urlpatterns += patterns('',
    url(r'account/', include('tbkt_system_dj.account.urls')),       # 系统
    url(r'ticket/', include('tbkt_system_dj.ticket.urls')),         # 工单系统
)
