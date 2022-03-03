board=[[0,0],[1,[1,0]],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0],[10,0],[11,0],[12,0],[13,[1,1]],[14,0],[15,0],[16,0],[17,0],[18,0],[19,[1,2]],[20,0],[21,0],[22,0],[23,0],[24,0],[25,0],[26,0],[27,0],[28,0],[29,0],[30,0],[31,0],[32,0],[33,0],[34,0],[35,0],[36,0],[37,0],[38,0],[39,0],[40,0],[41,0],[42,0],[43,0],[44,[2,2]],[45,0],[46,0],[47,0],[48,0],[49,0],[50,[2,1]],[51,0],[52,0],[53,0],[54,0],[55,0],[56,0],[57,0],[58,0],[59,0],[60,0],[61,0],[61,0],[62,[2,0]],[63,0]]
turn=1
win=0
def search(piece):
  for i in range(64):
    square=board[i]
    if square[2]==piece:
      return i
    else:
      pass
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
    elif y1>y0:
      for i in range(y1-y0+1):
        path.append(start+i*8)
    else:
      return 'invalid'
  elif y0==y1:
    if x0>x1:
      for i in range(x0-x1+1):
        path.append(start-i)
    if x1>x0:
      for i in range(x1-x0+1):
        path.append(start+i)
    else:
      return 'invalid'
  elif abs(x0-x1)==abs(y0-y1):
    if x0>x1:
      if y0>y1:
def move(piece,square):
  global board
  global turn
  start=search(piece)
  
  