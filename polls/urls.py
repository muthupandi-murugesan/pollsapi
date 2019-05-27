from django.urls import path
# from .views import poll_list, poll_detail
# from .apiview import PollList, PollDetail, ChoiceList, CreateVote

#introdusing viewset
from rest_framework.routers import DefaultRouter
from .apiview import PollViewSet, ChoiceList, CreateVote, UserCreate, LoginView

#another way of login endpoint
from rest_framework.authtoken import views

router = DefaultRouter()
router.register('polls', PollViewSet, base_name='polls')

urlpatterns = [
    # path('polls/', poll_list, name="poll_list"),
    # path('polls/', PollList.as_view(), name="poll_list"),
    # path('polls/<int:pk>', poll_detail, name="poll_detail"),
    # path('polls/<int:pk>', PollDetail.as_view(), name="poll_detail"),
    # path("choices/", ChoiceList.as_view(), name="choice_list"),
    path("polls/<int:pk>/choices/", ChoiceList.as_view(), name="choice_list"),
    # path(vote/", CreateVote.as_view(), name="create_vote"),
    path("polls/<int:pk>/choices/<int:choice_pk>/vote/", CreateVote.as_view(), name="create_vote"),
    path("users/", UserCreate.as_view(), name="user_create"),
    # path("login/", LoginView.as_view(), name="login"),
    path("login/", views.obtain_auth_token, name="login"),
]


urlpatterns += router.urls