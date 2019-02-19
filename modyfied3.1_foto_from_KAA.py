"""  coded by Dvoretsky Vasily
     mail:  vasya.dvoretsky@yandex.ru
 """    
"""importing required libraries """
import cv2                                   #library of computer vision
import numpy as np                           #library of math
from mpl_toolkits.mplot3d import Axes3D      #library for plots
import matplotlib.pyplot as plt              # -||-
import matplotlib                            # -||-


"""importing the image"""
""" IMAGES FOR WORK 

circles04.jpg - small picture to try the parameters 
circles3      - big (1076) picture to show contrasting of an images

"""
  
"""opening an image for work"""
img = cv2.imread('circles04.jpg',3) 
#imshow(img)
cv2.circle(img, (22,22),10, (200,200,80), -1)


#"""drawing a circle of certain size """
#cv2.circle(img, (22,22),21, (200,200,80), -1)           
"""converting of the image into grayscale """
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#cv2.imshow('circles', gray )  
                     
"""cv.HOUGH_GRADIENT is one of the Detection method to use
Python: cv2.HoughCircles(image, method, dp, minDist[, circles[, param1[, param2[, minRadius[, maxRadius]]]]]) → circles
    Parameters:	
    ---image – 8-bit, single-channel, grayscale input image.
    
    ---circles – Output vector of found circles. 
    Each vector is encoded as a 3-element floating-point vector (x, y, radius) .

    ---circle_storage – In C function this is a memory storage that will contain
    the output sequence of found circles.

    ---method – Detection method to use. Currently, the only implemented method 
    is CV_HOUGH_GRADIENT , which is basically 21HT , described in [Yuen12.50].

    ---dp – Inverse ratio of the accumulator resolution to the image resolution.
    For example, if dp=1 , the accumulator has the same resolution as the input image. 
    If dp=2 , the accumulator has half as big width and height.
    
    ---minDist – Minimum distance between the centers of the detected circles.
    If the parameter is too small, multiple neighbor circles may be falsely
    detected in addition to a true one. If it is too large, some circles may be missed.
    
    ---param1 – First method-specific parameter. In case of CV_HOUGH_GRADIENT , 
    it is the higher threshold of the two passed to the Canny() edge detector 
    (the lower one is twice smaller).
    
    ---param2 – Second method-specific parameter. In case of CV_HOUGH_GRADIENT ,
    it is the accumulator threshold for the circle centers at the detection stage.
    The smaller it is, the more false circles may be detected.
    Circles, corresponding to the larger accumulator values, will be returned first.
    
    ---minRadius – Minimum circle radius.
    
    ---maxRadius – Maximum circle radius.
    
"""
image_to_work_with = gray
#method = cv2.HOUGH_GRADIENT
#dp=1
#minDist=7
#param1=7
#param2=14
#minRadius=7
#maxRadius=15

"""Applying Hough algorithm to the image"""
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1,33,param1=2,param2=15,minRadius=15,maxRadius=20)
print("  [X   ],[Y   ],[R  ]")
print( circles)


"""определение среднего радиуса"""

n = 0  
r_sum = 0
for i in range(np.shape(circles)[1]):
    r_sum = r_sum + circles[0][i][2]
    n=n+1
#print("кол-во шаров",n)    
R = np.int64(r_sum/n )
print("Средний радиус",R)

"""A bit of  information for people without without telepathic abilities  XD
#   circles is a three-dimensional array of ([[[x1, y1,r1]
                                               [x2, y2,r2]
                                               ..........
                                               [xn,yn,rn]]])
    
#   it can be represented as              ([[[i[0][ 0 ][0],i[0][ 0 ][1],i[0][ 0 ][2]]
                                             [i[0][ 1 ][0],i[0][ 1 ][1],i[0][ 1 ][2]]
                                              ........................................
                                             [i[0][n-1][0],i[0][n-1][1],i[0][n-1][2]]]])
#   
#            n is a number of found by hough algorithm circles
#       to decreaze the dimensions of an array i use ...
#       array = array[0]
#       it converts the array into         ([[[i[ 0 ][0],i[ 0 ][1],i[ 0 ][2]]
                                              [i[ 1 ][0],i[ 1 ][1],i[ 1 ][2]]
                                              ........................................
                                              [i[n-1][0],i[n-1][1],i[n-1][2]]]])
#        thus shortening the length of the request 
#

"""


