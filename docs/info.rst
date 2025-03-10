General Information
**************************

Assumptions
-----------------------------------------
Whily PyTorch-OOD aims to be general, there are certain assumptions that we have to make.
These are as follows:


OOD as Binary Classification
=============================
PyTorch-OOD casts OOD detection as binary classification with the goal to discriminate between
in-distribution (IN) and out-of-distribution (OOD) data. This
detection is performed in addition to other tasks, like classification or segmentation.
Thus, it is assumed that each **OOD detector produces outlier scores**, where high values indicate greater outlierness.
While these are strong assumptions that some detectors, like OpenMax, might not adhere to,
we argue that most methods can be reformulated in such a fashion.

Workflow
==============
We assume a workflow involving 3 Steps:

1. Training a Deep Neural Network
2. Creating an OOD detector, which is optionally fitted on some training data.
3. Evaluating the OOD detector on some benchmark dataset

Labeling
===============

We adopt the following convention: samples from in-distribution data use target class labels :math:`>= 0`.
Samples from out-of-distribution data (known or unknown during training) will be assigned target values :math:`< 0`.



Scope
-----------------------------------------

While Out-of-Distribution detection, Anomaly Detection, Novelty Detection, Open-Set recognition etc. differ in details,
we believe that these tasks are related. To out knowledge, the nomenclature is not fully settled, and different
researchers tend to use different terminologies.
Sometimes, some of these terms are used interchangeably.
Therefore, while this packages aims at out-of-distribution methods, it also covers methods from closely related fields.
