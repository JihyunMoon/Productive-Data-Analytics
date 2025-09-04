class Kiosk:
    def __init__(self):
        # 메뉴와 가격
        self.menu = ['americano', 'latte', 'mocha', 'yuza_tea', 'green_tea', 'choco_latte']
        self.price = [2000, 3000, 3000, 2500, 2500, 3000]
        self.order_menu = []   # 주문한 메뉴 리스트
        self.order_price = []  # 주문한 가격 리스트

    def menu_print(self):
        print("📋 메뉴판")
        for i in range(len(self.menu)):
            print(f"{i + 1}. {self.menu[i]} : {self.price[i]}원")

    def menu_select(self):
        n = 0

        # 첫 주문
        while n < 1 or n > len(self.menu):
            n = int(input("음료 번호를 입력하세요 : "))
            if 1 <= n and n <= len(self.menu):
                self.price_sum = self.price[n - 1]
            else:
                print("없는 메뉴입니다. 다시 입력해주세요.")

        # 온도 선택
        t = 0
        while t != 1 and t != 2:
            t = int(input("HOT 음료는 1, ICE 음료는 2를 입력하세요 : "))
            if t == 1:
                self.temp = "HOT"
            elif t == 2:
                self.temp = "ICE"
            else:
                print("1 또는 2를 입력해주세요.")

        self.order_menu.append(self.temp + ' ' + self.menu[n - 1])
        self.order_price.append(self.price[n - 1])

        print(self.temp, self.menu[n - 1], ' : ', self.price_sum, '원')

        # 추가 주문
        while True:
            print()
            n = int(input("추가 주문은 음료 번호를, 지불은 0을 누르세요 : "))

            if n == 0:
                print("🧾 주문이 완료되었습니다.")
                for i in range(len(self.order_menu)):
                    print(f"{self.order_menu[i]} : {self.order_price[i]}원")
                print("총 합계 :", sum(self.order_price), "원")
                break

            elif 1 <= n and n <= len(self.menu):
                # 온도 선택
                t = 0
                while t != 1 and t != 2:
                    t = int(input("HOT 음료는 1, ICE 음료는 2를 입력하세요 : "))
                    if t == 1:
                        self.temp = "HOT"
                    elif t == 2:
                        self.temp = "ICE"
                    else:
                        print("1 또는 2를 입력해주세요.")

                menu_name = self.menu[n - 1]
                menu_price = self.price[n - 1]
                self.order_menu.append(self.temp + ' ' + menu_name)
                self.order_price.append(menu_price)

                print(f'추가 주문 음료: {self.temp} {menu_name} : {menu_price}원')
                print(f'현재 합계: {sum(self.order_price)}원')

            else:
                print("없는 메뉴입니다. 다시 주문해주세요.")
