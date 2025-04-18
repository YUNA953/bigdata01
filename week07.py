from week08 import *
while True:
    try:
        menu = int(input(isplay_menu()))
        if len(drinks) >= menu >= 1:
            rder_process(int(menu) - 1)
        elif menu == len(drinks) + 1:
            print("주문종료")
            break
        else:
            print(f"{menu}번 메뉴는 존재하지 않습니다.")
    except ValueError:
        print(f"{menu}는 잘못된 입력입니다. 숫자를 입력해주세요.")


print_receipt()

