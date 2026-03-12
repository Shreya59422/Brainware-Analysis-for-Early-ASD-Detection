# Data Description

## Dataset Overview

The dataset used in this project contains EEG brainwave features collected for Autism Spectrum Disorder research.

Total Samples: 383  
Total EEG Features: 12

## Feature Description

The dataset includes the following EEG features:

- delta_F_sx : Delta band power from left frontal region
- delta_F_dx : Delta band power from right frontal region

- theta_F_sx : Theta band power from left frontal region
- theta_F_dx : Theta band power from right frontal region

- low_alpha_F_sx : Low alpha band power from left frontal region
- low_alpha_F_dx : Low alpha band power from right frontal region

- high_alpha_F_sx : High alpha band power from left frontal region
- high_alpha_F_dx : High alpha band power from right frontal region

- beta_F_sx : Beta band power from left frontal region
- beta_F_dx : Beta band power from right frontal region

- gamma_F_sx : Gamma band power from left frontal region
- gamma_F_dx : Gamma band power from right frontal region

## Target Variable

Diagnosis_group represents the diagnostic category.

0 → Non-ASD  
2 → ASD

For model training, this was converted to a binary label:

ASD = 1 → ASD  
ASD = 0 → Non-ASD
