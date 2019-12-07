import csv
import math
import codecs
import ast
def sortSecond(val): 
    return val[2] 
def knn():

    knn_list=[]
    Sorted_List=[]
    test_data=[770,'tt0031381','Gone with the Wind',1939,"[{'id': 18, 'name': 'Drama'}, {'id': 10749, 'name': 'Romance'}, {'id': 10752, 'name': 'War'}]","[{'name': 'Selznick International Pictures', 'id': 1553}, {'name': 'Metro-Goldwyn-Mayer (MGM)', 'id': 8411}]",7.618957752254195,"An American classic in which a manipulative woman and a roguish man carry on a turbulent love affair in the American south during the Civil War and Reconstruction.",1939-12-15,'/4o1yeosjSFMaI9pe1rOkYcZ6hHO.jpg',0.4452054794520548
]
    #test_data=[389,'tt0050083','12 Angry Men',1957,"[{'id': 18, 'name': 'Drama'}]","[{'name': 'United Artists', 'id': 60}, {'name': 'Orion-Nova Productions', 'id': 10212}]",8.153591909848416,"The defense and the prosecution have rested and the jury is filing into the jury room to decide if a young Spanish-American is guilty or innocent of murdering his father. What begins as an open and shut case soon becomes a mini-drama of each of the jurors' prejudices and preconceptions about the trial, the accused, and each other.",1957-0-25,'/3W0v956XxSG5xgm7LB6qu8ExYJ2.jpg',0.5684931506849316]
    #test_data=[9603,'tt0112697','Clueless',1995,"[{'id': 35, 'name': 'Comedy'}, {'id': 18, 'name': 'Drama'}, {'id': 10749, 'name': 'Romance'}]","[{'name': 'Paramount Pictures', 'id': 4}]",6.834793145795854,"Shallow, rich and socially successful Cher is at the top of her Beverly Hills high school's pecking scale. Seeing herself as a matchmaker, Cher first coaxes two teachers into dating each other. Emboldened by her success, she decides to give hopelessly klutzy new student Tai a makeover. When Tai becomes more popular than she is, Cher realizes that her disapproving ex-stepbrother was right about how misguided she was -- and falls for him.",1995-0-19,'/i8gEHh2sszB6YWLC0jl559sxAeN.jpg,0.8287671232876712']

    #test_data=[862,'tt0114709','Toy Story',1995,"[{'id': 16, 'name': 'Animation'}, {'id': 35, 'name': 'Comedy'}, {'id': 10751, 'name': 'Family'}]","[{'name': 'Pixar Animation Studios', 'id': 3}]",7.684683758682903,"Led by Woody, Andy's toys live happily in his room until Andy's birthday brings Buzz Lightyear onto the scene. Afraid of losing his place in Andy's heart, Woody plots against Buzz. But when circumstances separate Buzz and Woody from their owner, the duo eventually learns to put aside their differences.",1995-10-30,'/rhIRbceoE9lR4veEXuwCC2wARtG.jpg',0.8287671232876712]
    #test_data=[8844,'tt0113497','Jumanji',1995,"[{'id': 12, 'name': 'Adventure'}, {'id': 14, 'name': 'Fantasy'}, {'id': 10751, 'name': 'Family'}]","[{'name': 'TriStar Pictures', 'id': 559}, {'name': 'Teitler Film', 'id': 2550}, {'name': 'Interscope Communications', 'id': 10201}]",6.877012452950091,"When siblings Judy and Peter discover an enchanted board game that opens the door to a magical world, they unwittingly invite Alan -- an adult who's been trapped inside the game for 26 years -- into their living room. Alan's only hope for freedom is to finish the game, which proves risky as all three find themselves running from giant rhinoceroses, evil monkeys and other terrifying creatures.",1995-12-15,'/vzmL6fP7aPKNKPRTFnZmiUfciyV.jpg']
    #xmax=2019
    #test_data=[24428,'tt0848228','The Avengers',2012,"[{'id': 878, 'name': 'Science Fiction'}, {'id': 28, 'name': 'Action'}, {'id': 12, 'name': 'Adventure'}]","[{'name': 'Paramount Pictures', 'id': 4}, {'name': 'Marvel Studios', 'id': 420}]",7.393911631476678,"When an unexpected enemy emerges and threatens global safety and security, Nick Fury, director of the international peacekeeping agency known as S.H.I.E.L.D., finds himself in need of a team to pull the world back from the brink of disaster. Spanning the globe, a daring recruitment effort begins!",2012-0-25,'/cezWGskPY5x7GaglTTRN4Fugfb8.jpg',0.9452054794520548]

    #xmin=1900
    #test_data=[414,'tt0112462','Batman Forever',1995,"[{'id': 28, 'name': 'Action'}, {'id': 80, 'name': 'Crime'}, {'id': 14, 'name': 'Fantasy'}]","[{'name': 'Warner Bros.', 'id': 6194}, {'name': 'Polygram Filmed Entertainment', 'id': 31080}]",5.200976013313185,"The Dark Knight of Gotham City confronts a dastardly duo: Two-Face and the Riddler. Formerly District Attorney Harvey Dent, Two-Face believes Batman caused the courtroom accident which left him disfigured on one side. And Edward Nygma, computer-genius and former employee of millionaire Bruce Wayne, is out to get the philanthropist; as The Riddler. Former circus acrobat Dick Grayson, his family killed by Two-Face, becomes Wayne's ward and Batman's new partner Robin.",1995-0-16,'/eTMrHEhlFPHNxpqGwpGGTdAa0xV.jpg',0.8287671232876712]

    #scaled_Test=(test_data[4]-xmin)/(xmax-xmin)
    
    eucledian_dist=0
    Genre_TList=[]
    Prod_TList=[]
    genresTest=ast.literal_eval(test_data[4])
    prodTest=ast.literal_eval(test_data[5])
    i=0
    for genre in genresTest:
        Genre_TList.append(genre['name'])
    for prod in prodTest:
        Prod_TList.append(prod['name'])
    
    types_of_encoding=["utf8"]
    for encoding_type in types_of_encoding:
        with codecs.open('MoviesData.csv',encoding=encoding_type,errors='replace') as csv_file:
            csv_reader=csv.reader(csv_file,delimiter=',')
            for row in csv_reader:
                if(row[2]!=test_data[2]):
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
                    YearTest=float(test_data[10])
                    YearData=float(row[10])
                    eucledian_dist+=((YearTest-YearData))*(YearTest-YearData)*2
                    
                    eucledian_dist=math.sqrt(eucledian_dist) 
                    knn_list.append([eucledian_dist,row[2],row[6]]) 
        knn_list.sort()
 
    
    for x in range(15):
        Sorted_List.append(knn_list[x])
    
    Sorted_List.sort(key = sortSecond,reverse=True)
    print("hello")
    print(Sorted_List)
    print("hello")

knn()

def main():

    knn

main()
