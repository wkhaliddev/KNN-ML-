
#-----------git code-------#

import codecs
import ast

#---------------------------#
import numpy as np
import csv
import math
import json             #to use a function changing string of list of dictionary to only list of dictionary

#For Improved KNN
def movies_data_extract(searchedMovie):
    movie_name=''
    movie_genres=''
    movie_rating=''
    movie_posterpath=''
    movie_description=''
    movie_imdbpath=''   #null initialization
    recommended_movies=[]
    with open('ProcessedFinal2.csv',encoding="utf8") as csv_file:
        csv_reader=csv.reader(csv_file,delimiter=',')
        
    
        for row in csv_reader:
            
            
            if (searchedMovie.upper() in row[2].upper()):
                
                recommended_movies=knn(row)
                
                movie_name,movie_genres,movie_description,movie_rating,movie_posterpath,movie_imdbpath=row_to_return(row)   #caling function to return each valuable information               
                break
    
    return movie_name,movie_genres,movie_rating,movie_description,movie_posterpath,movie_imdbpath,recommended_movies



       


def row_to_return(movie_information_list):
    default_posterpath='https://image.tmdb.org/t/p/original'
    if movie_information_list[0]!="123123":
        poster_path=default_posterpath + movie_information_list[9]    #appending default url path with particaular movies url path 
    else:
        poster_path=movie_information_list[9]
        
    default_imdbpath="https://www.imdb.com/title/"
    imdb_path=default_imdbpath+movie_information_list[1]
    
    movie_genre=''
    Movie_total_genres=ast.literal_eval(movie_information_list[4])
    for genres in Movie_total_genres:       #accessing each dictionary inside total list of dictionaries
        movie_genre+=genres['name']+"|"     #appending single genre to make total set of genres
    
    movie_genre=movie_genre[:-1]            #deleting last "|" just for printing purposes



    return movie_information_list[2],movie_genre,movie_information_list[7],movie_information_list[1],poster_path,imdb_path


#----------------git code---------------#


def sortSecond(val): 
    return val[5] 
def knn(ref_movie):

    knn_list=[]
    Sorted_List=[]
    test_data=ref_movie
    default_posterpath=""
  
    
    eucledian_dist=0
    Genre_TList=[]
    Prod_TList=[]
    genresTest=ast.literal_eval(test_data[4])
    prodTest=ast.literal_eval(test_data[5])
    
    for genre in genresTest:
        Genre_TList.append(genre['name'])
    for prod in prodTest:
        Prod_TList.append(prod['name'])
    
    types_of_encoding=["utf8"]
    for encoding_type in types_of_encoding:
        with codecs.open('ProcessedFinal2.csv',encoding=encoding_type,errors='replace') as csv_file:
            csv_reader=csv.reader(csv_file,delimiter=',')
            for row in csv_reader:
                if(row[0]!=test_data[0]):
                    Genre_DList=[]
                    Prod_DList=[]
                    eucledian_dist=0

                    
                    genresData=ast.literal_eval(row[4])
                    for genre in genresData:
                        Genre_DList.append(genre['name'])
                    for j in (Genre_TList): 
                        if j not in Genre_DList:
                            eucledian_dist+=0.25
                    for l in (Genre_DList): 
                        if l not in Genre_TList:
                            eucledian_dist+=0.15

                    prodData=ast.literal_eval(row[5])
                    for prod in prodData:
                        Prod_DList.append(prod['name'])
                    for prod in (Prod_TList): 
                        if prod not in Prod_DList:
                            eucledian_dist+=1
                    for prod in (Prod_DList): 
                        if prod not in Prod_TList:
                            eucledian_dist+=0.25
                    YearTest=float(test_data[10])*2
                    YearData=float(row[10])*2
                    eucledian_dist+=((YearTest-YearData))*(YearTest-YearData)
                    
                    eucledian_dist=math.sqrt(eucledian_dist) 
                    
                    default_posterpath='https://image.tmdb.org/t/p/original'+row[9]
                    
                    knn_list.append([eucledian_dist,row[2],Genre_DList ,default_posterpath,row[0],row[6]]) 
        knn_list.sort()
 
    
    for x in range(15):
        Sorted_List.append(knn_list[x])
    
    Sorted_List.sort(key = sortSecond,reverse=True)
    print(Sorted_List)
    
    return Sorted_List[:6]



