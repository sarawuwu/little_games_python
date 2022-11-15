rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


# 加入random模組
import random

# 建立一個list
total_list=[rock,paper,scissors]

# 先讓玩家輸入，而得到一個值
player_num=int(input("請輸入0石頭、1布、2剪刀，其中一個數字 : "))
if player_num >2 and player_num<0:
  print('輸入錯誤')
else:
  print("你的出拳: ")
  print(total_list[player_num])
  
  # 再讓電腦隨機產生一個值
  
  print("電腦的出拳: ")
  # computer_num=0
  computer_num=random.randint(0,2)
  print(total_list[computer_num])
  
  # 再將兩值比較，進而判斷結果
  
  if player_num == computer_num:
    print("平手啦!! 再來一次")
  elif player_num == 0 and computer_num == 2:
    print("你贏了 >.<")
  elif player_num == 2 and computer_num == 0 :
    print("顆顆，你輸了")
  elif player_num > computer_num:
    print("你贏了 >..<")