"""wrшtes number of circles, uses original matrix named circles"""

height, width = img.shape[:2]    #defining the parameters of chosen image
img_mesh      = np.zeros((height, width,3), np.uint8)  # new picture for mesh
img_number    = img.copy() #making copies for monitoring images  Number of circle
img_found     = img.copy() #making copies for monitoring images  Drawing found circles om image
img_found_4R  = img.copy() #making copies for monitoring images  Drawing found circles and 4R-circles om image
img_KNN       = img.copy() #making copies for monitoring images  Drawing number of neighbour circles

""" Piece where number,found and found4R images are filled"""
Number_of_circles=0
font = cv2.FONT_HERSHEY_SIMPLEX    #initializing one of fonts
for i in circles[0,:]:
    #Black bold text as a background
    cv2.putText(img_number,str(Number_of_circles),(int(i[0]-5),int(i[1]+8)),font, 0.6,(255,255,255),2,cv2.LINE_AA)
    #white thin text 
    cv2.putText(img_number,str(Number_of_circles),(int(i[0]-5),int(i[1]+8)),font, 0.6,(0  ,0  ,0  ),1,cv2.LINE_AA)
    #writing radiuses of found circles
    cv2.putText(img_found,str(i[2]),(int(i[0]-5),int(i[1]+8)),font, 0.6,(0  ,0  ,0  ),1,cv2.LINE_AA)
    
    #drawing circles
    cv2.circle(img_found,(i[0],i[1]),i[2],(0,255,0),2)
    #drawing centers of circles
    cv2.circle(img_found,(i[0],i[1]),2,(0,0,255),3)
    
    #drawing 4R-circles
    cv2.circle(img_found_4R,(i[0],i[1]),4*R,(160,50,200),2)
    #drawing circles
    cv2.circle(img_found_4R,(i[0],i[1]),i[2],(0,255,0),2)
    #drawing centers of circles
    cv2.circle(img_found_4R,(i[0],i[1]),2,(0,0,255),3)
    #adding a number of circle
    Number_of_circles=Number_of_circles+1
    
    

"""A piece where LAB algorithms are defined """
original_array = circles   
or_a = original_array[0]   # decreasing dimencion of an array 

#
#def Lenght(i,datatype):     #datatype = int or float
#    
#    new_arrayLenght = np.empty([np.int_(np.shape(original_array)[1]*(np.shape(original_array)[1]-1)/2), 1],dtype=datatype)  # НО МОЖНО И float
#    k=0
#    for i in range(np.shape(original_array)[1]-1):
#        for j in range(1,np.shape(original_array)[1]):
#            if j<i or j==i:
##                print("пропускаем",i,j)
#                j=j+1
#            else:
##            print("берём",i,j)
#                new_arrayLenght[k] = np.sqrt((or_a[i][0]- or_a[j][0])**2 + (or_a[i][1]- or_a[j][1])**2 )
##                print("берём",i,j,new_array[i])
#                k=k+1
#                j=j+1
##        continue
#    return  new_arrayLenght
#
#
#def Alfa(i,datatype):    #datatype = int or float
#    new_arrayAlfa = np.empty([np.int_(np.shape(original_array)[1]*(np.shape(original_array)[1]-1)/2), 1],dtype=datatype)  # НО МОЖНО И float
#    k1=0
#    for i in range(np.shape(original_array)[1]-1):
#        for j in range(1,np.shape(original_array)[1]):
#            if j<i or j==i:
##                print("пропускаем",i,j)
#                j=j+1
#            else:
##            print("берём",i,j)
#                new_arrayAlfa[k1] = np.rad2deg(np.arctan((or_a[i][1]- or_a[j][1])/(or_a[i][0]- or_a[j][0])))
##                print("берём",i,j,new_array[i])
#                k1=k1+1
#                j=j+1
##        continue
#    return  new_arrayAlfa
#
##___________________________________________________________________________________
#def Betta(i,datatype):   #datatype = int or float
#    new_arrayBetta = np.empty([np.int_(np.shape(original_array)[1]*(np.shape(original_array)[1]-1)/2), 1],dtype=datatype)  # НО МОЖНО И float
#    k2=0
#    for i in range(np.shape(original_array)[1]-1):
#        for j in range(1,np.shape(original_array)[1]):
#            if j<i or j==i:
##                print("пропускаем",i,j)
#                j=j+1
#            else:
##            print("берём",i,j)
#                new_arrayBetta[k2] = or_a[i][1]+ ((or_a[i][1]- or_a[j][1])/(or_a[i][0]- or_a[j][0]))*or_a[i][0] 
##                print("берём",i,j,new_array[i])
#                k2=k2+1
#                j=j+1
##        continue
#    return  new_arrayBetta
#________________________________________________________________


