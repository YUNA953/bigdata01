drinks = ["아메리카노", "카페라떼", "수박주스", "아인슈페너"]
prices = [1500,2500,4000,8000]
total_price=0
#amounts = list()
#for _ in range(len(drinks)):
#    amounts.append(0)

#amounts = [0 for _ in range(len(drinks))]
amounts = [0] * len(drinks)

def order_process(idx):
    global total_price
    print(f"{drinks[idx]}를 주문하셨습니다 가격은 {prices[idx]}입니다.")
    total_price = total_price + prices[idx]
    amounts[idx] = amounts[idx]+1

#menu_texts = ""
#for j in range(len(drinks)):
#    menu_texts = menu_texts + f"{j+1}) {drinks[j]} {prices[j]}원 "
#menu_texts = menu_texts + f"{len(drinks)+1} 주문종료 :"

menu_texts = "".join([f"{j+1}) {drinks[j]} {prices[j]}원 " for j in range(len(drinks))])
menu_texts = menu_texts + f"{len(drinks)+1}) 주문종료:"

while True:
    menu=int(input(menu_texts))
    if len(drinks)>=menu >= 1:
        order_process(int(menu) - 1)
    elif menu== len(drinks)+1:
        print("주문종료")
        break
    else:
        print(f"{menu}번 메뉴는 존재하지 않습니다.")

print(f"{'상품명':^20} {'단가':^6} {'수량':^3} {'금액':^6}")
for i in range(len(drinks)):
    if amounts[i] > 0:
        print(f"{drinks[i]:^20} {prices[i]:^6} {amounts[i]:^3} {prices[i] * amounts[i]:^6} ")

print(f"총 주문 금액 : {total_price}원")