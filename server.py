from flask import Flask , render_template , request ,flash, url_for, redirect
import utility 
import csv




movies={
            'movie_name':'',
            'movie_genres':'',
            'movie_rating':'',
            'movie_description':'',
            'movie_posterpath':'',
            'movie_imdbpath':''
        }

movie_searched="-1"     #default value 

app=Flask(__name__)
@app.route("/")

@app.route("/index" )


def main():
    
   
    movie_searched='-1'       #reinitializing for assurring that main page runs with defalt value                                                                      
    return render_template("index.html",movie_searched=movie_searched)          #movie_searched variable was pass just to see if this page was triggered first time i.e no search earlier
                                                                                #or it is searched earlier but no movie was found according to input search

#when an image of movie is clicked in improve knn
@app.route("/sendbyGet/<movie_id>", methods=['GET'])
def sendbyGet(movie_id):
    
    recommended_movies=[]
    global movies 
    #Part One:Getting Entered Movie's Data
    with open('ProcessedFinal2.csv',encoding="UTF8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if row[0]==movie_id:
                print("row[2]",row[2])
                movies['movie_name'],movies['movie_genres'],movies['movie_description'],movies['movie_rating'],movies['movie_posterpath'],movies['movie_imdbpath']=utility.row_to_return(row)
                recommended_movies=utility.knn(row)
                break
    #End Of Part One

 
    return render_template("result.html", movies=movies, recommended_movies=recommended_movies)




#when image of movie is clicked in classical knn
@app.route("/sendbyGetClassic/<movie_id>", methods=['GET'])
def sendbyGetClassic(movie_id):
    
    recommended_movies=[]
    global movies 
    #Part One:Getting Entered Movie's Data
    with open('ClassicOriginal1.csv',encoding="UTF8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        counter=-1
        for row in csv_reader:
            counter+=1
            if row[0]==movie_id:
                print("row[2]",row[2])
                movies['movie_name'],movies['movie_genres'],movies['movie_rating'],movies['movie_description'],movies['movie_posterpath'],movies['movie_imdbpath'],recommended_movies=utility.movies_data_extract_classic(counter)
                
                break
    #End Of Part One

 
    return render_template("resultClassic.html", movies=movies, recommended_movies=recommended_movies)


#For Improved KNN function i.e routed when Improved KNN button is pressed

@app.route("/result", methods=['POST'])
def result():
    recommended_movies=[]
    global movies,movie_searched           #so that any change here will act as global change
    movie_searched=request.form['searched']     #input from user inside of template
    
    
    movies['movie_name'],movies['movie_genres'],movies['movie_rating'],movies['movie_description'],movies['movie_posterpath'],movies['movie_imdbpath'],recommended_movies=utility.movies_data_extract(movie_searched)
    
    if not movies['movie_name']:       #if movie_name is not found in list neither it is -1 i.e the default value
        
        return render_template("index.html",movie_searched=movie_searched)    


    
    return render_template("result.html", movies=movies, recommended_movies=recommended_movies)



#Now for Classical KNN new route is passed from Classic KNN button
@app.route("/resultClassic", methods=['POST'])
def resultClassic():
    recommended_movies=[]
    global movies,movie_searched           #so that any change here will act as global change
    movie_searched=request.form['searched']     #input from user inside of template
    with open('ClassicOriginal1.csv',encoding="UTF8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        counter=-1
        for row in csv_reader:
            counter+=1
            
            if movie_searched.upper() in row[2].upper():
                
    
    
                movies['movie_name'],movies['movie_genres'],movies['movie_rating'],movies['movie_description'],movies['movie_posterpath'],movies['movie_imdbpath'],recommended_movies=utility.movies_data_extract_classic(counter)
                break
    if not movies['movie_name']:       #if movie_name is not found in list neither it is -1 i.e the default value
        
        return render_template("index.html",movie_searched=movie_searched)    


    
    return render_template("resultClassic.html", movies=movies, recommended_movies=recommended_movies)




if __name__=="__main__":
    app.run(debug=True , host="0.0.0.0" , port = 80)
