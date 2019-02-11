# Earth Observation Data for Agriculture
Workshop slides, projects and jupyter notebooks for the Medellin 2019 RADA Big Data Summer School

## Contents
This repository contains all of the slides, tutorial notebooks and project notebooks for the workshop in Medellin, Colombia (11th - 15th of February 2019).
### Tutorials
[Optical Satellite Imagery](tutorials/1.%20Optical%20satellite%20imagery)
[Sci-Kit Learn for Image Data](tutorials/2.%20SKLearn%20for%20images.ipynb)
[Image Segmentation with Radar Images](tutorials/3.%20Segmenting%20radar%20images.ipynb)

### Project
A group project using remote sensing data is included in this repository. An overview of the research challenge is provided [here](project/Research%20Questions.ipynb) and we have provided a demonstration on how to access the dataset [here](project/The%20Dataset.ipynb)

### Slides

## Getting Started
Here are the detailed steps you need to get started with this project, using Anaconda. If you are more familiar with a different package manager (e.g. virtualenv), you may prefer to use this.

### 1. Install Anaconda
Before starting any of the project work, it is important to set up Anaconda. First step is to download and install it from https://www.anaconda.com/distribution/

### 2. Clone this repository
Download this whole repository to your local disk and unzip it. If you have git installed, you can just use:
```
git clone https://github.com/joe-fennell/medellin-2019.git
```
### 3. Set up the conda environment

Open a terminal window and navigate to the top level folder of the project repository.

For example, if you downloaded the repository to ```Documents```, then it would be:

```
cd ~/Documents/medellin-2019
```

Once you are in the directory, set up a new environment using the file we provided

```
conda env create -f medellin.yml
```

Now whenever you want to run the code, use:

```
conda activate medellin
```

to run the environment.

### 4. Download Sentinel 2 Data

NB: You only need to do this if you are planning on working on the agri project.

Pre-processed Sentinel 2 data for the project can be downloaded from

https://drive.google.com/file/d/1oSitiedyaYiaElcTfFhvJHUSjJYQQxNU/view?usp=sharing.

Move the data file (```cali_training.nc```) to ```project/geo_data```

### 5. Get started!

Start the environment and launch jupyter notebooks
```
conda activate medellin
jupyter notebook
```
