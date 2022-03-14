from django.conf.urls import url
from django.contrib.auth.decorators import login_required, permission_required
from apps.users.views import userCreate, userList, userDelete, userEdit, user_create, user_edit, user_list, user_delete

urlpatterns = [
    url(r'^create', userCreate.as_view(), name='usersCreate'),
    url(r'^delete/(?P<pk>\d+)/', permission_required('user.delete_profile')(userDelete.as_view()), name='usersDelete'),
    url(r'^edit/(?P<pk>\d+)/', permission_required('user.delete_profile')(userEdit.as_view()), name='usersEdit'),
    url(r'^list', permission_required('user.delete_profile')(userList.as_view()), name='usersList'),
    url(r'^fcreate/', user_create, name='user_create'),
    url(r'^flist/', permission_required('user.delete_profile')(user_list), name='user_list'),
    url(r'^fedit/(?P<pk>\d+)/', permission_required('user.delete_profile')(user_edit), name='user_edit'),
    url(r'^fdelete/(?P<pk>\d+)/', permission_required('user.delete_profile')(user_delete), name='user_delete'),
]
