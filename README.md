# MNQ Mean Reversion Strategy Research

A systematic research project investigating an intraday trading strategy on Micro E-mini Nasdaq-100 futures (MNQ). The project combines TradingView strategy backtesting with Python-based trade analysis to evaluate historical performance, drawdown, and risk characteristics.

**Research focus:** Intraday systematic trading · Strategy evaluation · Performance analytics

**Tools:** Pine Script v6 · Python · pandas · Matplotlib

---

## Research Objective

Evaluate the historical performance of a rules-based MNQ strategy and establish a reproducible workflow for analyzing trades, measuring risk, and testing whether observed results remain robust under different conditions.

## Strategy Overview

The strategy uses configurable entry and exit rules, including:

- Liquidity void detection and retracement-based entries
- Configurable stop-loss and profit-target levels
- Position scaling and entry-expiration rules
- Trading-session restrictions

The strategy is implemented in Pine Script v6 and evaluated using historical TradingView backtests.

## Initial Backtest Results

The current analysis covers **49 closed trades** from the exported trade dataset.

| Metric | Result |
|---|---:|
| Initial capital | $2,500 |
| Net P&L | +$2,950 |
| Gross profit | $4,113 |
| Gross loss | $1,163 |
| Profit factor | 3.54 |
| Win rate | 42.86% |
| Average P&L per trade | $60.20 |
| Maximum closed-trade drawdown | $307 |

These figures describe the current historical sample. They are preliminary results, not evidence of a validated or persistent trading edge. The backtest period, execution assumptions, and robustness of the results require further documentation and testing.

## Research Workflow

1. **Strategy implementation:** Define trading rules and parameters in Pine Script v6.
2. **Trade-data export:** Export historical trade records from TradingView into CSV format.
3. **Performance analysis:** Use Python and pandas to calculate profitability and risk metrics.
4. **Visualization:** Generate cumulative P&L and drawdown charts using Matplotlib.
5. **Robustness testing:** Evaluate parameter sensitivity and performance on data not used for strategy development.

## Repository Structure

```text
├── data/
│   └── trades.csv
├── pine_script/
│   └── mnq_strategy.pine
├── python/
│   └── analyze_trades.py
├── results/
│   └── charts/
├── requirements.txt
└── README.md
```

## Getting Started

**Requirements:** Python and the trade CSV in the expected format.

Install dependencies:

```bash
py -m pip install -r requirements.txt
```

Run the analysis:

```bash
py python/analyze_trades.py
```

The script reads `data/trades.csv`, validates the required columns, calculates performance metrics, and saves cumulative P&L and drawdown charts under `results/charts/`.

The CSV must contain `exit_time` and `net_pnl` columns. The analysis uses closed-trade results and does not reconstruct intratrade equity movements.

## Further Research

Planned investigations include:

- Trade-level analysis of winners, losers, and consecutive losing streaks
- Sensitivity analysis for strategy parameters
- Transaction-cost and slippage sensitivity
- Performance comparisons across market sessions and volatility regimes
- Out-of-sample testing and checks for look-ahead bias
- Evaluation of whether results depend disproportionately on a small number of trades

## Limitations

The current dataset contains 49 closed trades. The analysis is descriptive and does not establish statistical significance or future profitability. Results depend on the quality of the exported data, the assumptions used in the backtest, and the treatment of commissions and slippage.

This is an independent quantitative research project for educational and analytical purposes. Historical performance does not guarantee future results.
