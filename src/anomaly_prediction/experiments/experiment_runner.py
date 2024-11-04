
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import pyplot as plt
from sklearn.preprocessing import StandardScaler
import random
import torch
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset, Subset, random_split
from sklearn.model_selection import StratifiedKFold, KFold
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, f1_score
import matplotlib.pyplot as plt
import os

def run_experiment(X, y , dataset, model, iterations=2, num_epochs=100, patience=10):
  f1_existence_list = []
  average_density_sum_list = []
  average_lead_time_list = []
  average_dice_score_list = []
  average_cumloss_scores_list = []

  train_loss_list = []
  val_loss_list = []
  test_loss_list = []

  # Use StratifiedKFold for 5-fold cross-validation
  #skf = StratifiedKFold(n_splits=5)
  skf = KFold(n_splits=5)

  input_length, output_length = dataset.input_length, dataset.input_length

  # Iterate through each fold
  for fold, (train_idx, test_idx) in enumerate(skf.split(X[input_length+output_length:, :], y[input_length+output_length:])):
      print(f'Fold {fold+1}')
      print(f'train_idx {train_idx}, test_idx {test_idx}, ')
      if fold != 4:
        continue
      
  for i in range(iterations):
      # Create train and test subsets
      train_dataset = Subset(dataset, train_idx)
      test_dataset = Subset(dataset, test_idx)

      # Calculate the validation set size
      val_size = len(train_dataset) // 8
      train_size = len(train_dataset) - val_size

      # Split train dataset into train and validation sets
      #train_subset, val_subset = random_split(train_dataset, [train_size, val_size])
      train_subset, val_subset = Subset(train_dataset, train_idx[:train_size]), Subset(train_dataset, train_idx[train_size:])

      train_loader = DataLoader(train_subset, batch_size=32, shuffle=True)
      val_loader = DataLoader(val_subset, batch_size=32, shuffle=False)
      test_loader = DataLoader(test_dataset, batch_size=32, shuffle=False)


      # Loss and optimizer
      criterion = CumulLoss(reduction='none')
      optimizer = optim.Adam(model.parameters(), lr=0.001)

      # Training loop with early stopping
      best_val_loss = float('inf')
      patience_counter = 0

      for epoch in range(num_epochs):
          train_loss = 0
          val_loss = 0
          test_loss = 0
          model.train()
          count = 0
          for inputs, labels in train_loader:
              optimizer.zero_grad()
              outputs = model(inputs)
              loss = criterion(outputs, labels).mean(1)
              loss.mean().backward()
              optimizer.step()
              train_loss += loss.sum().detach().item()
              count += len(inputs)
          train_loss /= count
          #print(f"train_loss, {train_loss:.03f}, {count}")

          model.eval()
          with torch.no_grad():
              count = 0
              for inputs, labels in val_loader:
                  outputs = model(inputs)
                  loss = criterion(outputs, labels).mean(1)
                  val_loss += loss.sum().item()
                  count += len(inputs)
              val_loss /= count
          #print(f"val_loss, {val_loss:.03f}, {count}")

          with torch.no_grad():
              count = 0
              for inputs, labels in test_loader:
                  outputs = model(inputs)
                  loss = criterion(outputs, labels).mean(1)
                  test_loss += loss.sum().item()
                  count += len(inputs)
              test_loss /= count
          #print(f"test_loss, {test_loss:.03f}, {count}")

          print(f'Epoch {epoch+1}/{num_epochs}, Training Loss: {train_loss}, Validation Loss: {val_loss}, Test Loss: {test_loss}')

          if val_loss < best_val_loss:
              best_val_loss = val_loss
              patience_counter = 0
              torch.save(model.state_dict(), f'best_model_fold{fold+1}.pth')  # Save the best model
          else:
              patience_counter += 1

          if patience_counter >= patience:
              print('Early stopping')
              break

          train_loss_list.append(train_loss)
          val_loss_list.append(val_loss)
          test_loss_list.append(test_loss)


      # Load the best model
      model.load_state_dict(torch.load(f'best_model_fold{fold+1}.pth'))

      # Metric 3: Dice Score
      def dice_score(true, pred):
          intersection = np.sum(true * pred)
          return (2. * intersection) / (np.sum(true) + np.sum(pred))

      # Evaluation on Test Set
      model.eval()
      existence_anomaly = {"TP": 0, "TN": 0, "FP": 0, "FN": 0}
      density_sum = []
      lead_time = []
      dice_scores = []
      cumloss_scores = []
      activation_threshold = 0.1

      with torch.no_grad():
          for inputs, labels in test_loader:
              outputs = model(inputs)
              loss = criterion(outputs, labels)
              outputs = outputs.detach().cpu().numpy()
              predictions = outputs > activation_threshold

              labels = labels.detach().cpu().numpy()

              exist_pred = predictions.sum(1) >= 1
              exist_labels = labels.sum(1) >= 1

              TP, FP, FN, TN = exist_pred * exist_labels, exist_pred * (1 - exist_labels), \
                              (1 - exist_pred) * exist_labels, (1 - exist_pred) * (1 - exist_labels)
              existence_anomaly["TP"] += TP.sum()
              existence_anomaly["TN"] += TN.sum()
              existence_anomaly["FP"] += FP.sum()
              existence_anomaly["FN"] += FN.sum()

              #density_sum.extend((1 - np.abs(outputs.mean(1) - labels.mean(1))).tolist())
              density_sum.extend([1 - abs(tf - pf) / len(outputs[1]) for tf, pf, true, pred in zip(labels, outputs, exist_labels, exist_pred) if true > 0 and pred > 0])
              true_first = np.argmax(labels, axis=1)
              pred_first = np.argmax(predictions, axis=1)

              lead_time.extend([1 - abs(tf - pf) / len(outputs[1]) for tf, pf, true, pred in zip(true_first, pred_first, exist_labels, exist_pred) if true > 0 and pred > 0])

              dice_scores.extend([dice_score(true, pred) for true, pred, true_exist, pred_exist  in zip(labels, predictions, exist_labels, exist_pred) if true_exist > 0 and pred_exist > 0])
              cumloss_scores.extend(loss.mean(1).tolist())

      # Print the result
      TP = existence_anomaly["TP"]
      TN = existence_anomaly["TN"]
      FP = existence_anomaly["FP"]
      FN = existence_anomaly["FN"]

      precision = TP / (TP + FP) if (TP + FP) > 0 else 0
      recall = TP / (TP + FN) if (TP + FN) > 0 else 0
      f1_existence = 2 * ( TP ) / (2 * TP + FP + FN) if (2 * TP + FP + FN) > 0 else 0

      average_density_sum = np.mean(density_sum)
      average_lead_time = np.mean(lead_time) if lead_time else float('nan')
      average_dice_score = np.mean(dice_scores)
      average_cumloss_scores = np.mean(cumloss_scores) / (dataset.output_length+1) * 2 # coeff 1/(T*(T+1))

      f1_existence_list.append(f1_existence)
      average_density_sum_list.append(average_density_sum)
      average_lead_time_list.append(average_lead_time)
      average_dice_score_list.append(average_dice_score)
      average_cumloss_scores_list.append(average_cumloss_scores)

  return TP, TN, FP, FN, f1_existence, \
            average_density_sum_list, average_lead_time_list, \
            average_dice_score_list, average_cumloss_scores_list, \
                train_loss_list, val_loss_list, test_loss_list, \
                train_loader, val_loader, test_loader