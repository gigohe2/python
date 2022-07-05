#일반 유닛
class Unit:
    def __init__(self, name, hp, damage): # __init__ 은 생성자이다.
        self.name = name # self.name 은 멤버 변수
        self.hp = hp


#공격 유닛
class AttackUnit:
    def __init__(self, name, hp, damage): # __init__ 은 생성자이다.
        self.name = name # self.name 은 멤버 변수
        self.hp = hp
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name,location,self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp<=0:
            print("{0} : 파괴되었습니다.".format(self.name))


# 메딕 : 의무병 -> 공격력이 없음 -> 일반 유닛
# 공격 유닛이 일반 유닛을 상속받아 사용한다.

#파이어뱃 : 공격 유닛, 화염방사기, 
firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

#공격을 2번 받고 죽음
firebat1.damaged(25)
firebat1.damaged(25)