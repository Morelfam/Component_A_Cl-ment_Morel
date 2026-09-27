"""Component A — reference solution (moving-average overlay).

"""
from pathlib import Path
import pandas as pd
import matplotlib

matplotlib.use("Agg")  # non-interactive backend: save to file, don't open a window
import matplotlib.pyplot as plt

# Paths are relative to the repo root (where you run the command from).
DATA = Path("data/prices.csv")
OUT = Path("outputs/plot.png")
WINDOW = 20  # trading days


def main() -> None:
    # 1. Load — parse the date column so the x-axis is time, not strings.
    df = pd.read_csv(DATA, parse_dates=["date"]).sort_values("date")

    # 2. Compute the metric — a 20-day simple moving average of the close.
    df["ma20"] = df["close"].rolling(window=WINDOW).mean()

    # 3. Plot price with the MA overlaid.
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(df["date"], df["close"], label="Close", linewidth=1.2, color="#1D2A4B")
    ax.plot(df["date"], df["ma20"], label=f"{WINDOW}-day MA", linewidth=1.8, color="#7CB9E8")
    ax.set_title("Daily close with 20-day moving average")
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.legend()
    ax.grid(True, alpha=0.3)
    fig.tight_layout()

    # 4. Save — make sure the outputs/ folder exists first.
    OUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT, dpi=120)
    print(f"Saved {OUT}  ({len(df)} rows, MA window = {WINDOW})")


if __name__ == "__main__":
    main()