"""radius shoul be between Rmid and sqrt(3)*Rmid""" 
#n = np.size(circles[0]) 
#new_arrayKNN = np.zeros([np.shape(original_array)[1], 2],dtype=float)  # НО МОЖНО И float
##print(new_arrayKNN)
#dx_sqrd=0
#dy_sqrd=0
"""функция квадрата длинны отрезка меж 2 точек """
def d2xy(mat,i,j):
    len = (mat[j][0]-mat[i][0])**2 + (mat[j][1]-mat[i][1])**2
    return len
#"""функция квадратов расстояний по x"""
#def d2y(mat,i,j):
#    return (mat[j][1]-mat[i][1])**2
"""_________________________________________"""
#def Printline(X1,X2,Y1,Y2,N1,N2):
#    Xe = (X1+X2)/2
#    Ye = (Y1+Y2)/2
#    return  cv2.line(img,(X1,Y1),(Xe,Ye),(N1),5)
#cv2.line(img,(Xe,Ye),(X2,Y2),(N2),5)



print("/////////////////////////////")



d, H , W = np.shape(original_array)   #Defining shape of an array 
Mat_w = 5   #Width of matrix
Mat_h = H
matrix     = [[0 for x in range(Mat_w)] for y in range(Mat_h)]
#matrix_x   = [[0 for x in range(1)    ] for y in range(Mat_h)]
matrix_y   = [[0 for x in range(1)    ] for y in range(Mat_h)]
#matrix_knn = [[0 for x in range(1)    ] for y in range(Mat_h)]
for i in range(H):
    for j in range(H):
        if matrix[i][4]<12.5:
            if (i==j) and (j<H) and (i<H):
                print("||| 1         |||",i+1,j+1)
                j=j+1                
            elif (i==j) and (j<H) and (i>=H):
                print("||| 2            |||",i+1,j+1)
                break
            elif (i==j) and (j>=H) :
                print("||| 3            |||",i+1,j+1)
                i=i+1
                j=0
            elif (i!=j) and (d2xy(original_array[0],i,j)< 12.5*(R**2)) and (j<H) and (i>=H):
                print("||| 4            |||",i+1,j+1,"|||+1|||")
#                cv2.line(img,(original_array[0][i][1],original_array[0][i][2]),(original_array[0][j][1],original_array[0][j][2]),(0,0,0),5)
#                cv2.line(img,(circles[0][i][0],circles[0][i][1]),(circles[0][j][0],circles[0][j][1]),(2012.5, 46, 182),3)
                matrix[i][4] = matrix[i][4]+1
                matrix[i][0] = i+1
                matrix[i][1] = original_array[0][i][0]
                matrix[i][2] = original_array[0][i][1]
                matrix[i][3] = original_array[0][i][2]
#                matrix_x[i]=original_array[0][i][0]
                matrix_y[i]=original_array[0][i][2]
#                matrix_knn[i]=matrix[i][4]
            
            
                break
            elif (i!=j) and (d2xy(original_array[0],i,j)< 12.5*(R**2)) and (j<H) and (i<H):
                print("||| 5            |||",i+1,j+1,"|||++1|||")
                matrix[i][4] = matrix[i][4]+1
