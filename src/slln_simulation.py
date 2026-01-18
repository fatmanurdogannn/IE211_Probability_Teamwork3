import numpy as np
import matplotlib.pyplot as plt
import os

def run_slln_multidistribution(n=10000):
    """
    Simulates SLLN for 5 different distributions:
    1. Uniform (Control)
    2. Exponential (Standard)
    3. Pareto (alpha=3, Finite Variance)
    4. Pareto (alpha=1.5, Infinite Variance -> Anomaly)
    5. Cauchy (Undefined Mean -> Anomaly)
    """
    
    # Klasör kontrolü
    save_path = 'results/figures'
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    # Dağılımların ve Teorik Ortalamalarının Tanımlanması
    # Pareto notu: np.random.pareto(a) Lomax dağılımıdır (Type II). 
    # Mean = 1 / (a - 1)
    distributions = {
        "Uniform": {
            "func": lambda size: np.random.uniform(0, 1, size),
            "mu": 0.5,
            "color": "blue"
        },
        "Exponential": {
            "func": lambda size: np.random.exponential(1, size),
            "mu": 1.0,
            "color": "green"
        },
        "Pareto (alpha=3)": {
            "func": lambda size: np.random.pareto(3.0, size),
            "mu": 1.0 / (3.0 - 1.0), # Mean = 0.5
            "color": "purple"
        },
        "Pareto (alpha=1.5)": {
            "func": lambda size: np.random.pareto(1.5, size),
            "mu": 1.0 / (1.5 - 1.0), # Mean = 2.0 (Ama varyans sonsuz)
            "color": "orange"
        },
        "Cauchy": {
            "func": lambda size: np.random.standard_cauchy(size),
            "mu": None, # Tanımsız
            "color": "red"
        }
    }

    print("SLLN Simülasyonu Başlıyor (5 Dağılım)...")

    for name, params in distributions.items():
        # 1. Veri Üret
        X = params["func"](n)
        
        # 2. Kümülatif Ortalama Hesapla
        S_n = np.cumsum(X) / np.arange(1, n + 1)

        # 3. Çizim
        plt.figure(figsize=(10, 6))
        plt.plot(S_n, label=f'Sample Mean ($S_n$)', color=params["color"], linewidth=1)
        
        # Teorik Ortalama Varsa Çiz (Cauchy'de yok)
        if params["mu"] is not None:
            plt.axhline(y=params["mu"], color='black', linestyle='--', linewidth=2, label=f'Theoretical Mean $\mu={params["mu"]}$')
        
        plt.title(f'SLLN Convergence: {name} Distribution')
        plt.xlabel('Number of Observations (n)')
        plt.ylabel('Cumulative Mean')
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        # Kaydet
        filename = f"slln_{name.replace(' ', '_').replace('(', '').replace(')', '').replace('=', '')}.png"
        full_path = os.path.join(save_path, filename)
        plt.savefig(full_path)
        print(f"Grafik kaydedildi: {filename}")
        plt.show() # Colab'de görmek için

# Çalıştır
if __name__ == "__main__":
    run_slln_multidistribution()
