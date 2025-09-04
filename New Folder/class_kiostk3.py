# 문제 3-1. 지불 메서드
# 위의 설명을 참고하여 pay 함수를 구현합니다. 
def pay(self):
    total = sum(self.order_price)
    print(f"총 결재 금액은 \n {total} KRW입니다.")

    while True:
        method = input("지불 방법을 선택하세요 (1 또는 'cash', 2 또는 'card'): ").strip().lower()
        
        if method == 'cash' or method == '1':
            print('현금 결제 선택: 직원을 호출하겠습니다.')
        elif method == 'card' or method == '2':
            print('카드 결제 선택: IC칩에 맞추어서 카드를 꽂아주세요.')
            break
        else:
            print("지불 방법을 다시 입력해주세요. 1 또는 'cash', 2 또는 'card').")
            
    while True:        
        try:
            money = int(input("your total payment: "))
        except :
            print("insert only numbers: ")
            continue 

        if money < total:
            print(f"{total - money}원 부족합니다. 다시 입력해주세요.")
        else:
            change = money - total 
            print(f"결제가 완료되었습니다. 거스름돈은 {change}입니다.")
            break

