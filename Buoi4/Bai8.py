ROUND = 1
p1_point = 0
p2_point = 0
p1_winning_rounds = []
p2_winning_rounds = []
p1_pen = 0
p2_pen = 0

while True:
    print('ROUND:', ROUND)
    while True:
        try:
            n = int(input('Nhập n:'))
            k = int(input('Nhập k:'))
            if n > k:
                break
            else:
                print('n và k không thỏa mãn. Yêu cầu nhập lại:')
        except ValueError:
            print('Vui lòng nhập lại')

    while n > 0:
        while True:
            try:
                p1 = int(input('Người thứ nhất nhập: '))
                if 1 <= p1 <= k:
                    break
                else:
                    print('Số vừa nhập không thỏa mãn. Yêu cầu nhập lại: ')
                    p1_pen += 1
            except ValueError:
                print('Vui lòng nhập lại: ')
        n -= p1
        if n == 0:
            print('Người thứ nhất thắng round', ROUND)
            p1_point += 1
            p1_winning_rounds.append(ROUND)
            break
        
        while True:
            try:
                p2 = int(input('Người thứ hai nhập: '))
                if 1 <= p2 <= k:
                    break
                else:
                    print('Số vừa nhập không thỏa mãn. Yêu cầu nhập lại: ')
                    p2_pen += 1
            except ValueError:
                print('Vui lòng nhập lại: ')
        n -= p2
        if n == 0:
            print('Người thứ hai thắng round', ROUND)
            p2_point += 1
            p2_winning_rounds.append(ROUND)
            break
        
    while True:
        play_again = input('Bạn muốn chơi lại không? (YES/NO): ')
        if play_again.upper() in ['YES', 'NO']:
            break
        else:
            print('Giá trị không hợp lệ. Yêu cầu nhập lại.')

    if play_again == 'NO':
        break
    ROUND += 1

if p1_point > p2_point:
    print('Người chơi thứ nhất thắng chung cuộc.')
    print('Số round thắng của người chơi thứ nhất là:')
    for i in p1_winning_rounds:
        print(i, end=' ')
elif p1_point < p2_point:
    print('Người chơi thứ hai thắng chung cuộc.')
    print('Số round thắng của người chơi thứ hai là:')
    for i in p2_winning_rounds:
        print(i, end=' ')
else:
    if p1_pen > p2_pen:
        print('Người chơi thứ hai thắng chung cuộc.')
        print('Số round thắng của người chơi thứ hai là:')
        for i in p2_winning_rounds:
            print(i, end=' ')
    elif p1_pen < p2_pen:
        print('Người chơi thứ nhất thắng chung cuộc.')
        print('Số round thắng của người chơi thứ nhất là:')
        for i in p1_winning_rounds:
            print(i, end=' ')
