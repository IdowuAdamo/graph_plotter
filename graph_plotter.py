import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

st.title("📊 Simple Data Plotter")
st.write("Enter your data manually and create plots!")

# Chart type definitions
chart_definitions = {
    "Pie Chart": "A pie chart displays data in a circular graph where each slice represents a proportion of the whole.",
    "Line Chart": "Line charts show trends over time by connecting data points with lines.",
    "Bar Chart": "Bar charts are used to compare quantities across different categories using rectangular bars.",
    "Histogram": "Histograms show the frequency distribution of a dataset, dividing data into bins.",
    "Scatter Plot": "Scatter plots are used to observe relationships between two numerical variables."
}

# Chart type selection
chart_type = st.selectbox(
    "Select Chart Type",
    list(chart_definitions.keys())
)

if chart_type == "Pie Chart":
    st.subheader("Pie Chart Input")
    st.write(chart_definitions[chart_type])
    labels = st.text_input("Enter labels (comma-separated)", "A, B, C")
    values = st.text_input("Enter values (comma-separated)", "30, 40, 30")
    
    if st.button("Generate Pie Chart"):
        labels_list = [x.strip() for x in labels.split(",")]
        values_list = [float(x.strip()) for x in values.split(",")]
        
        if len(labels_list) != len(values_list):
            st.error("The number of labels must match the number of values.")
        else:
            df = pd.DataFrame({'Category': labels_list, 'Value': values_list})
            st.write("Your Data:")
            st.write(df)
            
            fig = px.pie(
                values=values_list,
                names=labels_list,
                title="Pie Chart"
            )
            st.plotly_chart(fig)

elif chart_type == "Line Chart":
    st.subheader("Line Chart Input")
    st.write(chart_definitions[chart_type])
    x_values = st.text_input("Enter X values (comma-separated)", "1, 2, 3, 4, 5")
    y_values = st.text_input("Enter Y values (comma-separated)", "2, 4, 6, 8, 10")
    
    if st.button("Generate Line Chart"):
        x = [float(x.strip()) for x in x_values.split(",")]
        y = [float(y.strip()) for y in y_values.split(",")]
        
        if len(x) != len(y):
            st.error("The number of X values must match the number of Y values.")
        else:
            df = pd.DataFrame({'X': x, 'Y': y})
            st.write("Your Data:")
            st.write(df)
            
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=x, y=y, mode='lines+markers'))
            fig.update_layout(
                title="Line Chart",
                xaxis_title="X",
                yaxis_title="Y",
                xaxis=dict(showgrid=True),
                yaxis=dict(showgrid=True)
            )
            st.plotly_chart(fig)

elif chart_type == "Bar Chart":
    st.subheader("Bar Chart Input")
    st.write(chart_definitions[chart_type])
    labels = st.text_input("Enter labels (comma-separated)", "A, B, C, D")
    values = st.text_input("Enter values (comma-separated)", "20, 35, 25, 40")
    
    if st.button("Generate Bar Chart"):
        labels_list = [x.strip() for x in labels.split(",")]
        values_list = [float(x.strip()) for x in values.split(",")]
        
        if len(labels_list) != len(values_list):
            st.error("The number of labels must match the number of values.")
        else:
            df = pd.DataFrame({'Category': labels_list, 'Value': values_list})
            st.write("Your Data:")
            st.write(df)
            
            fig = go.Figure()
            fig.add_trace(go.Bar(x=labels_list, y=values_list))
            fig.update_layout(
                title="Bar Chart",
                xaxis_title="Categories",
                yaxis_title="Values",
                yaxis=dict(showgrid=True)
            )
            st.plotly_chart(fig)

elif chart_type == "Histogram":
    st.subheader("Histogram Input")
    st.write(chart_definitions[chart_type])
    values = st.text_input("Enter values (comma-separated)", "1, 2, 2, 3, 3, 3, 4, 4, 5")
    bins = st.slider("Number of bins", 5, 20, 10)
    
    if st.button("Generate Histogram"):
        values_list = [float(x.strip()) for x in values.split(",")]
        
        df = pd.DataFrame({'Value': values_list})
        st.write("Your Data:")
        st.write(df)
        
        fig = go.Figure()
        fig.add_trace(go.Histogram(x=values_list, nbinsx=bins))
        fig.update_layout(
            title="Histogram",
            xaxis_title="Values",
            yaxis_title="Frequency",
            yaxis=dict(showgrid=True)
        )
        st.plotly_chart(fig)

elif chart_type == "Scatter Plot":
    st.subheader("Scatter Plot Input")
    st.write(chart_definitions[chart_type])
    x_values = st.text_input("Enter X values (comma-separated)", "1, 2, 3, 4, 5")
    y_values = st.text_input("Enter Y values (comma-separated)", "2, 4, 5, 4, 5")
    
    if st.button("Generate Scatter Plot"):
        x = [float(x.strip()) for x in x_values.split(",")]
        y = [float(y.strip()) for y in y_values.split(",")]
        
        if len(x) != len(y):
            st.error("The number of X values must match the number of Y values.")
        else:
            df = pd.DataFrame({'X': x, 'Y': y})
            st.write("Your Data:")
            st.write(df)
            
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=x, y=y, mode='markers'))
            fig.update_layout(
                title="Scatter Plot",
                xaxis_title="X",
                yaxis_title="Y",
                xaxis=dict(showgrid=True),
                yaxis=dict(showgrid=True)
            )
            st.plotly_chart(fig)

# Add some basic instructions
st.markdown("""
### Instructions:
1. Select the type of chart you want to create
2. Enter your data as comma-separated values
3. Click the 'Generate' button to create the plot
""")