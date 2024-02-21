import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def calculate_traversal_time(stroke_length, max_speed, motor_power):
    # Assuming a simple relation for acceleration based on motor power
    # This is a placeholder and should be adjusted based on actual motor characteristics
    acceleration = motor_power * 10  # Placeholder formula

    # Calculate distance for acceleration and deceleration phases
    d_accel = max_speed**2 / (2 * acceleration)

    if 2 * d_accel < stroke_length:
        # Maximum speed is reached
        d_constant = stroke_length - 2 * d_accel
        t_accel = max_speed / acceleration
        t_constant = d_constant / max_speed
        t_decel = t_accel
        total_time = t_accel + t_constant + t_decel
    else:
        # Maximum speed is not reached
        t_accel = (2 * stroke_length / acceleration)**0.5
        total_time = 2 * t_accel

    return total_time, acceleration

def plot_motion_profile(stroke_length, max_speed, total_time, acceleration):
    t = np.linspace(0, total_time, 500)
    d = np.minimum(0.5 * acceleration * t**2, stroke_length)
    d = np.minimum(d, stroke_length - 0.5 * acceleration * (total_time - t)**2)

    plt.figure(figsize=(10, 6))
    plt.plot(t, d)
    plt.xlabel('Time (s)')
    plt.ylabel('Position (mm)')
    plt.title('Motion Profile')
    plt.grid(True)
    plt.show()

# Streamlit interface
st.title('Traversal Time Calculator')

stroke_length = st.text_input('Stroke Length (mm)', '250')
motor_power = st.slider('Motor Power (W)', 1, 100, 50)
max_speed = st.slider('Maximum Speed (m/s)', 0.1, 10.0, 1.0)

if st.button('Calculate'):
    stroke_length = float(stroke_length)
    max_speed *= 1000  # Convert to mm/s
    total_time, acceleration = calculate_traversal_time(stroke_length, max_speed, motor_power)
    st.write(f"Traversal Time: {total_time:.2f} seconds")
    
    plot_motion_profile(stroke_length, max_speed, total_time, acceleration)
