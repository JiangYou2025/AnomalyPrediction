
# Prédiction d'Anomalies : Une Nouvelle Approche avec Délai et Horizon Explicites
Ceci est le dépôt officiel pour l'article "Prédiction d'Anomalies : Une Nouvelle Approche avec Délai et Horizon Explicites"

Lien vers l'article : https://arxiv.org/abs/2408.04377

## Résumé
La détection d'anomalies dans les données de séries temporelles est un défi critique dans de nombreux domaines. Les méthodes traditionnelles se concentrent généralement sur l'identification des anomalies aux étapes suivantes immédiates, sous-estimant souvent l'importance de la dynamique temporelle comme le temps de délai et l'horizon des anomalies, qui nécessitent généralement une analyse postérieure extensive. Ce dépôt introduit une nouvelle approche de prédiction d'anomalies dans les séries temporelles, intégrant les informations temporelles directement dans les résultats de prédiction. Nous proposons un nouveau jeu de données conçu spécifiquement pour évaluer cette approche et menons des expériences complètes en utilisant plusieurs méthodes de pointe. Nos résultats démontrent l'efficacité de notre approche pour fournir des prédictions d'anomalies précises et en temps opportun, établissant ainsi une nouvelle référence pour les recherches futures dans ce domaine.

## Prédiction d'Anomalies avec Délai et Horizon Explicites
![Prédiction d'Anomalies](./src/figure/anomaly_prediction.png)
*Figure 1 : Illustration de la tâche de Prédiction d'Anomalies.*

## Comparaison entre la Prédiction et la Détection d'Anomalies
![Comparaison](./src/figure/comparison_ad_ap.png)
*Figure 2 : Comparaison entre la Prédiction et la Détection d'Anomalies.*

## Utilisation
Pour utiliser ce dépôt, suivez ces étapes :

1. Clonez le dépôt :
   ```bash
   git clone https://github.com/JiangYou2025/AnomalyPrediction.git
   ```

2. Ouvrez Anomaly_Prediction_Examples.ipynb :
   ```bash
   run all
   ```

## Exemples

#### Exemple de Prédiction d'Anomalies sur le Jeu de Données Synthétique 1 avec le Réseau Complètement Connecté (FCN)
![Comparaison](./src/figure/synthetical_1_test_prediction_example_1.png)
![Comparaison](./src/figure/synthetical_1_test_prediction_example_2.png)
![Comparaison](./src/figure/synthetical_1_test_prediction_example_3.png)
*Figure 3 : Exemples 1-9 de Prédiction d'Anomalies sur Synthetical_1.*

#### Exemple de Prédiction d'Anomalies sur le Jeu de Données Synthétique 10 avec le Réseau Complètement Connecté (FCN)
![Comparaison](./src/figure/synthetical_10_test_prediction_example_1.png)
![Comparaison](./src/figure/synthetical_10_test_prediction_example_2.png)
![Comparaison](./src/figure/synthetical_10_test_prediction_example_3.png)
*Figure 4 : Exemples 1-9 de Prédiction d'Anomalies sur Synthetical_10.*

## Citation
En utilisant cet article ou ce code, merci de citer :
   ```tex
   @inproceedings{you_2024_anomaly_prediction,
   author={You, Jiang and Cela, Arben and Natowicz, René and Ouanounou, Jacob and Siarry, Patrick},
   booktitle={2024 IEEE 20th International Conference on Intelligent Computer Communication and Processing (INISTA)}, 
   title={Anomaly Prediction: A Novel Approach with Explicit Delay and Horizon},
   year={2024},
   volume={},
   number={},
   pages={-},
   keywords={Time series;Anomaly Prediction;Anomaly Detection;U-Net;Transformers;},
   url={https://arxiv.org/abs/2408.04377}}
   ```
