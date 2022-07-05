import inspect
import random
print(inspect.getfile(random)) # random 모듈의 파일 위치를 알려주는 구문
from travel import *

print(inspect.getfile(thailand))
# 실행파일과 같은 라이브러리, 혹은 c아래 파이썬 라이브러리에 모듈 또는 패키지가 존재하면 정상적으로 실행된다.