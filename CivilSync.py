import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#changehlfe

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)
'You selected: ',add_slider

# Set up the Streamlit app
st.title("Draggable Graph Pointer")

# Create a slider to move the pointer
pointer_value = st.slider("Move the pointer", 0, 10, 5)

# Generate some sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)  # Example function

# Create the plot
fig, ax = plt.subplots()
ax.plot(x, y, label="y = sin(x)")
ax.axvline(pointer_value, color='r', linestyle='--', label=f'Pointer at {pointer_value}')
ax.scatter([pointer_value], [np.sin(pointer_value)], color='red', zorder=3)
ax.legend()
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_title("Graph with Draggable Pointer")

# Display the plot
st.pyplot(fig)

