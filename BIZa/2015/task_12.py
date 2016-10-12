# Задача 12. 
#Разработайте игру "Крестики-нолики"
#Иванова М.Д.
size = 3

board = [ 0 ] * size * size
pics = [' . ', ' x ', ' o ']


def print_board (board):
  print()

  
  for num in range(size):
    print('  ' + str(num +1) + ' ', end='')

  print()

  
  index = 1
  letter = 97
  for cell in board:
    print('|', end='')
    print(pics[cell], end='')
    if index == size:
      print('| ' + chr(letter))
      letter += 1
      index = 0
    index += 1
  print()


def check_board (board):
  
  for row in range(size):
    if board[row] in [1, 2]:
      count = 0
      for cell in range(size):
        if board[row+cell*size] == board[row]:
          count += 1
        else:
          break
      if count == size:
        print_board(board)
        print('x' if board[row] == 1 else 'o', 'is winner!')
        return True

  
  for row in range(0, size * size, size):
    if board[row] in [1, 2]:
      count = 0
      for cell in range(size):
        if board[row+cell] == board[row]:
          count += 1
        else:
            break
      if count == size:
        print_board(board)
        print('x' if board[row] == 1 else 'o', 'is winner!')
        return True

  
  for row in [0, size-1]:
    if board[row] in [1, 2]:
      count = 0
      for cell in range(size):
        if board[row+cell*(size + (1 if row==0 else -1))] == board[row]:
          count += 1
        else:
          break
      if count == size:
        print_board(board)
        print('x' if board[row] == 1 else 'o', 'is winner!')
        return True


print('\nWelcome! Make your turns like this - \'2a\' or \'3c\'')
ixes = True

while True:
  print_board(board)
  turn = input(('x' if ixes else 'o') + ' turn > ')
  try:
    index = ( int(turn[0]) -1 +
             (ord(turn[1]) -97) * size )
    if board[index] in [1, 2]:
      raise
    board[index] = 1 if ixes else 2
  except:
    print('invalid value', turn)
  else:
    if check_board(board):
      break
    ixes = not ixes



input('Press Enter..')