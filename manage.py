#장고 OVERALL FLOW
#클라이언트 request -> project URL -> (include된걸로) APP URL -> SignInview(create, filter, get) -> database -> 데이터 들고 다시 view.py -> 프론트엔드로 해당 request에 대한 요청값 return

#python manage.py makemigrations: 모델스파이에서 수정이 있을 경우 반드시 쳐야하는 명령어 (ex. initial 0001)
#python manage.py migrate: migrations 속에 정보를 넣어 실제 DB에 적용
#python manage.py showmigrate: 이미 migrate가 적용된 파일은 [X]로, 그렇지 않은 파일은 [ ]로 표현되어 있음.
#python manage.py shell : model.py에 저장되어, db화된 데이터를 불러올 때 사용/ from [앱이름].[models] import [클래스명]  ex) from pybo.models import Question

#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
