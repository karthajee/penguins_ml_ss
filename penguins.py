import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Display some context as to what this app is
st.title('Scatterplot Visualizer App')
st.write('This app lets users upload a classification dataset', 'Scatterplot of 2 attributes are plotted')

# Get the user inputs
# spec = st.selectbox(label='Which species do you want to plot?', 
#                         options=('Adelie', 'Gentoo', 'Chinstrap'))

# Let user upload the file
user_file = st.file_uploader(label='Pls upload a dataset')
if user_file:    
    df = pd.read_csv(user_file)
    # st.write('[INFO] Inspecting var contents', user_file)
    st.write("Displaying the head...\n", df.head())
else:
    st.warning('No dataset uploaded yet')
    st.stop()

attributes = df.columns.tolist()
x_var = st.selectbox(label='Which attribute do you want to plot on the X-axis?', options=attributes)
y_var = st.selectbox(label='Which attribute do you want to plot on the Y-axis?', options=attributes)

# Filter the dataframe
# df_f = df.loc[df.species == spec]
fig, ax = plt.subplots()
sns.set_style('darkgrid')
sns.scatterplot(df, x = x_var, y = y_var, hue = 'species', ax=ax).set(title = f'Comparing species attributes');

# Plot & display
st.pyplot(fig)