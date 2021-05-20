

class Dynamic_Array:
    #we create a null(all elements are 0) three dimensional array with given dimensions
    def __init__(self,length=0,width=0,depth=0):
        self.length=length
        self.width=width
        self.depth=depth

        self.Arr=[[[0 for k in range(self.depth)] for j in range(self.width)] for i in range(self.length)]
     
    #we print the dimensions of our array   
    def get_dimensions(self):
        print('length=',self.length)
        print('width=',self.width)
        print('depth=',self.depth)
   
        #we print the elements of our array
    def get_Array(self):
        print('Elements of Array=',self.Arr)

    #we replace the zero elemenent from the given position 
    def insert_element(self,l,w,d,element): 
        self.Arr[l][w][d]=element
    
        # we acces an element through its position
    def access_element(self,l,w,d):
        if l<0 or w<0 or d<0 or l>=self.length or w>=self.width or d>=self.depth:
                print("Given position is out of bound")
        else:  
                  #self.Arr[l][w][d]=512
                return self.Arr[l][w][d]
  
           #we change the dimensions of the array with new ones
    def change_dimensions(self,new_length,new_width,new_depth): 
        #we use a temporary array who has the new dimensions to initialize the elements with zero
        New_Arr=[[[0 for k in range(new_depth)] for j in range(new_width)] for i in range(new_length)]

   
    #we will add  our elements from the array who has the old dimensions 
    #if a new dimension is bigger than the old one we will add all elements and the remaining elements will be 0
    #else if a new dimension is smaller than the old one we will add elements until the new capacity is full(we cannot add all elments)  
    #so we have to find the minimum from the new dimensions and old dimensions to know until where  to add the elements   
        for i in range (min(new_length,self.length)):
          for j in range (min(new_width,self.width)):
             for k in range (min(new_depth,self.depth)):
                  New_Arr[i][j][k]=self.Arr[i][j][k]
        #we replace our dimensions with the new ones         
        self.Arr=New_Arr
        self.length=new_length
        self.width=new_width
        self.depth=new_depth
    

    
  #we add elements of two arrays
def Add_two_arrays(Arr1,Arr2):
     #to add two arrays I thought that the best way to do that is to create a new array with maximum dimensions
     #between the two ones(maximum lenght,width,depth).So we can save all the additions and the elements not added
     #due to the different sizes between the two arrays
    Arr3=Dynamic_Array(max(Arr1.length,Arr2.length),max(Arr1.width,Arr2.width),max(Arr1.depth,Arr2.depth))
    
  
    Arr1.change_dimensions(Arr3.length,Arr3.width,Arr3.depth)
    Arr2.change_dimensions(Arr3.length,Arr3.width,Arr3.depth)
    
    
    for i in range (Arr3.length) :
        for j in range (Arr3.width):
            for k in range (Arr3.depth):
                    Arr3.Arr[i][j][k]=Arr1.Arr[i][j][k]+Arr2.Arr[i][j][k]
    return Arr3.Arr

#we subtract elements of two arrays
def Substract_two_arrays(Arr1,Arr2):
     #just like adding but subtracting the second from the first array
    Arr3=Dynamic_Array(max(Arr1.length,Arr2.length),max(Arr1.width,Arr2.width),max(Arr1.depth,Arr2.depth))
    
  
    Arr1.change_dimensions(Arr3.length,Arr3.width,Arr3.depth)
    Arr2.change_dimensions(Arr3.length,Arr3.width,Arr3.depth)
    
    
    for i in range (Arr3.length) :
        for j in range (Arr3.width):
            for k in range (Arr3.depth):
                    Arr3.Arr[i][j][k]=Arr1.Arr[i][j][k]-Arr2.Arr[i][j][k]
    return Arr3.Arr 
  
   





Array1=Dynamic_Array(3,2,1)
print("Dimensions of first Array:")
Array1.get_dimensions()
print("No.of elements in first Array=",Array1.length*Array1.width*Array1.depth)
print("Give elements of first Array:")
# we refill(initially the array is a null array) the array with given elements from the keyboard,the elements has the float type(real numbers)
for i in range (Array1.length):
      for j in range (Array1.width):
            for k in range (Array1.depth):
                t_elem=input('Element=')
                elem=float(t_elem)
                Array1.insert_element(i,j,k,elem)

Array1.get_Array()
print('Accessed Element through its position=',Array1.access_element(0,0,0))
print("Changing dimensions of first Array:")
Array1.change_dimensions(1,2,1)
Array1.get_dimensions()
Array1.get_Array()



Array2=Dynamic_Array(2,2,1)
print("Dimensions of second Array:")
Array2.get_dimensions()
print("No. of elements in second Array=",(Array2.length*Array2.width*Array2.depth))
print("Give elements of second Array:")
for i in range (Array2.length):
      for j in range (Array2.width):
            for k in range (Array2.depth):
                t_elem=input('Element=')
                elem=float(t_elem)
                Array2.insert_element(i,j,k,elem)
Array2.get_Array()

print('Adding the elements of the two arrays=',Add_two_arrays(Array1,Array2))
print('Substracting the elements of the two arrays=',Substract_two_arrays(Array2,Array1))