class sqaure():

      def __init__(self):
          self.val =0
      def __iter__(self):
          return self
      def __next__(self):
          self.val+=1
          return self.val**2
sq = sqaure()
count=0
for num in sq:
    print(num,end=' ')
    if count==10:
        break
    count+=1

