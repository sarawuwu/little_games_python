# ASCII art
from art import guess_number_logo
print(guess_number_logo)

# 建立一個隨機數字
import random
computer_number = random.randint(1,100)
print(computer_number)

# 設定變數
lowest_number=1
highest_number=100

should_continue = True

# 讓用戶選擇要hard還是easy 然後判斷

level=(input('今天想要挑戰什麼級別的關卡? (請輸入 hard 或 easy) ').lower())
  # 判斷難易度的if
if level == "easy":
  lives = 10
elif level =="hard":
  lives =5
else:
  print("錯誤，請輸入easy或hard。")
  should_continue = False


while should_continue:
     
  player_number=int(input("Guess a number:"))
  if player_number == computer_number:
    print(f"太棒了，你猜中了!答案就是 : {player_number}。")
    should_continue=False
  else:
    lives -= 1
    if lives == 0:
      should_continue = False
      print('你輸了。')
    else:
      if player_number> computer_number:
        print("數字猜的太大了。")
        if player_number<highest_number:
            highest_number=player_number
      else:
        print("數字猜得太低了")
        if player_number>lowest_number:
            lowest_number=player_number
    
      print(f'你還有 {lives} 次機會. 範圍從 {lowest_number} 到 {highest_number} ，再猜一次吧!!')




