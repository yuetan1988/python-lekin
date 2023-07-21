"""
class CRScheduler:
    # ... (rest of the class code)

    def schedule_job(self, job):
        # ... (rest of the method code)

        for operation in job.route.operations:
            # ... (rest of the method code)

            # Store the scheduling result for each operation
            self.schedule_result[operation] = (operation.start_time, operation.end_time)
"""

from matplotlib import ticker
import matplotlib.patches as patches
import matplotlib.pyplot as plt


def plot_gantt_chart(schedule_result):
    fig, ax = plt.subplots()

    # Set y-axis limits
    ax.set_ylim(0, 10)
    ax.set_xlim(0, max([end_time for (_, end_time) in schedule_result.values()]))

    for i, (operation, (start_time, end_time)) in enumerate(schedule_result.items()):
        # Draw Gantt chart bar for each operation
        y = 5 - i  # Position the bar on the y-axis
        height = 1  # Bar height
        width = end_time - start_time
        rect = patches.Rectangle((start_time, y), width, height, linewidth=1, edgecolor="black", facecolor="blue")
        ax.add_patch(rect)

        # Add text label for the operation name
        ax.text(
            start_time + width / 2, y + height / 2, f"Operation {operation.id}", ha="center", va="center", color="white"
        )

    plt.xlabel("Time")
    plt.ylabel("Operations")
    plt.title("Gantt Chart - Scheduling Result")
    plt.show()
