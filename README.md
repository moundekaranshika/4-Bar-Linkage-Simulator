# 🔗 4-Bar Linkage Simulator

A Python-based interactive simulator for a 4-bar mechanism with Grashof condition detection.

## 🎯 Features

- 📐 Enter custom link lengths: Ground (L1), Crank (L2), Coupler (L3), Rocker (L4)
- 🔄 Real-time animation of the mechanism as the crank rotates
- 🧠 Automatically detects and classifies the mechanism using **Grashof condition**
- ✅ Supports Crank-Rocker, Double-Crank, Double-Rocker, and Change-Point types
- 🖱️ GUI input using Tkinter
- 📊 Visualization using `matplotlib`

---

## 🔧 Grashof Classification

Based on input link lengths, the simulator classifies the linkage as:

L-Longest Link
S-Shortest Link
P,Q-Adjacent Links

Grashof Criteria : L+S<=P+Q

- ✅ **Double Crank (Grashof)** – Shortest link is the ground
- ✅ **Crank-Rocker (Grashof)** – Shortest link is the crank or rocker
- ❌ **Double Rocker (Non-Grashof)** – No full rotation link possible
- ⚠️ **Change Point Mechanism** – Links are at critical equal length

You'll see the classification in:
- A popup message
- The plot window title
- The terminal

---




