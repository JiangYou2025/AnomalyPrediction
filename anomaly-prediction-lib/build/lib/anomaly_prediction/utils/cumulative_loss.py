import numpy as np
import torch
import torch.nn as nn
class CumulLoss(nn.Module):
    def __init__(self, reduction='none'):
        super(CumulLoss, self).__init__()
        self.mae_loss = nn.L1Loss(reduction=reduction)

    def forward(self, outputs, labels):
        # Compute the cumulative sum along the sequence dimension (dim=1)
        cum_outputs = torch.cumsum(outputs, dim=1)
        cum_labels = torch.cumsum(labels, dim=1)

        # Compute the MAE loss between the cumulative sums of outputs and labels
        loss = self.mae_loss(cum_outputs, cum_labels)
        return loss