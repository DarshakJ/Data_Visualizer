import streamlit as st
import pandas as pd
import numpy as np
from utils import *

# 1. Enhanced Transformation Function
def transform_input(user_query):
    query = user_query.lower()
    # api_output = {'output': {'GenderCode': ['Female', 'Male'], 'GenderCount': [1682, 1318]}, 'graph_type': 'pie', 'title': 'Employee Gender Distribution'}
    api_output = call_adk_agent(user_query)
    print(api_output)
    data = api_output["output"]
    print("data ",data)
    # Common sample data for charts
    df = pd.DataFrame(data).set_index([i for i in data][0])
    title = api_output['title']
    # Routing logic based on user input
    if "bar" in query:
        return {"format": "bar", "results": df, "title": title}
    elif "line" in query:
        return {"format": "line", "results": df, "title": title}
    elif "area" in query:
        return {"format": "area", "results": df, "title": title}
    elif "pie" in query:
        # Streamlit doesn't have a native st.pie_chart, so we use a small helper
        return {"format": "pie", "results": df, "title": title}
    elif "table" in query:
        return {"format": "table", "results": df.reset_index()}
    else:
        return {"format": "bar", "results": df, "title": title}

# 2. Streamlit UI
st.title("📊 SQ-Auto Graph ")

user_input = st.text_input("")

if user_input:
    output = transform_input(user_input)
    fmt = output["format"]
    data = output["results"]
    title = output["title"]

    st.subheader(f"Displaying: {title.upper()}")

    # 3. Multi-Chart Rendering Logic
    if fmt == "bar":
        st.bar_chart(data)
        
    elif fmt == "line":
        st.line_chart(data)
        
    elif fmt == "area":
        st.area_chart(data)
        
    elif fmt == "pie":
        # Since Streamlit lacks st.pie_chart, we use a quick Matplotlib plot
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(figsize=(1,1))
        print("data :",data)
        ax.pie(data[data.columns[-1]], labels=data.index, autopct='%1.1f%%',  radius=0.6,startangle=90, textprops={'fontsize': 3})
        ax.axis('equal') 
        st.pyplot(fig)

    elif fmt == "table":
        st.dataframe(data, use_container_width=True)

    elif fmt == "text":
        st.write(data)