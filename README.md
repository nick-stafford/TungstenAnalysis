# Tungsten Analysis

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat&logo=python&logoColor=white)](https://python.org)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=flat&logo=jupyter&logoColor=white)](https://jupyter.org)
[![Pandas](https://img.shields.io/badge/Pandas-Data_Analysis-150458?style=flat&logo=pandas&logoColor=white)](https://pandas.pydata.org)

**Quantitative financial analysis of tungsten-related equities.**

Comprehensive risk-adjusted performance analysis with correlation studies, technical indicators, and professional-grade visualizations.

---

## Features

### Risk Metrics
- **Sharpe Ratio** — Risk-adjusted returns vs. risk-free rate
- **Sortino Ratio** — Downside deviation focus
- **Calmar Ratio** — Returns vs. maximum drawdown
- **Maximum Drawdown** — Peak-to-trough analysis

### Technical Analysis
- Moving averages (SMA, EMA)
- Volatility bands
- RSI and momentum indicators
- Volume analysis

### Visualization
- Multi-asset performance comparison
- Correlation heatmaps
- Drawdown charts
- Rolling metrics over time

---

## Stocks Analyzed

| Ticker | Company | Sector |
|--------|---------|--------|
| ALB | Albemarle Corporation | Materials |
| MP | MP Materials | Rare Earth |
| UUUU | Energy Fuels | Uranium/REE |
| LAC | Lithium Americas | Mining |
| PLL | Piedmont Lithium | Mining |

---

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Launch Jupyter
jupyter notebook tungsten_analysis.ipynb
```

---

## Sample Output

```
Performance Metrics (5-Year Analysis)
═══════════════════════════════════════
Ticker    Ann. Return    Volatility    Sharpe    Sortino    Max DD
──────────────────────────────────────────────────────────────────
ALB          18.4%         32.1%       0.52       0.71     -42.3%
MP           24.7%         48.2%       0.48       0.63     -58.1%
UUUU         31.2%         55.4%       0.53       0.72     -61.4%
LAC          12.3%         61.8%       0.18       0.24     -72.5%
PLL          -8.2%         68.3%      -0.14      -0.18     -81.2%
```

---

## Project Structure

```
TungstenAnalysis/
├── tungsten_analysis.ipynb   # Main analysis notebook
├── src/
│   ├── metrics.py            # Risk metric calculations
│   ├── visualization.py      # Plotting utilities
│   └── data_loader.py        # Data fetching
├── data/                     # Cached price data
├── output/                   # Generated charts
├── requirements.txt
└── README.md
```

---

## Requirements

- Python 3.11+
- pandas, numpy
- yfinance
- matplotlib, seaborn
- jupyter

---

<p align="center">
  Built by <a href="https://nickstafford.dev">Nick Stafford</a>
</p>
