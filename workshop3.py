boss = int(input("บอสสั่งให้ไปเก็บส่วยกี่ร้าน : "))
sum = 0
for i in range(1,boss+1) :
    money_shop = float(input(f"เก็บเงินจากร้านที่ {i} ได้เท่าไหร่? : "))
    sum += money_shop
print("จำนวนที่เก็บ : ", boss)
print("จำนวนเงินทั้งหมดที่เก็บได้ : ", sum)