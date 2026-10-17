# MNQ Mean Reversion Strategy Research

**Asset:** Micro E-mini Nasdaq-100 Futures (MNQ)  
**Research Area:** Intraday Systematic Strategies  
**Implementation:** Pine Script v6, Python

---

### Research Premise

Short-horizon price dislocations may be followed by partial retracements under certain market conditions. This project tests a rules-based intraday strategy against that hypothesis, with emphasis on entry mechanics, trade management, and realized strategy performance after execution costs.

The objective is not to optimize for gross returns in isolation, but to examine the relationship between trade frequency, average trade expectancy, drawdown, and transaction costs.

### Model Specification

- **Signal logic:** Price-based conditions for identifying potential retracement opportunities.
- **Execution:** Market and limit-entry configurations.
- **Position management:** Fixed stop-loss and profit-target levels, with configurable scaling and breakeven rules.
- **Risk controls:** Position sizing and predefined trade-level exits.
- **Evaluation:** Closed-trade P&L, profit factor, win rate, average trade, and peak-to-trough drawdown.

### Empirical Evaluation

Historical strategy results are assessed by configuration. Gross profitability is considered alongside gross losses, execution costs, and drawdown. Parameter changes are evaluated separately to avoid conflating results from different model specifications.

Further validation will examine transaction-cost sensitivity, parameter stability, and out-of-sample performance.

### Research Implementation

- **Pine Script v6:** Strategy logic and TradingView backtests.
- **Python / pandas:** Trade-level data processing and performance statistics.
- **Matplotlib:** Equity and drawdown visualization.

### Scope and Limitations

This is an independent research project using historical strategy tests. Findings are conditional on the tested data, model parameters, and execution assumptions. Price-based signals do not independently establish order-book imbalances or institutional liquidity conditions.

Out-of-sample robustness and statistical significance will not be claimed without supporting tests.

---

*Research and educational purposes only. Historical results are not indicative of future performance.*
