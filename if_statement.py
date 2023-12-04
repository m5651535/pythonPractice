age = int(input("請輸入年齡"))
if age >= 100:
    print("年齡過大，無法註冊")
elif age >= 18:
    print("你可以註冊")
elif age < 0:
    print("你未滿 18 歲")
else:
    print("你必須年滿 18 歲才能註冊")
