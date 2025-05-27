# ⚡ Python Socks5 Scanner
![License](https://img.shields.io/badge/license-MIT-green)  
> 🛡️ 透過pysocks掃描IP:4145 確認連線能力 **可以在大部分vps或是vm運行!**，  
> 常做掃描的人一定知道的, zmap沒多少vps能用 但是這款一定可以，
> 你也可以自訂自己的標準跟port 即可掃描不同設備 缺點就是python速度不如zmap

---

## 🚀 功能特色

- 🔹 **pysocks標準讓你不被封**  
 因為是正常的TCP連線 並不是大量syn 所以被封鎖的機率很低 目前測試azure跟aws都沒被封

- 🔹 **極速代理檢測**  
 檢測socks5代理的連線能力以及發送HTTP請求的能力

- 🔹 **新手友好**  
 簡易參數設計，小白也能快速上手壓測。

- 🔹 **高穩定性**  
 多執行緒與記憶體管理完善，**不會出現 core dumped**！

- 🔹 **擴充性強**  
 架構模組化，可自訂掃描。

---

## 🖥️ 系統配置需求

| 項目       | 建議配置        |
|------------|-----------------|
| 處理器     | 4 核心以上      |
| 記憶體     | 8 GB 以上        |
| 網路速度   | 100 Mbps 以上   |

---

## 📦 安裝說明

### ✅ 下載專案
```bash
git clone https://github.com/GogoZin/Socks5_Scanner
cd Socks5_Scanner
```

### 🐧 Linux 安裝模組
```bash
pip3 install -r requirements.txt
```

### 🧊 Windows 安裝模組
```bash
py -m pip install -r requirements.txt
```

## 🏃 使用方式

### 🐧 Linux 執行命令
```bash
python3 scan.py
```

### 🧊 Windows 執行命令
```bash
py scan.py
```

---

## 📜 授權條款

本專案使用 [MIT License](LICENSE)。

---

## ⚠️ 使用規章

> 📌 請注意：本工具僅供開發者學習與合法壓力測試用途。 
>  
> ❌ 禁止用於任何非法活動。
> 
> 📄 使用本工具即表示您同意以上規章與 MIT 授權條款。
> 
> ⚖️ 作者對於任何非法用途造成的後果概不負責。
> 
> 🙅 不同意規章者請勿下載或使用本工具。

---

## 🌟 支持本專案

感謝使用 Socks5 Scanner，歡迎 star ⭐ 支持！
