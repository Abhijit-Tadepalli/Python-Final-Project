import pandas as pd
import matplotlib.pyplot as plt

# Initial pose (x, y, z)
pose = {'x': 0.4, 'y': 0.0, 'z': 0.5}
trajectory = []

def process_command(command, pose):
    command = command.lower()
    if "forward" in command:
        pose['x'] += 0.05
    elif "backward" in command:
        pose['x'] -= 0.05
    elif "left" in command:
        pose['y'] += 0.05
    elif "right" in command:
        pose['y'] -= 0.05
    elif "up" in command:
        pose['z'] += 0.05
    elif "down" in command:
        pose['z'] -= 0.05
    return pose

# Read commands from CSV
df = pd.read_csv("commands.csv")  # Must have column: 'command'

# Simulate movements
for cmd in df['command']:
    pose = process_command(cmd, pose.copy())
    trajectory.append({**pose, 'command': cmd})

# Save trajectory to CSV
traj_df = pd.DataFrame(trajectory)
traj_df.to_csv("position_log.csv", index=False)

# Plot the trajectory
plt.plot(traj_df['x'], label='X')
plt.plot(traj_df['y'], label='Y')
plt.plot(traj_df['z'], label='Z')
plt.xlabel("Step")
plt.ylabel("Position (m)")
plt.title("Simulated UR5 End-Effector Trajectory")
plt.legend()
plt.grid()
plt.savefig("trajectory_plot.png")
plt.show()
