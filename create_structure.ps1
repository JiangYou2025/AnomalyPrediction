# Define the root directory
$RootDir = "AnomalyPrediction"

# Create the directory structure
New-Item -ItemType Directory -Path "$RootDir\src\anomaly_prediction\datasets" -Force
New-Item -ItemType Directory -Path "$RootDir\src\anomaly_prediction\models" -Force
New-Item -ItemType Directory -Path "$RootDir\src\anomaly_prediction\utils" -Force
New-Item -ItemType Directory -Path "$RootDir\src\anomaly_prediction\experiments" -Force
New-Item -ItemType Directory -Path "$RootDir\tests" -Force

# Create __init__.py files
New-Item -ItemType File -Path "$RootDir\src\anomaly_prediction\__init__.py" -Force
New-Item -ItemType File -Path "$RootDir\src\anomaly_prediction\datasets\__init__.py" -Force
New-Item -ItemType File -Path "$RootDir\src\anomaly_prediction\models\__init__.py" -Force
New-Item -ItemType File -Path "$RootDir\src\anomaly_prediction\utils\__init__.py" -Force
New-Item -ItemType File -Path "$RootDir\src\anomaly_prediction\experiments\__init__.py" -Force
New-Item -ItemType File -Path "$RootDir\tests\__init__.py" -Force

# Create main code files
New-Item -ItemType File -Path "$RootDir\src\anomaly_prediction\datasets\time_series_dataset.py" -Force
New-Item -ItemType File -Path "$RootDir\src\anomaly_prediction\models\simple_linear_model.py" -Force
New-Item -ItemType File -Path "$RootDir\src\anomaly_prediction\utils\cumulative_loss.py" -Force
New-Item -ItemType File -Path "$RootDir\src\anomaly_prediction\utils\plot_utils.py" -Force
New-Item -ItemType File -Path "$RootDir\src\anomaly_prediction\experiments\experiment_runner.py" -Force

# Create test files
New-Item -ItemType File -Path "$RootDir\tests\test_datasets.py" -Force
New-Item -ItemType File -Path "$RootDir\tests\test_models.py" -Force
New-Item -ItemType File -Path "$RootDir\tests\test_utils.py" -Force
New-Item -ItemType File -Path "$RootDir\tests\test_experiments.py" -Force

Write-Output "Directory structure created under $RootDir"
