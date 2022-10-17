# def addition(a,b):
#     return a + b; 
# print(addition(5,6))   

list = ["car","bike","scooter"]

def loop(items):
    
   print(items*3)
        

def map_sim(i,items):
      for item in items:
          i(item)
map_sim(loop,list)