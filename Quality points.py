#!/usr/bin/env python
# coding: utf-8

# # programe that scale the quality points of the students 

# In[10]:


average = float(input("Enter the student's average: "))
def qualityPoints(average):
    if average >= 90 and average <= 100:
        print( f'{average} on a 4 scale points is : ',4)
    elif average >= 80 and average <= 89:
        print( f'{average} on a 4 scale points is : ',3)
    elif average >= 70 and average <= 79:
        print( f'{average} on a 4 scale points is : ',2)
    elif average >= 60 and average <= 69:
        print( f'{average} on a 4 scale points is : ',1)
    else:
        print( f'{average} on a 4 scale points is : ',0)
points = qualityPoints(average)
points


# In[ ]:




