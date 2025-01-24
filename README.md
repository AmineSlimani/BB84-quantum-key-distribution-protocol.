# BB84 Quantum Key Distribution Protocol

![GitHub](https://img.shields.io/badge/license-MIT-blue) 
![Python](https://img.shields.io/badge/Python-3.7%2B-blue)

This repository contains a Python-based simulation of the **BB84 quantum key distribution (QKD) protocol**. The BB84 protocol, developed by Charles Bennett and Gilles Brassard in 1984, allows two parties (Alice and Bob) to establish a shared secret key while detecting eavesdropping attempts by an adversary (Eve). The project includes a Python script (`BB84.py`) that simulates the protocol, calculates the probability of error (\(P_{\text{error}}\)) for different lengths of random strings (\(N\)), and generates a plot showing \(P_{\text{error}}\) as a function of \(N\).

## Table of Contents
- [Overview](#overview)
- [Key Concepts](#key-concepts)
- [Repository Structure](#repository-structure)
- [Requirements](#requirements)
- [Usage](#usage)
- [Results](#results)
- [License](#license)
- [Acknowledgments](#acknowledgments)

---

## Overview

The `BB84.py` script simulates the BB84 protocol by generating random bits and bases for Alice and Bob. It calculates the probability of error (\(P_{\text{error}}\)) for different lengths of random strings (\(N\)) and generates a plot showing \(P_{\text{error}}\) as a function of \(N\). The theoretical \(P_{\text{error}} = 0.5\) is also plotted as a reference.

---

## Key Concepts

### BB84 Protocol
- **Alice's Bits and Bases**: Randomly generated bits (0 or 1) and bases (0 or 1) for Alice.
- **Bob's Bases**: Randomly generated bases for Bob.
- **Shifted Key**: The shared key between Alice and Bob, derived from matching bases.
- **Probability of Error (\(P_{\text{error}}\))**: Calculated as \(1 - \frac{\text{length of shifted key}}{N}\).

---


---

## Requirements

To run the code in this repository, you need the following Python packages:
- **NumPy**: For numerical calculations.
- **Matplotlib**: For plotting the results.

You can install the required packages using the following command:
```bash
pip install numpy matplotlib
