
from torch.utils.data import DataLoader, Dataset, Subset, random_split
import torch

# Custom Dataset
class TimeSeriesDataset(Dataset):
    def __init__(self, X, y, input_length=50, output_length=50, device="cpu"):
        self.X = torch.tensor(X, dtype=torch.float32).to(device)
        self.y = torch.tensor(y, dtype=torch.float32).to(device)
        self.input_length = input_length
        self.output_length = output_length

    def __len__(self):
        return len(self.X) - self.input_length - self.output_length

    def __getitem__(self, idx):
        x = self.X[idx:idx + self.input_length]
        y = self.y[idx + self.input_length:idx + self.input_length + self.output_length]
        return x, y