import pandas as pd
import os

# Get path to Commands.csv relative to this script
csv_path = os.path.join(os.path.dirname(__file__), "Commands.csv")

# Load the CSV
try:
    df = pd.read_csv(csv_path)
except FileNotFoundError:
    print(f"Commands.csv not found at: {csv_path}")
    exit()

# Get user command
cmd = input("Enter command (move forward / move left / move up): ").strip().lower()

# Look up command
row = df[df['command'].str.lower() == cmd]

if not row.empty:
    print("\nJoint Names:")
    for joint in df.columns[1:]:
        print(f"- {joint}")

    print("\nJoint Positions:")
    for joint in df.columns[1:]:
        print(f"- {row.iloc[0][joint]}")
else:
    print("Invalid command. Try: move forward, move left, or move up")
