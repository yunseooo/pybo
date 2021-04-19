#url.py :
#실제 프론트가 요청을 보냈을 때 가장 먼저 어디로 보낼지 판단하는 곳이며 (클래스로 진입하기 위한 진입 메소드를 제공)
#근데 project와 app에 둘 다 urls.py가 있는데 그 둘 중 project에서 먼저 url을 받아서 어디로 갈지 결정. 그래서 project내의 urls.py에 include를 import하는 것
#프론트와 백의 연결 통로, 통신 통로

# ---------------------------------- [edit] ---------------------------------- #
from django.urls import path

from . import views

# ---------------------------------- [edit] ---------------------------------- #
app_name = 'pybo'
# ---------------------------------------------------------------------------- #

urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:question_id>/', views.detail, name = 'detail'),
    # ---------------------------------- [edit] ---------------------------------- #
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    # ---------------------------------------------------------------------------- #
    path( 'question/create/', views.question_create, name = 'question_create'),
]
