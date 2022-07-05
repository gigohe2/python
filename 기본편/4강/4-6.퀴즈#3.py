# http:// 부분 제외
# 처음 만나는 점(.) 이후 부분 제외
# 남은 글자 중 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 암호 구성



address="http://naver.com"

rule1=address[7:]
#rule1=address.replace("http://", "")

rule2=rule1[:rule1.index(".")]

size=len(rule2)
enum=rule2.count('e')


rule3=rule2[:3]+str(size)+str(enum)+'!'

print(address, "의 비밀번호는" , rule3, "입니다.")