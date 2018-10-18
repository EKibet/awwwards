from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import PostListView,PostCreateView,CreateView,DetailsView,PostDetailView,CreateProfileView,ProfileDetailsView
from rest_framework.urlpatterns import format_suffix_patterns



urlpatterns=[
    url(r'^$',PostListView.as_view(),name='home'),
    url(r'^post/new/$', PostCreateView.as_view(), name='post-create'),
    # url(r'^post/<int:pk>/update$', PostUpdateView.as_view(), name='post-update'),
    url(r'^signout/$', views.signout, name='signout'),
    url(r'^comment/(?P<post_id>\d+)', views.add_comment, name='comment'),
    
    # url(r'^prof/(?P<username>[-_\w.]+)/$', views.profile, name='prof'),
    # url(r'^profile/(?P<username>[-_\w.]+)/followers/$', views.followers, name='followers'),
    # url(r'^profile/(?P<username>[-_\w.]+)/following/$', views.following, name='following'),
    # url(r'^profile/(?P<username>[-_\w.]+)/$', views.profile, name='profile'),
    # url(r'^post/(?P<pk>\d+)/$', views.post, name='post'),
    # url(r'^profile/(?P<username>[-_\w.]+)/edit/$', views.profile_settings, name='profile_settings'),
    url(r'^search/',views.search_results, name='search_results'),

    # url(r'^post/(?P<pk>\d+)/likes/$', views.likes, name='likes'),
    # url(r'^review/(?P<review_id>[0-9]+)/$', views.review_detail, name='review_detail'),
    # url(r'^post/(?P<post_id>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/(?P<post_id>[0-9]+)/review_design/$', views.add_design, name='add_design'),
    url(r'^post/(?P<post_id>[0-9]+)/review_usability/$', views.add_usability, name='review_usability'),
    url(r'^post/(?P<post_id>[0-9]+)/review_content/$', views.add_content, name='review_content'),

    url(r'^post/(?P<post_id>[0-9]+)/add_vote/$', views.vote, name='add_vote'),
    url(r'^sites/$', CreateView.as_view(), name="create"),
    url(r'^sites/(?P<pk>[0-9]+)/$',DetailsView.as_view(), name="details"),
    url(r'^sites/(?P<pk>[0-9]+)/details$',PostDetailView.as_view(), name="detail"),
    url(r'^api_profile/(?P<pk>[0-9]+)/profile$',CreateProfileView.as_view(), name="details"),
    url(r'^api_detail/(?P<pk>[0-9]+)/detail$',ProfileDetailsView.as_view(), name="detail"),

]
urlpatterns = format_suffix_patterns(urlpatterns)

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)