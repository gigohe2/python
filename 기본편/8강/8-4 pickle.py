import pickle
# profile_file = open("profile.pickle", "wb")#wb는 바이너리(2진수)타입 쓰기
# profile={"이름":"박명수", "나이":30, "취미":["축구","골프","코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) # profile에 있는 정보를 profile_file에
# profile_file.close()

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) #file에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close()
