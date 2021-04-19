# model.py : class로 데이터 모델 작성하는 곳 !!데이터베이스 테이블을 만들고 그 안의 필드들을 생성 및 수정할 수 있는 역할 (여기서 만든 DB 테이블의 데이터 처리는 view.py에서)
# 1) 데이터 구조 작성 2) 데이터 타입 결정 3) 데이터 사이의 연관성 결정
# view.py가 알아서 꺼내쓸 수 있도록 가장 먼저 작성한다 (여기서 생성되는 클래스 하나하나가 곧 미래의 표(테이블)이 되며 클래스의 한줄한줄이 하나의 컬럼이 됨)

from django.db import models

# ---------------------------------- [edit] ---------------------------------- #
class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()  #글자수제한없음
    create_date = models.DateTimeField()
# ---------------------------------------------------------------------------- #
    def __str__(self):          #스페셜 메소드. model.py를 통해 만든 객체(인스턴스)가 하나씩 생길 때 대표적으로 어떤 값을 반환할지 명시
        return self.subject

# ---------------------------------- [edit] ---------------------------------- #
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  #ForeignKey:다른모델과 연결, on_delete=models.CASCADE: 질문이 삭제되면 답변도 삭제
    content = models.TextField()
    create_date = models.DateTimeField()
# ---------------------------------------------------------------------------- #