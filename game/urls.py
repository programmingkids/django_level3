from django.urls import path
from . import views

app_name = "game"

urlpatterns = [
    path('monster/work01', views.Work01View.as_view(), name="monster_work01"),
    path('monster/work02', views.Work02View.as_view(), name="monster_work02"),
    path('monster/work03', views.Work03View.as_view(), name="monster_work03"),
    path('monster/work04', views.Work04View.as_view(), name="monster_work04"),
    path('monster/work05', views.Work05View.as_view(), name="monster_work05"),
    path('monster/work06', views.Work06View.as_view(), name="monster_work06"),
    path('monster/work07', views.Work07View.as_view(), name="monster_work07"),
    path('monster/work08', views.Work08View.as_view(), name="monster_work08"),
    path('monster/work09', views.Work09View.as_view(), name="monster_work09"),
    path('monster/work10', views.Work10View.as_view(), name="monster_work10"),
    path('monster/work11', views.Work11View.as_view(), name="monster_work11"),
    path('monster/work12', views.Work12View.as_view(), name="monster_work12"),
    path('monster/work13', views.Work13View.as_view(), name="monster_work13"),
    path('monster/work14', views.Work14View.as_view(), name="monster_work14"),
    path('player/list', views.PlayerListView.as_view(), name="player_list"),
    path('job/list', views.JobListView.as_view(), name="job_list"),
    path('player/create', views.PlayerrCreateView.as_view(), name="player_create"),
    path('character/list', views.CharacterListView.as_view(), name="characte_list"),
    path('weapon/list', views.WeaponListView.as_view(), name="weapon_list"),
    path('user/list', views.UserListView.as_view(), name="user_list"),
    path('user/create', views.UserCreateView.as_view(), name="user_create"),
]
