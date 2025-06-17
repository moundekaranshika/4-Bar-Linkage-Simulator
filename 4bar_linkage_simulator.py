import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import tkinter as tk
from tkinter import simpledialog, messagebox

# Check Grashof condition
def classify_4bar(L1, L2, L3, L4):
    lengths = sorted([L1, L2, L3, L4])
    S, L = lengths[0], lengths[3]
    P, Q = lengths[1], lengths[2]
    if (S + L) < (P + Q):
        if L1 == S:
            return "Double Crank (Grashof)"
        elif L3 == S:
            return "Crank-Rocker (Grashof)"
        elif L4 == S:
            return "Crank-Rocker (Grashof)"
        elif L2 == S:
            return "Crank-Rocker (Grashof)"
        else:
            return "Grashof Linkage"
    elif (S + L) == (P + Q):
        return "Change Point Mechanism"
    else:
        return "Double Rocker (Non-Grashof)"

# Compute 4-bar points
def compute_points(theta2, L1, L2, L3, L4):
    A = np.array([0, 0])
    B = np.array([L2 * np.cos(theta2), L2 * np.sin(theta2)])
    D = np.array([L1, 0])
    dx, dy = D[0] - B[0], D[1] - B[1]
    c = np.sqrt(dx**2 + dy**2)

    try:
        angle_C = np.arccos((L3**2 + c**2 - L4**2) / (2 * L3 * c))
        angle_to_D = np.arctan2(dy, dx)
        theta3 = angle_to_D - angle_C
        C = B + [L3 * np.cos(theta3), L3 * np.sin(theta3)]
    except:
        C = B
    return A, B, C, D

# Animation function
def animate_4bar(L1, L2, L3, L4, linkage_type):
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    max_len = max(L1, L2, L3, L4)
    ax.set_xlim(-2 * max_len, 2 * max_len)
    ax.set_ylim(-2 * max_len, 2 * max_len)
    line, = ax.plot([], [], 'o-', lw=3)
    plt.title(f"4-Bar Linkage Simulation: {linkage_type}")

    def update(frame):
        theta2 = np.radians(frame)
        A, B, C, D = compute_points(theta2, L1, L2, L3, L4)
        x_vals = [A[0], B[0], C[0], D[0]]
        y_vals = [A[1], B[1], C[1], D[1]]
        line.set_data(x_vals, y_vals)
        return line,

    ani = FuncAnimation(fig, update, frames=np.arange(0, 360, 2), interval=50)
    plt.show()

# GUI Input
def get_link_lengths():
    root = tk.Tk()
    root.withdraw()
    L1 = float(simpledialog.askstring("Link Input", "Enter L1 (Ground):"))
    L2 = float(simpledialog.askstring("Link Input", "Enter L2 (Crank):"))
    L3 = float(simpledialog.askstring("Link Input", "Enter L3 (Coupler):"))
    L4 = float(simpledialog.askstring("Link Input", "Enter L4 (Rocker):"))
    linkage_type = classify_4bar(L1, L2, L3, L4)
    messagebox.showinfo("Linkage Type", f"This is a {linkage_type}.")
    print(f"[INFO] Detected: {linkage_type}")
    animate_4bar(L1, L2, L3, L4, linkage_type)

# Start
get_link_lengths()
