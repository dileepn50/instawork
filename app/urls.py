from django.conf.urls import url, include
from .views import TeamDetails, DeleteTeamMember


urlpatterns = [
    url(r'team_list', TeamDetails.as_view(), name='teamlist'),
    url(r'team_member_edit/(?P<pk>\d+)/', DeleteTeamMember.as_view(), name='edit_team_member'),
]