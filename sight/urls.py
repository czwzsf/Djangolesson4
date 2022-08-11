from django.urls import path

from sight import views

urlpatterns = [
    # 景点列表接口
    path('sight/list/', views.SightListView.as_view(), name="sight_list"),
    # 景点详情接口
    path('sight/detail/<int:pk>/', views.SightDetailView.as_view(), name="sight_detail"),
    # 景点评论接口
    path('comment/list/<int:pk>/', views.SightCommentListView.as_view(), name="sight_comment_list")
]
