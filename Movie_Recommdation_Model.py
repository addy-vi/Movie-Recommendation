import numpy as np
import pandas as pd
import streamlit as st
from joblib import load
import difflib

similarity=load(r"C:\Users\haider\Desktop\New folder (3)\movie_similarity.joblib")
data=pd.read_csv(r"C:\Users\haider\Desktop\New folder (3)\movies.csv")
new_data=data.fillna("")
title_movies=new_data["title"].tolist()

if __name__=="__main__":

    st.title("Movie Recommendatoin System")
    movie_name=st.text_input("Enter your Favourite movie name:")
    
    if st.button("Click for recommendation"):
        similar_movie_name=difflib.get_close_matches(movie_name,title_movies)
        
        if similar_movie_name:
            closer_match_movie=similar_movie_name[0]

            movie_name_index=new_data.loc[new_data["title"]==closer_match_movie].index[0]
            similarity_score=list(enumerate(similarity[movie_name_index]))
            sorted_similarity_score=sorted(similarity_score,key=lambda x:x[1], reverse=True)

            i=1
            for movie in sorted_similarity_score:
                a=movie[0]
                recommended_movie_name=new_data.loc[new_data.index==a]["title"].values[0]
                if i<=10:
                    st.write(i,".",recommended_movie_name)
                    i+=1
            st.success("Thanks for using ours System \nHope you like these movies....")
        