#row-to-return for classic knn as it has different csv files i.e rows are altered



def row_to_return_classic_knn(movie_information_list):
    default_posterpath='https://image.tmdb.org/t/p/original'
    if movie_information_list[0]!="123123":
        poster_path=default_posterpath + movie_information_list[5]    #appending default url path with particaular movies url path 
    else:
        poster_path=movie_information_list[5]
        
    default_imdbpath="https://www.imdb.com/title/"
    imdb_path=default_imdbpath+movie_information_list[1]
    
    movie_genre=''
    Movie_total_genres=ast.literal_eval(movie_information_list[3])
    for genres in Movie_total_genres:       #accessing each dictionary inside total list of dictionaries
        movie_genre+=genres['name']+"|"     #appending single genre to make total set of genres
    
    movie_genre=movie_genre[:-1]            #deleting last "|" just for printing purposes



    return movie_information_list[2],movie_genre,movie_information_list[4],movie_information_list[1],poster_path,imdb_path












#for Classical method i.e. only Euclidean 








def movies_data_extract_classic(counter):
    movie_name=''
    movie_genres=''
    movie_rating=''
    movie_posterpath=''
    movie_description=''
    movie_imdbpath=''   #null initialization
    recommended_movies=[]
    Genre_DList=[]
    eucledian_dist=0
    with open('ClassicDigitalized.csv',encoding="utf8") as csv_file:
        Arr_Digitalized=np.genfromtxt(csv_file,delimiter=',')
        
    
    types_of_encoding=["utf8"]
    for encoding_type in types_of_encoding:
        with codecs.open('ClassicOriginal1.csv',encoding=encoding_type,errors='replace') as csv_file2:
            Arr_Original = csv.reader(csv_file2, delimiter=',')
            NewList=list(Arr_Original)
            print(type(NewList))
            recommeded_raw=KNN_Classic(counter,Arr_Digitalized,NewList)
            Knn_Rec=[]
            #print(recommeded_raw)
            for i in range(7):
                counter_Value=recommeded_raw[i][1]
                if(counter_Value!=counter):
                    Knn_Rec.append([recommeded_raw[i][0],NewList[counter_Value][2],NewList[counter_Value][3],NewList[counter_Value][5],NewList[counter_Value][0]])
            recommeded_raw=Knn_Rec
            print(recommeded_raw)

                        
                        
            for single_movie in recommeded_raw:
                print(single_movie)
                genresData=ast.literal_eval(single_movie[2])
                Genre_DList=[]
                for genre in genresData:
                    Genre_DList.append(genre['name'])
                single_movie[2]=Genre_DList
                single_movie[3]='https://image.tmdb.org/t/p/original'+single_movie[3] 
                   


            recommended_movies=recommeded_raw
           
                
                
            movie_name,movie_genres,movie_rating,movie_description,movie_posterpath,movie_imdbpath=row_to_return_classic_knn(NewList[counter])   #caling function to return each valuable information               
            break
            #break
        recommended_movies.sort() 
        recommended_movies=recommended_movies[:6]   
    print("classic\n",recommended_movies)
    return movie_name,movie_genres,movie_rating,movie_description,movie_posterpath,movie_imdbpath,recommended_movies





def Euclidean(x,y):
            distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip(x, y)]))
            return distance
def KNN_Classic(count,Arr_Digitalized,NewList):
            knn_list=[]
            #Knn_Rec=[]
            test_Cdata=Arr_Digitalized[count]
            counter=0
            for row in Arr_Digitalized:
                knn_list.append([Euclidean(test_Cdata,row),counter])
                counter=counter+1



            knn_list.sort()
            knn_list=knn_list[:7]
            return knn_list



                  # Knn_Rec.append([knn_list[i][0],counter])
            
            #return(Knn_Rec)
            






