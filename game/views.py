from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import CreateView

from django.db.models import Q
from django.db.models import Count, Sum, Avg, Min, Max

from django.contrib.messages.views import SuccessMessageMixin

from .models import Monster
from .models import Player
from .models import Job
from .models import Character
from .models import Weapon
from .models import User

from .forms import PlayerForm
from .forms import UserForm


# Create your views here.
class Work01View( DetailView ) :
    model = Monster
    template_name = "game/monster/detail.html"
    
    def get_object(self):
        object = Monster.objects.get(id=1)
        
        #object = Monster.objects.get(id=2)
        #object = Monster.objects.get(name="ファイヤードラゴン")
        #object = Monster.objects.get(hp=100)
        # error DoesNotExist
        #object = Monster.objects.get(id=1000)
        """
        try:
            object = Monster.objects.get(id=1000)
        except Exception:
            object = None
        """
        return object
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Work01"
        context["message"] = "1件表示"
        return context


class Work02View( ListView ) :
    model = Monster
    template_name = "game/monster/list.html"
    
    def get_queryset(self):
        object_list = Monster.objects.all()
        return object_list
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Work02"
        context["message"] = "一覧表示"
        return context


class Work03View( ListView ) :
    model = Monster
    template_name = "game/monster/list.html"
    
    def get_queryset(self):
        object_list = Monster.objects.filter(name="ファイヤードラゴン")
        #object_list = Monster.objects.filter(name="キングスライム")
        return object_list
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Work03"
        context["message"] = "検索"
        return context


class Work04View( ListView ) :
    model = Monster
    template_name = "game/monster/list.html"
    
    def get_queryset(self):
        object_list = Monster.objects.filter(name__contains="ドラゴン")
        #object_list = Monster.objects.filter(name__contains="スライム")
        #object_list = Monster.objects.filter(name__startswith="ファイヤー")
        #object_list = Monster.objects.filter(name__endswith="ドラゴン")
        return object_list
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Work04"
        context["message"] = "あいまい検索"
        return context


class Work05View( ListView ) :
    model = Monster
    template_name = "game/monster/list.html"
    
    def get_queryset(self):
        object_list = Monster.objects.filter(hp=30)
        #object_list = Monster.objects.filter(mp=30)
        #object_list = Monster.objects.filter(hp__gt=50)
        #object_list = Monster.objects.filter(hp__gte=50)
        #object_list = Monster.objects.filter(hp__lt=40)
        #object_list = Monster.objects.filter(hp__lte=40)
        return object_list
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Work05"
        context["message"] = "数値検索"
        return context


class Work06View( ListView ) :
    model = Monster
    template_name = "game/monster/list.html"
    
    def get_queryset(self):
        object_list = Monster.objects.filter(hp__gte=40, hp__lte=80)
        #object_list = Monster.objects.filter(mp__gte=30, mp__lte=60, name__contains="ドラゴン")
        #object_list = Monster.objects.filter(mp__gte=30).filter(mp__lte=60).filter(name__contains="ドラゴン")
        return object_list
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Work06"
        context["message"] = "AND検索"
        return context


class Work07View( ListView ) :
    model = Monster
    template_name = "game/monster/list.html"
    
    def get_queryset(self):
        object_list = Monster.objects.filter(Q(hp__lte=30) | Q( hp__gte=80))
        #object_list = Monster.objects.filter(Q(hp__lte=10) | Q( mp__lte=10))
        return object_list
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Work07"
        context["message"] = "OR検索"
        return context


class Work08View( ListView ) :
    model = Monster
    template_name = "game/monster/list.html"
    
    def get_queryset(self):
        names = ["ファイヤードラゴン","キングスライム", "ダークナイト"]
        object_list = Monster.objects.filter(name__in=names)
        return object_list
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Work08"
        context["message"] = "リスト検索"
        return context


class Work09View( ListView ) :
    model = Monster
    template_name = "game/monster/list.html"
    
    def get_queryset(self):
        object_list = Monster.objects.all().order_by("hp")
        #object_list = Monster.objects.all().order_by("hp").reverse()
        #object_list = Monster.objects.filter(name__contains="ドラゴン").order_by("mp").reverse()
        return object_list
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Work09"
        context["message"] = "並び替え"
        return context


