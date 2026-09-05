# Program SPLTV Pinjaman Bank
# Input langsung dari terminal

def main():
    # I
    # Input total pinjaman
    total = int(input("Masukkan total pinjaman perusahaan: "))
    
    # Input total bunga tahunan
    bunga_total = int(input("Masukkan total bunga tahunan: "))
    
    # Input rasio A terhadap C (misalnya A = 2C → masukkan 2)
    rasio = int(input("Masukkan rasio A terhadap C (contoh: 2 untuk A=2C): "))
    # Persamaan:
    # A + B + C = total
    # 0.05A + 0.06B + 0.07C = bunga_total
    # A = rasio * C
    import numpy as np
    
    A = np.array([
        [1, 1, 1],
        [0.05, 0.06, 0.07],
        [1, 0, -rasio]
    ])
    b = np.array([total, bunga_total, 0])
    
    x = np.linalg.solve(A, b)
    
    print("\n=== HASIL PINJAMAN ===")
    print("Bank A:", int(x[0]))
    print("Bank B:", int(x[1]))
    print("Bank C:", int(x[2]))

if __name__ == "__main__":
    main()
