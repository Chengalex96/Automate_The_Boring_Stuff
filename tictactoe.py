theBoard = {'topL': ' ', 'topM': ' ', 'topR': ' ',
            'midL': ' ', 'midM': ' ', 'midR': ' ',
            'lowL': ' ', 'lowM': ' ', 'lowR': ' '           
            }

import pprint
pprint.pprint(theBoard)

def printBoard(board):
    print(board['topL'] + '|' + board['topM'] + '|' + board['topR'])
    print('-----')
    print(board['midL'] + '|' + board['midM'] + '|' + board['midR'])
    print('-----')
    print(board['lowL'] + '|' + board['lowM'] + '|' + board['lowR'])


print(printBoard(theBoard))