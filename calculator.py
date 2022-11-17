from replit import clear
import art

# 先定義你要的算法
def add(n1,n2):
  return n1+n2
def subtract(n1,n2):
  return n1-n2
def multiply(n1,n2):
  return n1*n2
def divide(n1,n2):
  return n1/n2

# 把他放到一個dict裡方便call
operations={
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide
}

print(art.calculator)
print("*********************")
print(" ")
print("歡迎來到簡易計算機，你可以將兩個數字做簡易的運算，準備好了嗎?")
print(" ")

def calculation():
    
    num1 = float(input("請輸入一個數字 : "))

    for action in operations:
        print(action)

    should_continue = True
    while should_continue:
        operation_symbol = input("選一個你想要使用的符號 : ")
        num2 = float(input("下一個數字想要輸入什麼呢? : "))
        calculation_function = operations[operation_symbol]
        answer=calculation_function(num1,num2)
        print(f'{num1}{operation_symbol}{num2}={answer}')
        continue_or_not = input(f"輸入 'y' 繼續與 {answer} 做運算 , 或輸入 'n' 重新開始 : ").lower()
        if continue_or_not =="y":
            num1 = answer
        else:
            should_continue = False
            clear()
            calculation()

calculation()