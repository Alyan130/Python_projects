import pandas as pd
import streamlit as st
import os
from io import BytesIO

st.set_page_config(page_title="📳 Data sweeper", layout='wide')
st.title("_Data_ :blue[_Sweeper_]")
st.write("Transform your files betwen CSV and Excel formats with built-in data cleaning and visualization 🎇")
upload_files=st.file_uploader("Upload your files [CSV or Excel]:",type=["csv","xlsx"] ,accept_multiple_files=True)

if upload_files:
    for file in upload_files:
        file_ext= os.path.splitext(file.name)[-1].lower()

        if file_ext==".csv":
          df=pd.read_csv(file)
        elif file_ext==".xlsx":
          df= pd.read_excel(file)
        else:
          st.error(f"Unsupported file type:{file_ext}")
          continue

        st.write(f"file name : :blue[{file.name}]")
        st.write(f"file size : :blue[{file.size/1024}kb]")

        st.markdown(
         "<style>div.block-container {padding-top: 50px;}</style>",
         unsafe_allow_html=True
        )

        st.write("Preview five rows of Data frame")
        st.write(df.head())



        st.markdown(
         "<style>div.block-container {padding-top: 50px;}</style>",
         unsafe_allow_html=True
        )

        st.subheader("Data cleaning options")
        if st.checkbox(f"clean data for {file.name}"):
           col1, col2 = st.columns(2)

           with col1:
              if st.button(f"Remove duplicates from {file.name}"):
                 df.drop_duplicates(inplace=True)
                 st.write("Duplicates Removed!")
            
           with col2:
             if st.button(f"Fill missing values frm {file.name}"):
                numeric_cols = df.select_dtypes(include=["number"]).columns
                df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                st.write("Missing values have been filled!")


        st.subheader("Select columns to convert")
        columns = st.multiselect(f"Choose columns for {file.name}", df.columns, default=df.columns)
        df=df[columns]

        st.markdown(
         "<style>div.block-container {padding-top: 50px;}</style>",
         unsafe_allow_html=True
        )

        st.subheader("Data :red[Visualization] 📉")
        if st.checkbox(f"Show visualization for {file.name}"):
           st.bar_chart(df.select_dtypes(include=["number"]).iloc[:,:2])
 
 
        st.markdown(
         "<style>div.block-container {padding-top: 50px;}</style>",
         unsafe_allow_html=True
        )


        st.subheader("File Conversion")
        conversion= st.radio(f"Convert {file.name} to: ",["CSV","Excel"], key=file.name)
        if st.button(f"Convert {file.name}"):
           buffer= BytesIO()

           if conversion == "CSV":
              df.to_csv(buffer,index=False)
              file_nmae= file.name.replace(file_ext,".csv")
              mime_type="text/csv"

           elif conversion == "Excel":
              df.to_excel(buffer,index=False)
              file_nmae= file.name.replace(file_ext,".xlsx")
              mime_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
              buffer.seek(0)

           st.download_button(
              label=f"Download {file.name} as {conversion}", 
              data=buffer , 
              file_name=file_nmae,
              mime=mime_type 
              )
           

        st.html("""
         <div style="width:30vw; position:relative; bottom:0px; margin-top:20px; padding:10px;    background-color:#232429; border-radius:10px;">
        <p style="color:white; font-size:15px;">Developed by Alyan Ali</p>
        <p style="color:white; font-size:15px;">LinkedIn: 
            <a href="https://www.linkedin.com/in/alyan-ali-560910268/" target="_blank" style="color: #1DA1F2; text-decoration: none;">Check now</a>
        </p>
       </div>
         """)
