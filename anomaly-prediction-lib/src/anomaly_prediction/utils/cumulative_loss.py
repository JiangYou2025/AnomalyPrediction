import numpy as np
import torch
import torch.nn 
class CumulLoss(nn.Module):
    def __init__(self, reduction='none', bidirection=False, norm="MAE"):
        super(CumulLoss, self).__init__()
        if norm.lower() == "mae":
            self.loss = nn.L1Loss(reduction=reduction)
        elif norm.lower() == "mse":
            self.loss = nn.MSELoss(reduction=reduction)
        else:
            raise ValueError("Unsupported norm type. Use 'MAE' or 'MSE'.")
        self.bidirection = bidirection

    def forward(self, outputs, labels):
        # Compute the cumulative sum along the sequence dimension (dim=1)
        cum_outputs = torch.cumsum(outputs, dim=1)
        cum_labels = torch.cumsum(labels, dim=1)
        # Compute the loss between the cumulative sums of outputs and labels
        loss = self.loss(cum_outputs, cum_labels)
        
        if self.bidirection:
            # Compute cumulative sum along the reversed sequence dimension
            cum_outputs_rev = torch.cumsum(outputs.flip(dim=1), dim=1)
            cum_labels_rev = torch.cumsum(labels.flip(dim=1), dim=1)
            # Add the loss from the reversed cumulative sums
            loss += self.loss(cum_outputs_rev, cum_labels_rev)
        
        return loss
