 # theater_module.py의 모듈을 사용한다
# import theater_module
# theater_module.price(3) #3명이서 영화 보러감
# theater_module.price_morning(4) #4명이서 조조할인 영화 보러감
# theater_module.price_soldier(5) #5명이서 군인할인 영화 보러감


# import theater_module as mv # theater_module을 mv로 별명을 붙여 mv로 호출할 수 있다.
# mv.price_soldier(4)
# mv.price(3)
# mv.price_morning(5)


# from theater_module import * #모듈명 호출 없이 모듈의 모든 기능들을 바로 사용하겠다.
# # from random import *
# price_morning(5)
# price(3)
# price_soldier(4)


# from theater_module import price, price_morning # 내가 필요한 함수만 가져다 쓸 수 있음
# price(5)
# price_morning(3)
# # 그러나!! price_soldier은 import 하지 않았기 때문에 기능 사용할 수 없다..


from theater_module import price_soldier as ps # price_soldier를 ps으로 별명을 붙여서 가져온다.
ps(3)