#                if  matrix[i][4]==6 :
#                cv2.line(mesh,(int(matrix[i][1]),int(matrix[i][2])),((int((matrix[i][1]+matrix[j][1])/2)),int((matrix[i][2]+matrix[j][2])/2)),(2012.5, 46, 182),3)
#            elif  matrix[i][4]==5 :
#                cv2.line(mesh,(int(matrix[i][1]),int(matrix[i][2])),((int((matrix[i][1]+matrix[j][1])/2)),int((matrix[i][2]+matrix[j][2])/2)),(0, 0, 255),3)
#            elif  matrix[i][4]==4 :
#                cv2.line(mesh,(int(matrix[i][1]),int(matrix[i][2])),((int((matrix[i][1]+matrix[j][1])/2)),int((matrix[i][2]+matrix[j][2])/2)),(0, 255, 255),3)
#            elif  matrix[i][4]==3 :
#                cv2.line(mesh,(int(matrix[i][1]),int(matrix[i][2])),((int((matrix[i][1]+matrix[j][1])/2)),int((matrix[i][2]+matrix[j][2])/2)),(255,255,255),3)
#            elif  matrix[i][4]==2 :
#                cv2.line(mesh,(int(matrix[i][1]),int(matrix[i][2])),((int((matrix[i][1]+matrix[j][1])/2)),int((matrix[i][2]+matrix[j][2])/2)),(255, 255,0),3)
#            elif  matrix[i][4]==1 :
#                cv2.line(mesh,(int(matrix[i][1]),int(matrix[i][2])),((int((matrix[i][1]+matrix[j][1])/2)),int((matrix[i][2]+matrix[j][2])/2)),(255, 0, 0),3)

            
#            matrix[i][4] = matrix[i][4]+1
            
                matrix[i][0] = i+1
                matrix[i][1] = original_array[0][i][0]
                matrix[i][2] = original_array[0][i][1]
                matrix[i][3] = original_array[0][i][2]
#                matrix_x[i]=original_array[0][i][0]
                matrix_y[i]=original_array[0][i][2]
#                matrix_knn[i]=matrix[i][4]
                j=j+1
            elif (i!=j) and (d2xy(original_array[0],i,j)< 12.5*(R**2)) and (j>=H):
                print("||| 6            |||",i+1,j+1,"|||+1|||")
#                cv2.line(img,(original_array[0][i][1],original_array[0][i][2]),(original_array[0][j][1],original_array[0][j][2]),(0,0,0),5)
#                cv2.line(img,(circles[0][i][0],circles[0][i][1]),(circles[0][j][0],circles[0][j][1]),(30, 240, 412.5),2)
                matrix[i][4] = matrix[i][4]+1
                matrix[i][0] = i+1
                matrix[i][1] = original_array[0][i][0]
                matrix[i][2] = original_array[0][i][1]
                matrix[i][3] = original_array[0][i][2]
#                matrix_x[i]=original_array[0][i][0]
                matrix_y[i]=original_array[0][i][2]
#                matrix_knn[i]=matrix[i][4]
                i=i+1
                j=0
            elif (i!=j) and (d2xy(original_array[0],i,j)>= 12.5*(R**2)) and (j>=H):
                print("||| 7            |||",i+1,j+1)
                i=i+1
                j=0
            elif (i!=j) and (d2xy(original_array[0],i,j)>= 12.5*(R**2)) and (j<H) and (i<H):
                print("||| 8            |||",i+1,j+1)
                j=j+1
            elif (i!=j) and (d2xy(original_array[0],i,j)>= 12.5*(R**2)) and (j<H) and (i>=H):
                print("||| 12.5            |||",i+1,j+1)
                break
        else:
            print("----------------------------------------------------------------6 ALREADY-----")
            break
#            i=i+1
#for i in range(H):
#    cv2.putText(img_KNN,str(matrix[i][4]),(int(matrix[i][1]-5),int(matrix[i][2]+8)),font, 0.6,(0  ,0  ,0  ),1,cv2.LINE_AA)
#    i=i+1
    
    
for i in range(H):
    cv2.putText(img_KNN,str(matrix[i][4]),(int(matrix[i][1]-5),int(matrix[i][2]+8)),font, 0.6,(0  ,0  ,0  ),1,cv2.LINE_AA)
    for j in range(H):
        if (i==j) and (j<H) and (i<H):
            print("||| 1         |||",i+1,j+1)
            j=j+1                
        elif (i==j) and (j<H) and (i>=H):
            print("||| 2            |||",i+1,j+1)
            break
        elif (i==j) and (j>=H) :
            print("||| 3            |||",i+1,j+1)
            i=i+1
            j=0
        elif (i!=j) and (d2xy(original_array[0],i,j)< 12.5*(R**2)) and (j<H) and (i>=H):
            print("||| 4            |||",i+1,j+1,"|||+1|||")
            break
