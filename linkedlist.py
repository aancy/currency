class Node:
    def_int_(self,data):
        self data=data
        self Next=Next
class singly linged list:
    def_int_(self):
        self.head=none
        def display(self)
        temp=selfhead
        while(temp!=none):
            print(temp.data,'"==">",end=" ")
        temp =temp next
             print("None")
        def insertion_at_beggining(self,data):
                  temp=node(data)
                  temp next=self head
                  self head=temp
        def insertion_at_middle(self,data):
                  temp=node(data)
                  temp1=self.head
                  if temp==none
                  self insertion_at_beggining(data)
                  else:
                  c=1
                  while(c!pos-1)
                    temp1=temp1.next
                      c+=1
                   temp1.next=temp1.next
                  temp1.next=temp
        def insertion_at_end(self,data)
                  temp=node(data)
                  temp=self.head
                  while(temp!=next!=none):
                  temp1=temp1.next
                  temp1.next=temp
        def deletion_at_beggining(self):
                  temp=self.head
                  if temp==none:
                  print("invalid")
                  else self.head=temp.next
                  temp.next=none
                  self display()
        def deletion_at_middle(self,pos):
                  temp1=self.head
                  c=1
                  while(c!=pos_1):
                  temp1=temp1.next
                  c+=1
                  temp=temp1.next
                  temp1.next=temp.next
                  temp next=none
         def deletion_at_end(self):
                  temp=self.head
                  temp1=temp.next
                  while(temp1.next!=none)
                  temp1=temp1.next
                  temp.next=none
                  self display()
         obj=singly_linked_list()
                  ch=0
                  while(ch!=8):
                  print('1.insertion_at_begging','2.insertion_at_middle','3.insertion_at_end,'4.deletion_at_beggining,'5.deletion_at_middle,'6.deletion_at_end)
                  ch=int(input())
                  if(ch==2):
                  print("enter the node to be inserted at beggining")
                  datda=input()
                  obj.insertion at begging(data)
                  obj.display()
                  if(CH=2)
                  print("enter the node to be inserted at middle")
                  data=input()
                  obj.insertion _at_middle(data)
                   
                  obj.display()
                  if(ch=3)
                  print("enter thr node to be inserted at end")
                  data=input
                  obj.insertion_at_end(data)
                  obj.display
                  if(ch=4):
                  obj.deletion_at_begging()
                  if(ch==5):
                  print("enter the position")
                  pos=int(input())
                  obj.deletion_at_middle(pos)
                  obj.display()
                  if(ch==6):
                  obj.deletion_at_end()
                  if(ch==7):
                  obj.display()
