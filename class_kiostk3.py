def pay(self):
    total = sum(self.order_price)
    print(f"\n총 결제 금액은 {total}원입니다.")

    # 지불 방법 선택
    while True:
        method = input("지불 방법을 선택하세요 (1 또는 'cash', 2 또는 'card') : ").strip().lower()

        if method == 'cash' or method == '1':
            print("직원을 호출하겠습니다.")
            break
        elif method == 'card' or method == '2':
            print("IC칩 방향에 맞게 카드를 꽂아주세요.")
            break
        else:
            print("지불 방법을 다시 입력해주세요 (1/cash 또는 2/card).")

    # 실제 지불 금액 입력
    while True:
        try:
            money = int(input("지불하실 금액을 입력하세요: "))
        except:
            print("숫자만 입력해주세요.")
            continue

        if money < total:
            print(f"{total - money}원이 부족합니다. 다시 입력해주세요.")
        else:
            change = money - total
            print(f"💰 결제가 완료되었습니다. 거스름돈은 {change}원입니다.")
            break
