# MNQ-Mean-Reversion-Strategy-Research-

Quantitative research and Python-based performance analysis of an MNQ futures mean reversion trading strategy.

## 1. Project Overview

This project investigates systematic intraday mean-reversion strategies in Micro E-mini Nasdaq-100 (MNQ) futures. The research focuses on identifying short-term price dislocations, evaluating retracement behavior, and testing rule-based trade execution and risk management.

The objective is to assess strategy performance across historical market data while examining transaction costs, execution assumptions, and downside risk.

## 2. Research Objectives

- **Signal Design:** Develop systematic entry criteria to evaluate potential mean-reversion opportunities following short-term price dislocations.
- **Execution Analysis:** Compare market and limit-entry mechanics under predefined trading rules.
- **Risk Management:** Evaluate stop-loss placement, profit targets, position scaling, and breakeven adjustments.
- **Performance Attribution:** Analyze net P&L, profit factor, win rate, average trade performance, and drawdown.
- **Sensitivity Analysis:** Examine the effects of transaction costs, slippage, and strategy parameter selection.
- **Robustness Testing:** Establish a framework for out-of-sample evaluation and performance comparison across market conditions.

## 3. Methodology

The strategy is implemented in Pine Script and evaluated using historical backtesting. Python-based analysis is used to process closed-trade data, calculate performance statistics, and visualize cumulative P&L and drawdown.

Research conclusions will be tied to the specific strategy configuration, historical sample, and execution assumptions used in each test.

### Strategy Components

- Systematic intraday entry and exit rules.
- Price-based retracement and mean-reversion hypotheses.
- Configurable market and limit orders.
- Rule-based stop-losses, profit targets, and position management.
- Performance evaluation under defined transaction-cost assumptions.

## 4. Technology Stack

- **Pine Script v6:** Strategy implementation and historical backtesting.
- **Python:** Quantitative analysis and performance evaluation.
- **pandas:** Data processing and trade-level statistical analysis.
- **Matplotlib:** Equity curve and drawdown visualization.

## 5. Performance Evaluation

The research framework is designed to evaluate:

- Net profit and loss (P&L).
- Gross profits and gross losses.
- Profit factor and win rate.
- Average P&L per trade.
- Cumulative equity and peak-to-trough drawdown.
- Sensitivity to commissions, slippage, and strategy parameters.

Performance metrics will be documented alongside the relevant strategy configuration, testing period, and execution assumptions. Results from separate configurations will be evaluated independently.

## 6. Research Development and Validation

Planned research extensions include:

- Parameter sensitivity analysis.
- Transaction-cost sensitivity testing.
- Comparison of entry and execution configurations.
- Out-of-sample testing on data not used during strategy development.
- Evaluation of performance consistency across different market conditions.

These extensions will be reported as completed only after the corresponding tests have been implemented and evaluated.

## 7. Limitations

Historical backtests are
