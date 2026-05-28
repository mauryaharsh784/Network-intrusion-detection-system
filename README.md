# 🛡️ Real-Time Network Intrusion Detection System (NIDS)

[![Live Demo](https://img.shields.io/badge/Live%20Demo-NIDS-6366f1?style=for-the-badge&logo=googlechrome&logoColor=white)](https://network-intrusion-detection-system-25zo.onrender.com)
[![Python](https://img.shields.io/badge/Python-3.8+-3776ab?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-Web%20App-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![ML](https://img.shields.io/badge/ML-Random%20Forest-22c55e?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)

![Status](https://img.shields.io/badge/Status-Active-22c55e?style=flat-square)
![License](https://img.shields.io/github/license/mauryaharsh784/Network-intrusion-detection-system?style=flat-square)
![Stars](https://img.shields.io/github/stars/mauryaharsh784/Network-intrusion-detection-system?style=flat-square)
![Last Commit](https://img.shields.io/github/last-commit/mauryaharsh784/Network-intrusion-detection-system?style=flat-square)

[Report Bug](https://github.com/mauryaharsh784/Network-intrusion-detection-system/issues) · [Request Feature](https://github.com/mauryaharsh784/Network-intrusion-detection-system)

A real-time Network Intrusion Detection System that captures live network packets and uses Machine Learning to detect malicious activity — all accessible through a clean web interface.

---

## ✨ Features

- 🔍 **Real-time Packet Capture** — Live network traffic monitoring using Scapy
- 🤖 **Machine Learning Detection** — Random Forest classifier to detect intrusions
- 🌐 **Flask Web Interface** — Clean and simple web dashboard
- 📊 **Live Monitoring** — Real-time alerts and detection results
- 🛡️ **Threat Classification** — Identifies different types of network attacks

---

## 🛠️ Tech Stack

| Technology | Purpose |
|-----------|---------|
| Python | Core language |
| Scapy | Packet capture & analysis |
| Scikit-learn | Random Forest ML model |
| Flask | Web interface |
| HTML/CSS/JS | Frontend UI |

---

## 📁 Project Structure

```
Network-intrusion-detection-system/
├── app.py                  # Flask web application
├── model/
│   ├── train.py            # ML model training
│   └── model.pkl           # Trained Random Forest model
├── capture/
│   └── sniffer.py          # Real-time packet capture (Scapy)
├── templates/
│   └── index.html          # Web UI
├── static/                 # CSS, JS files
├── requirements.txt        # Python dependencies
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip
- Admin/root privileges (for packet capture)

### Installation

```bash
# Clone the repository
git clone https://github.com/mauryaharsh784/Network-intrusion-detection-system.git
cd Network-intrusion-detection-system
```

```bash
# Install dependencies
pip install -r requirements.txt
```

### Run the Application

```bash
# Run with admin privileges (required for packet capture)
sudo python app.py
```

Open browser and go to:
```
http://localhost:5000
```

---

## ⚙️ How It Works

```
Network Traffic → Scapy (Packet Capture) → Feature Extraction
      → Random Forest Model → Prediction → Flask Dashboard
```

1. **Packet Capture** — Scapy captures live network packets
2. **Feature Extraction** — Extracts relevant features from packets
3. **ML Prediction** — Random Forest classifies traffic as normal or malicious
4. **Web Dashboard** — Results displayed in real-time on Flask UI

---

## 🔒 Detection Capabilities

- Port Scanning
- DDoS Attacks
- Brute Force Attacks
- Suspicious Traffic Patterns
- Anomaly Detection

---

## 👨‍💻 Author

**Harsh Vardhan Maurya**  
GitHub: [@mauryaharsh784](https://github.com/mauryaharsh784)  
LinkedIn: [harsh-vardhan-maurya](https://www.linkedin.com/in/harsh-vardhan-maurya/)

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.
