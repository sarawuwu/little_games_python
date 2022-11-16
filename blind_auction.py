from replit import clear
import art


print(art.hammer)

print("歡迎來到競標遊戲")
print("這是一場不公開的單盲競標，將會由出價最高者獲勝")
print("準備好你的價格，遊戲即將開始!!")

print("************************************")

people={}
name = input("你是誰? 請輸入你的名字 : ")
price = int(input("你想出多少錢? $:"))
# people = {name:price}
people[name]= price


again = input("還有其他人想要出價嗎? (請輸入:yes/no) :").lower()

try_again = True
while try_again :
  if again == "yes":
      clear()
      name = input("你是誰? 請輸入你的名字 : ")
      price = int(input("你想出多少錢? $:"))
      people[name] = price
      again=input("還有其他人想要出價嗎? (請輸入:yes/no) :").lower()
  else:
    clear()
    try_again =False
    highest_bid =0
    for bidder in people:
      if people[bidder]> highest_bid:
        highest_bid=people[bidder]
        winner = bidder
    print(f'贏家是: {winner} ， 最高價為 $ {highest_bid}')