#            if  matrix[i][4]==6 and matrix[j][4] ==6:
#                cv2.line(mesh,(matrix[i][1],matrix[i][2]),((int(matrix[i][1]+matrix[j][1])/2),(int(matrix[i][2]+matrix[j][2])/2)),(2012.5, 46, 182),3)
        
                
#           
            
        elif (i!=j) and (d2xy(original_array[0],i,j)< 12.5*(R**2)) and (j<H) and (i<H):
            print("||| 5            |||",i+1,j+1,"|||++1|||")
            if  matrix[i][4]==6 :
                cv2.line(img_mesh,(int(matrix[i][1]),int(matrix[i][2])),((int((matrix[i][1]+matrix[j][1])/2)),int((matrix[i][2]+matrix[j][2])/2)),(2012.5, 46, 182),1)
            elif  matrix[i][4]==5 :
                cv2.line(img_mesh,(int(matrix[i][1]),int(matrix[i][2])),((int((matrix[i][1]+matrix[j][1])/2)),int((matrix[i][2]+matrix[j][2])/2)),(0, 0, 255),1)
            elif  matrix[i][4]==4 :
                cv2.line(img_mesh,(int(matrix[i][1]),int(matrix[i][2])),((int((matrix[i][1]+matrix[j][1])/2)),int((matrix[i][2]+matrix[j][2])/2)),(0, 255, 255),1)
            elif  matrix[i][4]==3 :
                cv2.line(img_mesh,(int(matrix[i][1]),int(matrix[i][2])),((int((matrix[i][1]+matrix[j][1])/2)),int((matrix[i][2]+matrix[j][2])/2)),(255,255,255),1)
            elif  matrix[i][4]==2 :
                cv2.line(img_mesh,(int(matrix[i][1]),int(matrix[i][2])),((int((matrix[i][1]+matrix[j][1])/2)),int((matrix[i][2]+matrix[j][2])/2)),(255, 255,0),1)
            elif  matrix[i][4]==1 :
                cv2.line(img_mesh,(int(matrix[i][1]),int(matrix[i][2])),((int((matrix[i][1]+matrix[j][1])/2)),int((matrix[i][2]+matrix[j][2])/2)),(255, 0, 0),1)
            j=j+1 
        elif (i!=j) and (d2xy(original_array[0],i,j)< 12.5*(R**2)) and (j>=H):
            print("||| 6            |||",i+1,j+1,"|||+1|||")
            i=i+1
            j=0
        elif (i!=j) and (d2xy(original_array[0],i,j)>= 12.5*(R**2)) and (j>=H):
            print("||| 7            |||",i+1,j+1)
            i=i+1
            j=0
        elif (i!=j) and (d2xy(original_array[0],i,j)>= 12.5*(R**2)) and (j<H) and (i<H):
            print("||| 8            |||",i+1,j+1)
            j=j+1
        elif (i!=j) and (d2xy(original_array[0],i,j)>= 12.5*(R**2)) and (j<H) and (i>=H):
            print("||| 12.5            |||",i+1,j+1)
            break

#
#cv2.namedWindow('found+4R', cv2.WINDOW_NORMAL)
#cv2.imshow('found+4R',img_found_4R)
#
##cv2.namedWindow('Found', cv2.WINDOW_NORMAL)
##cv2.imshow('Found',img)
#
#cv2.namedWindow('mesh', cv2.WINDOW_NORMAL)
#cv2.imshow('mesh',img_mesh)
#
#cv2.namedWindow('found+4R', cv2.WINDOW_NORMAL)
#cv2.imshow('found+4R',img_found_4R)
#
#cv2.namedWindow('numbered', cv2.WINDOW_NORMAL)
#cv2.imshow('numbered',img_number)
#
#cv2.namedWindow('original', cv2.WINDOW_NORMAL)
#cv2.imshow('original',img)
#cv2.imshow('Found', img_found)

