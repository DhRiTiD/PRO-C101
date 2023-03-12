import random

def roller(q):
    while q=='yes':
      die=random.randint(1,6)

      if die==1:
         print('''.========.
                
    ⦿  
      
.========.''')
      elif die==2:
         print('''.========.
  ⦿   
       
      ⦿ 
.========.''')
      elif die==3:
         print('''.========.
  ⦿   ⦿ 
        
    ⦿   
.========.''')
      elif die==4:
         print('''.========.
  ⦿   ⦿ 
        
  ⦿   ⦿
.========.''')
      elif die==5:
         print('''.========.
  ⦿   ⦿ 
    ⦿   
  ⦿   ⦿ 
.========.''')
      elif die==6:
         print('''.========.
  ⦿   ⦿ 
  ⦿   ⦿ 
  ⦿   ⦿ 
.========.''')
      q=input('do you want to roll again? (yes/no)')

q=input('roll a die? (yes/no)')
roller(q)

