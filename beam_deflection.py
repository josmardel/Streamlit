import streamlit as st
import numpy as np
import plotly.express as px

# Title and Description
st.title('I-Beam Deflection Calculator')

# Documentation
st.markdown('''
## Documentation

### What Does This App Do?
This app calculates the deflection at the end of a cantilevered I-beam under a uniformly distributed load. It also plots the deflection along the length of the beam.

### How to Use the App
1. **Input Parameters**: Provide the uniformly distributed load (in N/m), length of the beam (in meters), modulus of elasticity of the material (in GPa), and moment of inertia of the I-beam cross-section (in \(m^4\)).
2. **Results**: The app will display the calculated deflection at the end of the beam.
3. **Deflection Plot**: An interactive plot will be shown representing the deflection along the length of the beam. You can zoom, pan, and hover over data points for more information.

### Formulas Used for Calculation
''')

# Display formulas in LaTeX
st.latex(r'\text{The deflection } \delta \text{ at the end of the beam is calculated as:}')
st.latex(r'\delta = \frac{w \cdot L^4}{8 \cdot E \cdot I}')
st.latex(r'\text{The deflection along the length } x \text{ is calculated as:}')
st.latex(r'\text{Deflection at } x = \frac{w \cdot x^2}{6 \cdot E \cdot I} \left( 3L - x \right)')

# User inputs
st.header('Input Parameters')

w = st.number_input('Uniformly Distributed Load (N/m)', min_value=0.0, value=100.0, step=0.1)
L = st.number_input('Length of the Beam (m)', min_value=0.1, value=5.0, step=0.1)
E = st.number_input('Modulus of Elasticity (GPa)', min_value=0.1, value=200.0, step=0.1) * 1e9  # Convert to Pa
I = st.number_input('Moment of Inertia (m^4)', min_value=0.00001, value=0.0001, step=0.00001)

# Calculate deflection at the end
delta = (w * L**4) / (8 * E * I)

st.header('Results')
st.write(f'The deflection at the end of the beam is {delta:.6f} meters.')

# Calculate and plot deflection along the length
x = np.linspace(0, L, 500)
y = (w * x**2) * (3 * L - x) / (6 * E * I)

fig = px.line(x=x, y=y, labels={'x': 'Length Along the Beam (m)', 'y': 'Deflection (m)'}, title='Deflection Along the Length of the I-Beam')
fig.update_layout(
    xaxis_title='Length Along the Beam (m)',
    yaxis_title='Deflection (m)',
    title='Deflection Along the Length of the I-Beam'
)

st.plotly_chart(fig)
