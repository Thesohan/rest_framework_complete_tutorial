from django.urls import path,include
from rest_framework.routers import DefaultRouter
from snippets import views



#create a router and register our viewserts with it

router = DefaultRouter()
router.register(r'snippets',views.SnippetViewSet)
router.register(r'users',views.UserViewSet)


urlpatterns = [
    path('',include(router.urls))
]


# from django.urls import path
# # from . import views
# from rest_framework.urlpatterns import format_suffix_patterns

# # urlpatterns =[
# #     path('',views.api_root,name='root'),
# #     path('snippets/',views.SnippetList.as_view(),name='snippet-list'),
# #     path('snippets/<int:pk>/',views.SnippetDetail.as_view(),name='snippet-detail'),
# #     path('snippets/<int:pk>/highlight/',views.SnippetHighlight.as_view(),name='snippet-highlight'),
# #     path('users/',views.UserList.as_view(),name='user-list'),
# #     path('user/<int:pk>/',views.UserDetail.as_view(),name= 'user-detail'),
# # ]
# # urlpatterns = format_su

# from .views import SnippetViewSet, UserViewSet, api_root

# from rest_framework import renderers

# snippet_list = SnippetViewSet.as_view({
#     'get':'list',
#     'post':'create'
# })

# snippet_detail = SnippetViewSet.as_view({
#     'get':'retrive',
#     'put':'update',
#     'patch':'partial_update',
#     'delete':'destroy'
# })

# snippet_highlight = SnippetViewSet.as_view({
#     'get':'highlight'
# })

# user_list = UserViewSet.as_view({
#     'get':'list'
# })

# user_detail  = UserViewSet.as_view({
#     'get':'retrive'
# })

# urlpatterns =format_suffix_patterns([
#     path('',api_root,name='root'),
#     path('snippets/',snippet_list,name='snippet-list'),
#     path('snippets/<int:pk>/',snippet_detail,name='snippet-detail'),
#     path('snippets/<int:pk>/highlight/',snippet_highlight,name='snippet-highlight'),
#     path('users/',user_list,name='user-list'),
#     path('user/<int:pk>/',user_detail,name= 'user-detail'),
# ])
