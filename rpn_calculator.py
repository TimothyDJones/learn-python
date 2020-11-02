import operator
ops = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
while True:
  try:
    st = []
    for tk in str.split(input()):
      if tk in ops:
        y,x = st.pop(),st.pop()
        z = ops[tk](x,y)
      else:
        z = float(tk)
      st.append(z)
    assert len(st)<=1
    if len(st)==1: print(st.pop())
  except EOFError:  break
  except:  print('error')