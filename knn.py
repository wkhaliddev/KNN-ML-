import csv
import math

def knn():

    knn_list=[]
    test_data=["fault in our stars","titanic","Romantic,Thriller,Fantasy",4]
    eucledian_dist=0
    with open('data.csv') as csv_file:
        csv_reader=csv.reader(csv_file,delimiter=',')
        for row in csv_reader:
            eucledian_dist=0
            if (row[1]==test_data):
                    eucledian_dist=0
            else:
                    eucledian_dist=1
            print(eucledian_dist)        
            
                
            for j in (test_data[2]): 
                if j not in row[2]:
                    eucledian_dist+=1

            for i in range(3,4):    
                
                eucledian_dist+=((int(row[i])-test_data[i])*(int(row[i])-test_data[i]))

            eucledian_dist=math.sqrt(eucledian_dist)
            
            knn_list.append([eucledian_dist,row[0]])
    
    knn_list.sort()
    
    print(knn_list)                

            



knn()



def main():

    knn

main()