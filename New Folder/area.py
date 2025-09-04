class Square:
    def __init__(self):
        self.square = int(input('넓이를 구하고 싶은 사각형의 숫자를 써주세요.\n1. 직각사각형  2. 평행사변형  3. 사다리꼴\n>>> '))

        if self.square == 1:
            self.rect()
        elif self.square == 2:
            self.par()
        elif self.square == 3:
            self.trape()
        else:
            print('1, 2, 3 중에서 다시 입력해주세요.')

    def rect(self):
        w, h = map(int, input("직사각형 - 가로, 세로를 입력하세요 (예: 10,20)\n>>> ").split(','))
        area = w * h
        print(f'직사각형의 넓이: {area}')

    def par(self):
        b, h = map(int, input("평행사변형 - 밑변, 높이를 입력하세요 (예: 10,15)\n>>> ").split(','))
        area = b * h
        print(f'평행사변형의 넓이: {area}')

    def trape(self):
        b1, b2, h = map(int, input("사다리꼴 - 윗변, 아랫변, 높이를 입력하세요 (예: 10,20,15)\n>>> ").split(','))
        area = (b1 + b2) * h / 2
        print(f'사다리꼴의 넓이: {area}')
a= Square()
a.rect()
a.par()
a.trape()
