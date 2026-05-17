````md
# 🛡️ Intelligent Network Intrusion Detection System

An advanced real-time Network Intrusion Detection System (IDS) developed using Machine Learning, Scapy, Flask, and Wireshark integration. The system captures live network traffic, identifies suspicious activities using anomaly detection techniques, and visualizes threats through an interactive dashboard.

---

# 🚀 Features

- Real-time packet monitoring
- Machine Learning-based anomaly detection
- Dynamic Flask dashboard
- Live alert generation
- Protocol analysis visualization
- Geo-location tracking of suspicious IPs
- Wireshark packet inspection support
- Lightweight and scalable architecture

---

# 🧠 Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Core development |
| Scapy | Packet capture & analysis |
| Pandas | Data preprocessing |
| Scikit-learn | Machine learning |
| Isolation Forest | Anomaly detection |
| Flask | Backend dashboard |
| Chart.js | Data visualization |
| Leaflet.js | Attack mapping |
| Wireshark | Packet inspection |

---

# 🌐 Computer Networks Concepts Used

- TCP/IP Model
- Packet Switching
- TCP and UDP Protocols
- Network Monitoring
- Packet Analysis
- Intrusion Detection Systems (IDS)

---

# 🏗️ System Architecture

```text
Network Traffic
       ↓
Packet Capture (Scapy)
       ↓
Feature Extraction
       ↓
Dataset Generation
       ↓
Model Training (Isolation Forest)
       ↓
Real-Time Threat Detection
       ↓
Flask Dashboard
       ↓
Wireshark Packet Analysis
````

---

# 📂 Project Structure

```text
network_ids_project/
│
├── member1_packet_capture/
├── member2_feature_extraction/
├── member3_threat_detection/
├── member4_dashboard/
├── models/
├── suspicious_packets.pcap
└── traffic_dataset.csv
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/Atharv-Jambhule/network-ids-project.git
cd network-ids-project
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment (Windows)

```bash
venv\Scripts\activate
```

---

## Install Required Libraries

```bash
pip install scapy pandas scikit-learn flask joblib requests
```

---

# ▶️ Running the Project

## Start Flask Dashboard

```bash
cd member4_dashboard
python app.py
```

Open in browser:

```text
http://127.0.0.1:5000
```

---

## Start Threat Detection System

Open another terminal:

```bash
cd member3_threat_detection
python threat_detector.py
```

---

## Generate Network Traffic

```bash
ping google.com
```

---

# 📊 Dashboard Features

* Live anomaly alerts
* Dynamic alert counter
* Real-time protocol analysis chart
* Geo-location attack visualization
* Continuous updates without refresh

---

# 🧠 Machine Learning Model

### Algorithm Used

Isolation Forest

### Features Used

* Packet Length
* Source Port
* Destination Port

### Prediction Output

* Normal Traffic
* Suspicious Traffic (Anomaly)

---

# 🌍 Geo-location Tracking

The system uses IP geolocation APIs to display the geographical origin of suspicious traffic on the dashboard map.

---

# 📦 Wireshark Integration

Detected suspicious packets are stored in:

```text
suspicious_packets.pcap
```

These packets can be analyzed in Wireshark for deep packet-level inspection.

---

# 🎯 Real-World Applications

* Enterprise Network Security
* Cloud Infrastructure Monitoring
* SOC (Security Operations Center)
* Banking & Financial Security
* IoT Security Monitoring
* Campus Network Monitoring

---

# 🔮 Future Enhancements

* Deep Learning-based Detection
* Attack Classification
* Automated Threat Response
* Cloud Deployment

---
* Advanced Security Analytics

