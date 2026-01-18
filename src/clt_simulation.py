import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import os

def run_clt_multidistribution(n=50, m=10000):
    """
    Simulates CLT for 5 distributions.
    n: Sample size (örneklem büyüklüğü)
    m: Number of replications (tekrar sayısı)
    """
    
    save_path = 'results/figures'
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    # Dağılım Parametreleri (Teorik Mean ve Std Dev)
    # Pareto Varyans: a / ((a-1)^2 * (a-2)) (Sadece a > 2 için geçerli!)
    distributions = [
        ("Uniform", lambda s: np.random.uniform(0, 1, s), 0.5, np.sqrt(1/12)),
        ("Exponential", lambda s: np.random.exponential(1, s), 1.0, 1.0),
        ("Pareto (alpha=3)", lambda s: np.random.pareto(3, s), 0.5, np.sqrt(3/((2**2)*1))), # sigma = sqrt(0.75) = 0.866
        
        # ANOMALİLER (Varyans sonsuz veya tanımsız)
        # Burada "sample std" kullanarak normalize etmeyi deneyeceğiz ki hatayı görelim.
        ("Pareto (alpha=1.5)", lambda s: np.random.pareto(1.5, s), 2.0, None), 
        ("Cauchy", lambda s: np.random.standard_cauchy(s), None, None)
    ]

    print(f"CLT Simülasyonu Başlıyor (n={n}, m={m})...")

    for name, func, mu_theo, sigma_theo in distributions:
        
        # 1. Veri Üretimi (m x n matrisi)
        samples = func((m, n))
        
        # 2. Toplamları ve Ortalamaları Hesapla
        sums = np.sum(samples, axis=1)
        means = np.mean(samples, axis=1)
        
        # 3. Standardizasyon (Z Hesaplama)
        # Eğer teorik sigma yoksa (Anomali), örneklem std'sini kullanıyoruz (ki CLT'nin çalışmadığını görelim)
        if sigma_theo is not None:
            # Standart CLT Formülü: (Mean - mu) / (sigma / sqrt(n))
            Z = (means - mu_theo) / (sigma_theo / np.sqrt(n))
            label_text = "Standardized using Theoretical Stats"
        else:
            # Anomali Durumu: Teorik formül çöktüğü için veriyi kendi ortalamasıyla normalize edip şekline bakarız
            # Rapor için NOT: Bu grafikler Normal Dağılıma UYMAYACAK.
            Z = (means - np.mean(means)) / np.std(means)
            label_text = "Standardized using Sample Stats (Theory Failed)"

        # 4. Çizim (Histogram vs Normal PDF)
        plt.figure(figsize=(8, 5))
        
        # Histogram (Veri)
        # Cauchy çok uç değerler ürettiği için aralığı kısıtlıyoruz (outlier'ları kesiyoruz)
        if "Cauchy" in name or "1.5" in name:
            range_limit = (-5, 5) 
        else:
            range_limit = (-4, 4)

        plt.hist(Z, bins=50, density=True, range=range_limit, alpha=0.6, color='skyblue', edgecolor='black', label='Simulation Data')
        
        # Normal Dağılım Eğrisi (Referans)
        x = np.linspace(range_limit[0], range_limit[1], 100)
        plt.plot(x, norm.pdf(x), 'r-', lw=2, label='Standard Normal N(0,1)')
        
        plt.title(f'CLT Test: {name} (n={n})\n{label_text}')
        plt.xlabel('Z Score')
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        # Kaydet
        filename = f"clt_{name.replace(' ', '_').replace('(', '').replace(')', '').replace('=', '')}.png"
        full_path = os.path.join(save_path, filename)
        plt.savefig(full_path)
        print(f"Grafik kaydedildi: {filename}")
        plt.show()

# Çalıştır
if __name__ == "__main__":
    run_clt_multidistribution()
