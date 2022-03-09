def drawboard(board,z10,z11,z12,z20,z21,z22):
  x10=(z10//8)*-1+7
  y10=(z10%8)
  x11=(z11//8)*-1+7
  y11=(z11%8)
  x12=(z12//8)*-1+7
  y12=(z12%8)
  x20=(z20//8)*-1+7
  y20=(z20%8)
  x21=(z21//8)*-1+7
  y21=(z21%8)
  x22=(z22//8)*-1+7
  y22=(z22%8)
  arr=[]
  for i in range(8):
    for j in range(8):
      if i==x10 and j==y10:
        arr.append('0')
      elif i==x11 and j==y11:
        arr.append('1')
      elif i==x12 and j==y12:
        arr.append('2')
      elif i==x20 and j==y20:
        arr.append('a')
      elif i==x21 and j==y21:
        arr.append('b')
      elif i==x22 and j==y22:
        arr.append('c')
      else:
        x=board[8*(i*-1+7)+j]
        if x[1]==-1:
          arr.append('_')
        else:
          arr.append('o')
  boar=''''''
  for i in range(64):
    if i%8==0 and i!=0:
      boar+="\n"
    boar+=arr[i]
  return boar