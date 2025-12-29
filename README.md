# IE211 Probability Teamwork 3

## Project Title and Description
This repository contains simulations to demonstrate key probability concepts:
- **SLLN (Strong Law of Large Numbers):** Shows that the sample mean of U[0,1] converges to its expected value (0.5).
- **CLT (Central Limit Theorem):** Shows that standardized sums approach a standard normal distribution as n increases.
- **Monte Carlo Pi Estimation:** Estimates π using random points in the unit square.

All generated plots are saved under `results/figures/`.

## Team Members
- İbrahim Genç - 2211021036  
- Ayşe Efsa Çelik - 2211021001  
- Fatmanur Doğan - 2311021001  
- Ecem Nur Yüksel - 2411013097  

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/fatmanurdogannn/IE211_Probability_Teamwork3.git
   cd IE211_Probability_Teamwork3
## Usage
Run the scripts from the repository root folder:

- **SLLN Simulation**
  ```bash
  python src/slln_simulation.py
  python src/clt_simulation.py
  python src/monte_carlo_pi.py
  
Project Structure

src/
Source code files for simulations

slln_simulation.py — SLLN simulation code

clt_simulation.py — CLT simulation code (histograms + Q-Q plots)

monte_carlo_pi.py — Monte Carlo π estimation code


results/figures/
All generated plots (PNG files)

reports/
Technical reports (TW2_Report.pdf, TW3_Report.pdf)

requirements.txt
Python dependencies

.gitignore
Files to ignore

README.md
Project description and instructions
