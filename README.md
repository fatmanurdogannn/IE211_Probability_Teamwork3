# Project Description (Teamwork3)
This project aims to experimentally verify the Strong Law of Large Numbers (SLLN) and the Central Limit Theorem (CLT) through computer simulations. Additionally, it demonstrates a practical application of SLLN using the Monte Carlo Method for estimating the value of 
π
.

# Team Members
# Ecem Nur Yüksel - 2411013097
# Fatmanur Doğan - 2311021001
# Ayşe Efsa Çelik - 221021001
# İbrahim Genç - 2211021036

# Project Structure
The repository is organized according to the project requirements:

├── src/                         # Contains all simulation source codes
│   ├── slln_simulation.py       # SLLN simulation (5 distributions)
│   ├── clt_simulation.py        # CLT simulation with histograms and Q–Q plots
│   └── monte_carlo_pi.py        # Monte Carlo Pi estimation
│
├── results/
│   └── figures/                 # Stores all generated plots in PNG format
│
├── reports/                     # Technical reports and documentation
│
├── requirements.txt             # List of necessary Python libraries
└── README.md                    # Project documentation

# Installation
To set up the environment and install the required dependencies, use the following command:

pip install -r requirements.txt

# IE 221 Probability – Simulation Project (Teamwork 4)

This repository contains the simulation codes and technical documentation for the IE 221 Probability course project.
In this phase (Teamwork 4), we focused on providing simulation-based illustrations of three fundamental concepts in probability theory:

Strong Law of Large Numbers (SLLN)

Central Limit Theorem (CLT)

Monte Carlo Method for π Estimation

All simulations were conducted using samples drawn from the Uniform(0,1) distribution to empirically demonstrate different modes of convergence and stochastic approximation techniques.
## Project Structure
.
├── src/                    
│   ├── slln_simulation.py      # Simulation of Strong Law of Large Numbers
│   ├── clt_simulation.py       # CLT simulation with histograms & Q-Q plots
│   └── monte_carlo_pi.py       # Monte Carlo estimation of π
├── results/
│   └── figures/               # Generated plots (SLLN, CLT, Monte Carlo)
├── reports/
│   └── TW4_Report.pdf         # Technical report (theory + results)
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation


# IE 221 Probability - Simulation Project (Teamwork 5)

This repository contains the simulation codes and documentation for the **IE 221 Probability** course project. In this phase (Teamwork 5), we extended our analysis to investigate the **Strong Law of Large Numbers (SLLN)** and the **Central Limit Theorem (CLT)** across 5 different probability distributions, specifically focusing on anomalies where these theorems fail.

## 📂 Project Structure

```text
.
├── src/                    # Source codes
│   ├── slln_simulation.py  # Updated SLLN simulation (5 Distributions)
│   ├── clt_simulation.py   # Updated CLT simulation (Histograms & Q-Q Plots for 5 Dists)
│   └── monte_carlo_pi.py   # Monte Carlo Pi estimation
├── results/figures/        # Generated plots (PNG files for all distributions)
├── reports/                # Technical reports (TW5_Report.pdf)
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
