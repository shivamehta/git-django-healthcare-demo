from django.conf.urls import url
from HealthCare import views

from django.conf.urls.static import static
from django.conf import settings


urlpatterns=[
    url(r'^entitytype$',views.m_entity_typeApi),
    url(r'^entitytype/([0-9A-Fa-f-]+)$',views.m_entity_typeApi),

    url(r'^user$',views.tbl_user_detailApi),
    url(r'^user/([0-9A-Fa-f-]+)$',views.tbl_user_detailApi),
]
