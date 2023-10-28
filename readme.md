
# Setup Environment

Berikut adalah langkah-langkah untuk membuat dan mengaktifkan environment baru menggunakan Conda, serta menginstal paket yang diperlukan:

1. Buat environment baru dengan Python versi 3.9:
    ```
    conda create --name main python=3.12
    ```

2. Aktifkan environment yang baru dibuat:
    ```
    conda activate main
    ```

3. Instal paket yang diperlukan menggunakan pip:
    ```
    pip install numpy pandas scipy matplotlib seaborn jupyter scikit-learn h5py
    ```

## Run steamlit app
```
streamlit run dashboard/main.py
```
