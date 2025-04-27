# 🛡️ Toy Analytics Platform — Local Differential Privacy Simulation

Built by **Stu**  
(Branding: "Built by Stu" throughout)

---

## 📖 Overview

This project simulates a toy analytics platform that collects **user interactions** (like clicks, typing, and page views) while applying **Local Differential Privacy (LDP)** to each event before it reaches the server.

It demonstrates:
- User event simulation
- Local DP (randomized response)
- Aggregation of noisy data
- Visualization of privacy-utility tradeoffs

---

## 📚 How It Works

1. **User Simulation:**  
   - 100 fake users generate clicks, page views, and keystroke counts.

2. **Local DP Application:**  
   - Each event is noised using randomized response before transmission.

3. **Aggregation:**  
   - Noised data is aggregated centrally.
   - Estimations correct for injected noise.

4. **Metrics:**  
   - Compare true values to noisy aggregates.
   - Study impact of privacy parameter ε.

---

## ⚙️ Setup

You need:
- Python 3.10+
- `numpy`
- `matplotlib`

Install with:

```bash
pip install numpy matplotlib
```

Launch the project notebook:

```bash
jupyter lab analytics_simulator.ipynb
```

---

## 📜 License

Restricted License:

- No resale, no rebranding without written permission.
- No reproduction of certificates without author signature.
- Educational and personal portfolio use only.

---

## 🏆 Certification

Upon completion:

- Certificate issued manually by patons02
- Permission required to list on LinkedIn profiles

---

# 🚀 Let's build ethical data systems!
