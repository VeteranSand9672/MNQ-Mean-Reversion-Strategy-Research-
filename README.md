# MNQ Mean Reversion Strategy Research

This **Python and Pine Script** project examines the performance of a rules-based intraday trading strategy on Micro E-mini Nasdaq-100 futures (MNQ). The research focuses on price behavior, trade execution, risk management, and performance measurement to evaluate how strategy parameters affect realized results.

The project combines TradingView backtesting with Python-based trade analysis to organize results, calculate performance statistics, and examine the relationship between profitability, drawdown, and trading costs.

---

## 📊 Research Objectives

- Evaluate the performance of a rules-based intraday strategy.
- Measure trade-level profitability and risk-adjusted performance.
- Analyze the impact of stop-losses, profit targets, and position management.
- Examine how transaction costs influence net performance.
- Establish a framework for comparing strategy configurations consistently.

---

## ⚙️ Strategy Components

- **Signal Generation:** Price-based conditions used to identify potential trading opportunities.
- **Trade Execution:** Configurable entry and exit rules.
- **Risk Management:** Defined stop-losses, profit targets, and position-sizing parameters.
- **Position Management:** Configurable trade management and scaling rules.
- **Performance Analysis:** Trade-level statistics and equity-curve evaluation.

---

## 🛠️ Technology Stack

- **Pine Script v6** — Strategy implementation and TradingView backtesting.
- **Python** — Trade data processing and statistical analysis.
- **pandas** — Tabular data manipulation.
- **Matplotlib** — Equity-curve and drawdown visualization.
- **CSV / Excel** — Trade-level data storage and review.

---

## 📈 Performance Evaluation

The analysis is designed to calculate and compare:

- **Net P&L:** Profit or loss after recorded trading costs.
- **Win Rate:** Percentage of closed trades with positive P&L.
- **Profit Factor:** Gross profits divided by gross losses.
- **Average Trade:** Mean realized P&L per closed trade.
- **Maximum Drawdown:** Largest peak-to-trough decline in cumulative equity.
- **Equity Curve:** Progression of cumulative strategy performance over time.

Performance statistics are evaluated by strategy configuration. Results should be interpreted alongside execution assumptions, transaction costs, and drawdown rather than by gross returns alone.

---

## 🗂️ Project Structure

```text
MNQ-Mean-Reversion-Strategy-Research/
├── README.md
├── requirements.txt
├── data/
│   └── trades_template.csv
├── python/
│   └── analyze_trades.py
└── results/
    └── charts/
```

*The structure above represents the intended project organization; files should be added as the implementation develops.*

---

## 🚀 Setup and Installation

### 1. Clone the Repository

```bash
git clone https://github.com/VeteranSand9672/MNQ-Mean-Reversion-Strategy-Research-.git
cd MNQ-Mean-Reversion-Strategy-Research-
```

### 2. Create a Virtual Environment

**Windows**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Prepare Trade Data

Export closed-trade results from TradingView and format them to match the columns expected by the Python analysis script. Use sample or anonymized data when sharing results publicly.

### 5. Run the Analysis

```bash
python python/analyze_trades.py
```

The analysis script can be used to calculate trade statistics and generate visualizations from properly formatted trade data.

---

## 🔬 Research Development and Validation

Future development will focus on:

- Comparing strategy configurations under consistent assumptions.
- Measuring sensitivity to commissions and slippage.
- Examining performance across different market periods.
- Testing parameter stability on data not used during strategy development.
- Separating exploratory results from out-of-sample validation.

---

## ⚠️ Limitations

Historical backtests depend on the quality of the data, the selected parameters, and the execution assumptions used by the platform. Backtested results do not establish that a strategy will perform similarly in live markets.

Claims about statistical significance, predictive power, or robustness require additional testing and supporting evidence.

*This project is for quantitative research and educational purposes only. It is not financial advice.*

---

## 👤 Author

**Daniel Vasquez**

GitHub: [VeteranSand9672](https://github.com/VeteranSand9672)