#img_stacked = Image.new('RGB', (2*width,height))
mina = 2*R
maxb = 0           
for i in range(H):
    c=np.min(original_array[0][i][2])
    if mina>c:
#        print("min,c",mina," ",c,"min",mina,"R",R)
        mina=c
#        print("min",mina)
    elif c>maxb:
        maxb=c
#        print("max,c",maxb," ",c,"max",maxb,"R",R)
        
    else:
        i=i+1
#        print("------------")
        
print(" минимальный радиус =",mina) 
print("максимальный радиус =",maxb)       
print("отклонение меньшего от среднеарифметического =",((R-mina)/R)*100,"%")
print("отклонение большего от среднеарифметического =",((maxb-R)/R)*100,"%")
#print(max(a[1]))        
        
        
        
        
        
img_stacked1 = np.concatenate((img     , img_found  , img_found_4R), axis=1)
img_stacked2 = np.concatenate((img_mesh,img_number  , img_KNN     ), axis=1)
img_stacked = np.concatenate((img_stacked1, img_stacked2), axis=0)
cv2.namedWindow('staked', cv2.WINDOW_NORMAL)
cv2.imshow('staked',img_stacked)

cv2.imwrite('out_12.5_F0000012.png', img_stacked)


#matrix_controle = [[0 for x in range(7)    ] for y in range(2)]
#for i in range(7): matrix_controle[0][i] = i
#
##print(matrix_controle) 
#for i in range(H):
#    if   matrix[i][4] ==6:
#        matrix_controle[1][6]= matrix_controle[1][6]+1
#    elif matrix[i][4] ==5:
#        matrix_controle[1][5]= matrix_controle[1][5]+1
#    elif matrix[i][4] ==4:
#        matrix_controle[1][4]= matrix_controle[1][4]+1
#    elif matrix[i][4] ==3:
#        matrix_controle[1][3]= matrix_controle[1][3]+1
#    elif matrix[i][4] ==2:
#        matrix_controle[1][2]= matrix_controle[1][2]+1
#    elif matrix[i][4] ==1:
#        matrix_controle[1][1]= matrix_controle[1][1]+1
#    elif matrix[i][4] ==0:
#        matrix_controle[1][0]= matrix_controle[1][0]+1
#
#for i in range(2):
#    print(matrix_controle[i]) 



print("кол-во шаров",n) 






#    
#print("Betta\n",Betta(or_a,float))
#print("\n")
#print("Alfa\n",Alfa(or_a,float))
#print("\n")
#print("Lenght\n", Lenght(or_a,float))

#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
#
#xs=[Lenght(or_a,float)]
#ys=[Alfa(or_a,float)]
#zs=[Betta(or_a,float)]
#xq=[matrix_x]
#yq=[matrix_y]
#zq=[matrix_knn]

#ax.scatter(xq, yq, zq, c='r', marker='o')
##ax.scatter(xt, yt, zt, c='b', marker='^')
#
#ax.set_xlabel('Длинна вектора (Length)')
#ax.set_ylabel('Угол наклона (Alfa)')
#ax.set_zlabel('Приращение (Betta)')

#plt.show()
#
#
##ax.scatter(xs, ys, zs, c='r', marker='o')
##ax.scatter(xt, yt, zt, c='b', marker='^')
#
#ax.set_xlabel('Длинна вектора (Length)')
#ax.set_ylabel('Угол наклона (Alfa)')
#ax.set_zlabel('Приращение (Betta)')

#plt.show()
#d, H , W = np.shape(original_array)

#    cv2.namedWindow('img_KNN', cv2.WINDOW_NORMAL)
#    cv2.imshow('img_KNN',img_KNN)
    
#    print(matrix[i])
    
 




#print("[N]","[X]","[Y]","[R]","[KNN]")

#for i in range(H):     
#    print(matrix[i])
#    i=i+1

#print(matrix)
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()