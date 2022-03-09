from board import drawboard

board=[[0,0],[1,[1,0]],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0],[10,0],[11,0],[12,0],[13,[1,1]],[14,0],[15,0],[16,0],[17,0],[18,0],[19,[1,2]],[20,0],[21,0],[22,0],[23,0],[24,0],[25,0],[26,0],[27,0],[28,0],[29,0],[30,0],[31,0],[32,0],[33,0],[34,0],[35,0],[36,0],[37,0],[38,0],[39,0],[40,0],[41,0],[42,0],[43,0],[44,[2,2]],[45,0],[46,0],[47,0],[48,0],[49,0],[50,[2,1]],[51,0],[52,0],[53,0],[54,0],[55,0],[56,0],[57,0],[58,0],[59,0],[60,0],[61,0],[62,[2,0]],[63,0]]
turn=1
activepiece=-1
win=0
def search(piece):
  for i in range(64):
    square=board[i]
    if square[1]==piece:
      return i
    else:
      pass
def makeboard():
  global board
  z10=search([1,0])
  z11=search([1,1])
  z12=search([1,2])
  z20=search([2,0])
  z21=search([2,1])
  z22=search([2,2])
  return drawboard(board,z10,z11,z12,z20,z21,z22)
def path(start,end):
  x0=start%8
  y0=start//8
  x1=end%8
  y1=end//8
  path=[]
  if x0==x1:
    if y0>y1:
      for i in range(y0-y1+1):
        path.append(start-i*8)
      return path
    elif y1>y0:
      for i in range(y1-y0+1):
        path.append(start+i*8)
      return path
    else:
      return []
  elif y0==y1:
    if x0>x1:
      for i in range(x0-x1+1):
        path.append(start-i)
      return path
    if x1>x0:
      for i in range(x1-x0+1):
        path.append(start+i)
      return path
    else:
      return []
  elif abs(x0-x1)==abs(y0-y1):
    if x0>x1:
      if y0>y1:
        for i in range(x0-x1+1):
          path.append(start-9*i)
      else:
        for i in range(x0-x1+1):
          path.append(start+7*i)
    else:
      if y0>y1:
        for i in range(x1-x0+1):
          path.append(start-7*i)
      else:
        for i in range(x1-x0+1):
          path.append(start+9*i)
  else:
    return []
  return path
def valid_path(path):
  global board
  result=1
  for i in range(1,len(path)):
    x=path[i]
    y=board[x]
    result=result*(y[1]==0)
  return result
def move(piece,square):
  global board
  start=search(piece)
  trail=path(start,square)
  if trail==[]:
    return False
  elif valid_path(trail)==0:
    return False
  else: 
    board[square]=[square,piece]
    board[start]=[start,0]
    return True
def shoot(piece,square):
  global board
  start=search(piece)
  trail=path(start,square)
  if trail==[]:
    return False
  elif valid_path(trail)==0:
    return False
  else:
    board[square]=[square,-1]
    return True

def ispiecedead(piece):
  global board
  square=search(piece)
  result=1
  x=square%8
  y=square//8
  for i in [-1,0,1]:
    for j in [-1,0,1]:
      if i==j and i==0:
        pass
      elif x+i>7 or x+i<0:
        pass
      elif y+j>7 or y+j<0:
        pass
      else:
        checksquare=8*(y+j)+x+i
        result*=((board[checksquare])[1]!=0)
  return bool(result)
def isgameover():
  global board
  global turn
  if ispiecedead([1,0]) and ispiecedead([1,1]) and ispiecedead([1,2]):
    return 2
    if ispiecedead([2,0]) and ispiecedead([2,1]) and ispiecedead([2,2]):
      return (turn-1)*-1+2
  elif ispiecedead([2,0]) and ispiecedead([2,1]) and ispiecedead([2,2]):
    return 1
  else:
    return 0
def game():
  global turn
  global board
  print(makeboard())
  if isgameover()!=0:
    if isgameover()==1:
      return 'Player 1 wins'
    elif isgameover()==2:
      return 'Player 2 wins'
  if turn==1:
    x=-1
    while x==-1:
      x=input('Player 1, what piece do you want to move?')
      if (x=='0' or x=='1' or x=='2'):
        x=int(x)
        if ispiecedead([1,x]):
          print('Invalid')
          x=-1
        else:
          x=[1,x]
      else:
        x=-1
    y=-1
    while y==-1:
      y=int(input('Where do you want to move?'))
      if isinstance(y,int) and y>=0 and y<=63 and move(x,y):
        pass
      else:
        y=-1
        print('Invalid')
    z=-1
    while z==-1:
      z=int(input('Where do you want to shoot?'))
      if isinstance(z,int) and z>=0 and z<=63 and shoot(x,z):
        turn=2
      else:
        z=-1
        print('Invalid')
    game()
  if turn==2:
    x=-1
    while x==-1:
      x=input('Player 2, what piece do you want to move?')
      if x=='a' and not ispiecedead([2,0]):
        x=[2,0]
      elif x=='b' and not ispiecedead([2,1]):
        x=[2,1]
      elif x=='c' and not ispiecedead([2,2]):
        x=[2,2]
      else:
        x=-1
    y=-1
    while y==-1:
      y=int(input('Where do you want to move?'))
      if isinstance(y,int) and y>=0 and y<=63 and move(x,y):
        pass
      else:
        y=-1
        print('Invalid')
    z=-1
    while z==-1:
      z=int(input('Where do you want to shoot?'))
      if isinstance(z,int) and z>=0 and z<=63 and shoot(x,z):
        turn=1
      else:
        z=-1
        print('Invalid')
    game()
game()