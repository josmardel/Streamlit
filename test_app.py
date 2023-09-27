import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Title and description
st.title('I-Beam Deflection Calculator')
st.write('This app calculates the deflection at the end of an I-beam and plots the deflection along the length of the beam.')

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

plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Deflection Curve')
plt.xlabel('Length Along the Beam (m)')
plt.ylabel('Deflection (m)')
plt.title('Deflection Along the Length of the I-Beam')
plt.grid(True)
plt.legend()

st.pyplot(plt)

