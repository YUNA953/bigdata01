drinks = ["아메리카노, 카페라떼"]
prices = [1500, 2500]
total_price=0

while True:
    menu = input(f"1) {drinks[0]} {prices[0]}원 2) {drinks[1]} {prices[1]}원 3)주문종료 :")
if menu=="1":
    print(f"{drinks[0]}를 주문하셨습니다 가격은 {prices[0]}입니다.")
elif menu=="2":
    print(f"{drinks[1]}를 주문하셨습니다 가격은 {prices[1]}입니다.")
elif menu=="3":
    printf("주문을 종료합니다.")
else:
    print(f"{menu}번 메뉴는 존재하지 않습니다.")

print(f"총 주문 금액 : {total_price}원")