class Work10View( ListView ) :
    model = Monster
    template_name = "game/monster/list.html"
    
    def get_queryset(self):
        object_list = Monster.objects.all().order_by("hp")[2:4]
        #object_list = Monster.objects.filter(name__contains="ドラゴン").order_by("hp").reverse()[0:2]
        return object_list
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Work10"
        context["message"] = "範囲指定"
        return context


class Work11View( DetailView ) :
    model = Monster
    template_name = "game/monster/detail.html"
    
    def get_object(self):
        object = Monster.objects.all().order_by("mp").last()
        object = Monster.objects.all().filter(name__contains="ドラゴン").order_by("hp").first()
        return object
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Work11"
        context["message"] = "特定のレコード"
        return context


class Work12View( DetailView ) :
    model = Monster
    template_name = "game/monster/count.html"
    
    def get_object(self):
        object = Monster.objects.all().filter(name__contains="ドラゴン").count()
        #object = Monster.objects.all().filter(hp__gte=40).count()
        return object
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Work12"
        context["message"] = "カウント"
        return context


class Work13View( ListView ) :
    model = Monster
    template_name = "game/monster/values.html"
    
    def get_queryset(self):
        object_list = Monster.objects.filter(name__contains="スライム").values()
        #object_list = Monster.objects.filter(hp__lte=40).values("id","name","hp")
        #object_list = Monster.objects.filter(mp__gte=50).values_list()
        #object_list = Monster.objects.filter(mp__gte=50).values_list("id","name","mp")
        return object_list
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Work13"
        context["message"] = "取得形式変更"
        return context


class Work14View( ListView ) :
    model = Monster
    template_name = "game/monster/aggregate.html"
    
    def get_queryset(self):
        object_list = Monster.objects.all().aggregate(Count('id'))
        #object_list = Monster.objects.all().aggregate(Sum('hp'))
        #object_list = Monster.objects.all().aggregate(Avg('mp'))
        #object_list = Monster.objects.filter(name__contains="ドラゴン").aggregate(Min('hp'))
        #object_list = Monster.objects.filter(name__contains="スライム").aggregate(Max('hp'))
        return object_list
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Work14"
        context["message"] = "集計"
        return context


class PlayerListView( ListView ) :
    model = Player
    template_name = "game/player/list.html"
    
    def get_queryset(self):
        object_list = Player.objects.select_related("job").all()
        return object_list
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Work04"
        context["message"] = "プレイヤー一覧"
        return context


class JobListView( ListView ) :
    model = Job
    template_name = "game/job/list.html"
    
    def get_queryset(self):
        object_list = Job.objects.prefetch_related('player_set').all()
        return object_list
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Work05"
        context["message"] = "職業一覧"
        return context


class PlayerrCreateView( CreateView ) :
    model = Player
    form_class = PlayerForm
    success_url = reverse_lazy("game:player_list")
    template_name = "game/player/create.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Work06"
        context["message"] = "プレイヤー新規作成"
        return context


class CharacterListView( ListView ) :
    model = Character
    template_name = "game/character/list.html"
    
    def get_queryset(self):
        object_list = Character.objects.prefetch_related("weapon_set").all()
        return object_list
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Work08"
        context["message"] = "キャラクター一覧"
        return context


class WeaponListView( ListView ) :
    model = Weapon
    template_name = "game/weapon/list.html"
    
    def get_queryset(self):
        object_list = Weapon.objects.prefetch_related("character").all()
        return object_list
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Work09"
        context["message"] = "武器一覧"
        return context


class UserListView( ListView ) :
    model = User
    template_name = "game/user/list.html"
    paginate_by = 4
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "バリデーション処理"
        context["message"] = "ユーザー一覧"
        return context


class UserCreateView( SuccessMessageMixin, CreateView ) :
    model = User
    form_class = UserForm
    success_url = reverse_lazy('game:user_list')
    template_name = "game/user/create.html"
    success_message = "ユーザ登録が完了しました"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "バリデーション処理"
        context["message"] = "ユーザー一覧"
        return context

