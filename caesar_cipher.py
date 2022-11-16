alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char in alphabet :
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text+=char
  print(f"你是要 {cipher_direction}d 結果是: {end_text}")


import art
print(art.logo)
print("-----------------------------------------")
print(" ")
print('歡迎來到密碼遊戲，使用這個小程式你可以將你的資料加密或解密，快來試試吧!')

should_continue = True
while should_continue:
  direction = input("你要加密或解密? 加密輸入: 'encode' 解密輸入: 'decode' \n")
  text = input("輸入你想要打的文字，請輸入英文、數字或符號:\n").lower()
  shift = (int(input("你想要順移的單位:\n")))%len(alphabet)


# new_shift= shift%len(alphabet)
  caesar(start_text=text, shift_amount=shift,     cipher_direction=direction)
  ans = input("想要再試一次嗎? (yes or no)").lower()
  if ans =="no":
    should_continue = False
    print('Good Bye!!')
