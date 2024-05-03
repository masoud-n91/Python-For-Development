import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from groq import Groq
import os


def data_analyzer(df):

    data = df.values.tolist()

    print(f"data: {data}")

    
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"),)

    sys_prompt =  """
    You are a data analyst.
    Your job is to analyze data and provide insights.
    A dataframe is given below.
    The format of the data is: a list of lists.
    For a dataframe of 3 rows and 3 columns, the format will be: [[row1_col1, row1_col2, row1_col3], [row2_col1, row2_col2, row2_col3], [row3_col1, row3_col2, row3_col3]].
    You will analyze the dataframe and provide some general information about the dataframe.
    Start your sentence with "Let's analyze the provided dataframe!"
    """
    
    chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": sys_prompt,
                },
                {
                    "role": "user",
                    "content": "Dataframe: " + str(df),
                },
            ],
            # model="llama3-8b-8192",
            model="llama3-70b-8192",
            temperature=0.5,
            top_p=1,
            stop=None,
            stream=False,
        )
    
    return chat_completion.choices[0].message.content


def main():
    st.title("Data Science App")
    
    st.sidebar.header("About")
    st.sidebar.write("This is a simple Data Science app built with Streamlit.")
    
    uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
    
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)

        st.sidebar.markdown("---")
        st.sidebar.subheader("Data Information")
        st.sidebar.write(data_analyzer(df))
        
        st.subheader("Dataframe")
        st.write(df)
        
        st.subheader("Chart")

        chart_type = st.selectbox("Select Chart Type", ["Line Chart", "Bar Chart"])

        x_axis = st.selectbox("Select X-axis", df.columns)
        y_options = [col for col in df.columns if col != x_axis]
        y_axis = st.selectbox("Select Y-axis", y_options)
        
        if chart_type == "Line Chart":
            st.line_chart(df.set_index(x_axis)[y_axis])
        elif chart_type == "Bar Chart":
            st.bar_chart(df.set_index(x_axis)[y_axis])

        chart_type2 = st.selectbox("Select Chart Type", ["Pie Chart", "Histogram"])

        option = st.selectbox("Select an option", df.columns)

        if chart_type2 == "Histogram":
            plt.hist(df[option], bins=20)
            st.pyplot(plt)
        elif chart_type2 == "Pie Chart":
            plt.pie(df[option].value_counts(), labels=df[option].unique())
            st.pyplot(plt)
        
if __name__ == "__main__":
    main()
