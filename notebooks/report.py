import marimo

__generated_with = "0.25.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import csv
    from pathlib import Path
    import matplotlib.pyplot as plt

    return Path, csv, plt


@app.cell
def _(Path, csv):
    with Path("data/features/events.csv").open(newline="") as file:
        durations = [
            float(row["duration_minutes"])
            for row in csv.DictReader(file)
        ]

    len(durations)
    return (durations,)


@app.cell
def _(durations, plt):
    fig, ax = plt.subplots()
    ax.hist(durations, bins=20, edgecolor="black")
    ax.set_xlabel("Duration (minutes)")
    ax.set_ylabel("Number of events")
    ax.set_title("Distribution of event durations")
    fig
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
