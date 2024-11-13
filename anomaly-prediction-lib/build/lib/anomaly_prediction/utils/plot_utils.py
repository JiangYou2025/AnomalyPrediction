import matplotlib.pyplot as plt
import torch
import numpy as np

def plot_random_predictions(dataloader, model, num_predictions=3):
    """
    Plot randomly selected predictions and ground truth values from the dataloader.

    Parameters:
    - dataloader (DataLoader): The DataLoader to get data from.
    - model (nn.Module): The trained model used for making predictions.
    - num_predictions (int): The number of random predictions to plot (default is 3).
    """
    model.eval()
    sample_list = []
    for (inputs, labels) in dataloader:
        for i in range(len(inputs)):
            if labels[i].sum() > 1.0 and np.random.random() < 0.2:
                sample_list.append((inputs[i], labels[i]))
            if len(sample_list) > num_predictions:
                break

    fig, axes = plt.subplots(1, num_predictions, figsize=(5*num_predictions, num_predictions))

    activation_threshold = 0.1
    with torch.no_grad():
        for i, (inputs, labels) in enumerate(sample_list):
            if i >= num_predictions:
                break
            inputs = torch.unsqueeze(inputs.float(), 0)
            outputs = model(inputs).detach().cpu().numpy()
            inputs = inputs[0].detach().cpu().numpy()
            labels = labels.detach().cpu().numpy()
            predictions = outputs > activation_threshold
            
            # Plot input series on the primary y-axis
            for k in range(inputs.shape[1]):
                axes[i].plot(inputs[:, k].flatten(), label=f'Input Series ({k})', alpha=0.7)
            
            # Create a secondary y-axis
            ax2 = axes[i].twinx()
            ax2.plot(np.arange(len(inputs[:, 0].flatten()), len(inputs[:, 0].flatten()) + len(labels.flatten())), labels.flatten(), label='Ground Truth', color='green')
            ax2.plot(np.arange(len(inputs[:, 0].flatten()), len(inputs[:, 0].flatten()) + len(predictions.flatten())), predictions.flatten(), label='Prediction', color='red', linestyle='-', alpha=0.3)
            ax2.plot(np.arange(len(inputs[:, 0].flatten()), len(inputs[:, 0].flatten()) + len(outputs.flatten())), outputs.flatten(), label='Density', color='orange', linestyle='dashed')
            
            # Set the y-axis limit of the secondary axis to [0, 1]
            ax2.set_ylim(-0.1, 1.1)
            
            # Plot the vertical line on both axes
            axes[i].axvline(x=len(inputs[:, 0].flatten()) - 1, color='black', linestyle='--')
            ax2.axvline(x=len(inputs[:, 0].flatten()) - 1, color='black', linestyle='--')
            
            # Set legends and titles
            axes[i].legend(loc='upper left')
            ax2.legend(loc='lower left')
            axes[i].set_title(f'Prediction {i+1}')

    plt.tight_layout()
    plt.show()

def plot_random_predictions_heatmap(dataloader, model, num_predictions=3):
    """
    Plot randomly selected predictions and ground truth values from the dataloader.

    Parameters:
    - dataloader (DataLoader): The DataLoader to get data from.
    - model (nn.Module): The trained model used for making predictions.
    - num_predictions (int): The number of random predictions to plot (default is 3).
    """
    model.eval()
    sample_list = []
    for (inputs, labels) in dataloader:
        for i in range(len(inputs)):
            if labels[i].sum() > 1.0 and np.random.random() < 0.2:
                sample_list.append((inputs[i], labels[i]))
            if len(sample_list) > num_predictions:
                break

    fig, axes = plt.subplots(1, num_predictions, figsize=(5*num_predictions, num_predictions))

    # Ensure axes is iterable
    if num_predictions == 1:
        axes = [axes]

    with torch.no_grad():
        for i, (inputs, labels) in enumerate(sample_list):
            if i >= num_predictions:
                break
            inputs = torch.unsqueeze(inputs.float(), 0).to(device)
            outputs = model(inputs).detach().cpu().numpy()
            inputs = inputs[0].detach().cpu().numpy()
            labels = labels.detach().cpu().numpy()
            predictions = outputs > 0.1

            # Plot the inputs as heatmaps
            im = axes[i].imshow(inputs.T, aspect='auto', origin='lower', interpolation='nearest', cmap='viridis')

            # Add colorbar
            # fig.colorbar(im, ax=axes[i])

            # Create a secondary y-axis for outputs
            ax2 = axes[i].twinx()

            # Adjust x-axis for labels and predictions
            input_length = inputs.shape[0]
            time_labels = np.arange(input_length, input_length + len(labels.flatten()))

            # Plot the outputs on the secondary y-axis
            ax2.plot(time_labels, labels.flatten(), label='Ground Truth', color='green')
            ax2.plot(time_labels, predictions.flatten(), label='Prediction', color='red', linestyle='-', alpha=0.3)
            ax2.plot(time_labels, outputs.flatten(), label='Density', color='orange', linestyle='dashed')

            # Plot the vertical line
            axes[i].axvline(x=input_length - 1, color='black', linestyle='--')

            # Hide the y-axis scale for the input (primary axis)
            axes[i].tick_params(axis='y', which='both', left=False, labelleft=False)
            axes[i].set_ylabel('')  # Remove y-axis label

            # Set y-axis label for the outputs (secondary axis)
            ax2.set_ylabel('Output Values')

            # Create custom legend entries
            handles1, labels1 = axes[i].get_legend_handles_labels()
            handles2, labels2 = ax2.get_legend_handles_labels()

            # Combine handles and labels
            handles = handles1 + handles2
            legend_labels = labels1 + labels2

            # Create a custom patch for the input heatmap
            cmap = plt.get_cmap('viridis')
            midpoint_color = cmap(0.5)
            input_patch = Patch(color=midpoint_color, label='Input Heatmap')

            # Insert the input_patch at the beginning of the handles and labels
            handles.insert(0, input_patch)
            legend_labels.insert(0, 'Input Heatmap')

            # Update the legend with the custom handles and labels
            axes[i].legend(handles=handles, labels=legend_labels, loc='upper left')

            axes[i].set_title(f'Prediction {i+1}')

            # Optionally, set the x-axis label
            axes[i].set_xlabel('Time')

        plt.tight_layout()
        plt.show()