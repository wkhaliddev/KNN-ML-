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
            if (row[1]==test_data[1]):
                    eucledian_dist=0  #taglist matched
            else:
                    eucledian_dist=1
                    
            
            genres=test_data[2].split(',')    #genres is in comma seperated string, converting it in list of genres
            for j in (genres): 
                if j not in row[2]:
                    eucledian_dist+=1

                
                
            eucledian_dist+=((int(row[3])-test_data[3])*(int(row[3])-test_data[3]))     #just squaring eucledian distance, pow was not working

            eucledian_dist=math.sqrt(eucledian_dist) #square root at the end
            
            knn_list.append([eucledian_dist,row[0]]) #adding movies name too
    
    knn_list.sort()
    
    print(knn_list)                

            



knn()



def main():

    knn

main()
