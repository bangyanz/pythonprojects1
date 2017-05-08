from IPython.display import clear_output

board = ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']
print board[0], board[1], board[2]
print board[3], board[4], board[5]
print board[6], board[7], board[8]
marker = 'x'
index = -1
while True:
    if board[0] == board[1] == board[2] == marker:
        print 'Congrats %s' % marker
        break
    elif board[3] == board[4] == board[5] == marker:
        print 'Congrats %s' % marker
        break
    elif board[6] == board[7] == board[8] == marker:
        print 'Congrats %s' % marker
        break
    elif board[0] == board[3] == board[6] == marker:
        print 'Congrats %s' % marker
        break
    elif board[1] == board[4] == board[7] == marker:
        print 'Congrats %s' % marker
        break
    elif board[2] == board[8] == board[5] == marker:
        print 'Congrats %s' % marker
        break
    elif board[0] == board[4] == board[8] == marker:
        print 'Congrats %s' % marker
        break
    elif board[2] == board[4] == board[6] == marker:
        print 'Congrats %s' % marker
        break
    else:
        if index == 1:
            marker = 'o'
        else:
            marker = 'x'
        print 'enter your location as [x,y]'
        x = input("what is x")
        y = input("what is y")
        n = (x - 1) + (y - 1) * 3
        if board[n] != 'a':
            print 'error'
            break
        board[n] = marker
        index = index * -1

        print board[0], board[1], board[2]
        print board[3], board[4], board[5]
        print board[6], board[7], board[8]
print 'good'
