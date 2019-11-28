from flask import Flask , render_template , request ,flash, url_for, redirect
import knn 
import csv
from knn import knn

#opening scv file
with open("MovieGenre.csv") as csv_file:
    csv_reader=csv.reader(csv_file,delimiter=',')



app=Flask(__name__)
@app.route("/", methods=['GET','POST'])
#@app.route("/index" , methods=['GET','POST'])


def main():
    
    
    if request.method=='POST':
        movie_searched=request.form['searched']
        #flash(movie_searched)  #for printing the submitted value i.e for Debugging
       # return render_template('index.html', movie_name=movie_searched )  
        return render_template("index.html", movie_name=movie_searched)

    else:
        return render_template("index.html")





if __name__=="__main__":
    app.run(debug=True , host="0.0.0.0" , port = 80)