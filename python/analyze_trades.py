
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt


# Project paths
ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = ROOT / "data" / "trades.csv"
RESULTS_DIR = ROOT / "results" / "charts"

# TradingView strategy configuration
ASSET = "MNQ"
INITIAL_CAPITAL = 2500.00
INITIAL_QTY = 2
ADD_QTY = 2
MIN_GAP_POINTS = 30.0
ENTRY_STYLE = "Retracement Limit"
ENTRY_EXPIRY_BARS = 12
STOP_POINTS = 25.0
ADD1_POINTS = 15.0
ADD2_POINTS = 25.0
TARGET_POINTS = 60.0
COMMISSION_PER_CONTRACT = 1.00
SLIPPAGE_TICKS = 1


def analyze_trades():
    if not DATA_FILE.exists():
        raise FileNotFoundError(
            f"Trade export not found: {DATA_FILE}\n"
            "Export your closed trades from TradingView "
            "and save them as data/trades.csv."
        )

    trades = pd.read_csv(DATA_FILE)

    required_columns = {"exit_time", "net_pnl"}
    missing = required_columns - set(trades.columns)

    if missing:
        raise ValueError(
            f"Missing required CSV columns: {sorted(missing)}"
        )

    trades["exit_time"] = pd.to_datetime(
        trades["exit_time"], errors="coerce"
    )
    trades["net_pnl"] = pd.to_numeric(
        trades["net_pnl"], errors="coerce"
    )

    trades = (
        trades.dropna(subset=["exit_time", "net_pnl"])
        .sort_values("exit_time")
        .reset_index(drop=True)
    )

    if trades.empty:
        raise ValueError("The CSV contains no valid closed trades.")

    pnl = trades["net_pnl"]
    gross_profit = pnl[pnl > 0].sum()
    gross_loss = abs(pnl[pnl < 0].sum())

    profit_factor = (
        gross_profit / gross_loss
        if gross_loss > 0
        else float("inf") if gross_profit > 0 else 0.0
    )

    equity = pnl.cumsum()
    running_peak = equity.cummax().clip(lower=0)
    drawdown = equity - running_peak

    print(f"\n{ASSET} Strategy Performance")
    print("=" * 34)
    print(f"Initial capital:  ${INITIAL_CAPITAL:,.2f}")
    print(f"Closed trades:    {len(trades)}")
    print(f"Net P&L:          ${pnl.sum():,.2f}")
    print(f"Gross profit:     ${gross_profit:,.2f}")
    print(f"Gross loss:       ${gross_loss:,.2f}")
    print(f"Profit factor:    {profit_factor:.4f}")
    print(f"Win rate:         {(pnl > 0).mean():.2%}")
    print(f"Average trade:    ${pnl.mean():,.2f}")
    print(f"Max drawdown:     ${abs(drawdown.min()):,.2f}")

    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    # Cumulative P&L
    plt.figure(figsize=(10, 5))
    plt.plot(trades["exit_time"], equity)
    plt.title(f"{ASSET} Cumulative Net P&L")
    plt.xlabel("Exit Time")
    plt.ylabel("Cumulative P&L ($)")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(RESULTS_DIR / "equity_curve.png", dpi=150)
    plt.close()

    # Drawdown
    plt.figure(figsize=(10, 5))
    plt.plot(trades["exit_time"], drawdown)
    plt.title(f"{ASSET} Drawdown")
    plt.xlabel("Exit Time")
    plt.ylabel("Drawdown ($)")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(RESULTS_DIR / "drawdown.png", dpi=150)
    plt.close()

    print(f"\nCharts saved in: {RESULTS_DIR}")


if __name__ == "__main__":
    analyze_trades()
