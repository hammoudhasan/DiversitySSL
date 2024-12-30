# On Pretraining Data Diversity for Self-Supervised Learning


<div align="center">
  Code and models will be released upon acceptance.

<div>
  <a href="https://scholar.google.com/citations?user=Plf1JSIAAAAJ&hl=en">Hasan Abed Al Kader Hammoud</a><sup>1*</sup>&nbsp;&nbsp;
  <a href="https://fr.linkedin.com/in/das-tuhin">Tuhin Das</a><sup>2*</sup>&nbsp;&nbsp;
  <a href="https://fabvio.github.io/">Fabio Pizzati</a><sup>2*</sup>&nbsp;&nbsp;
  <a href="https://scholar.google.com/citations?user=kPxa2w0AAAAJ&hl=en">Philip Torr</a><sup>2</sup>&nbsp;&nbsp;
  <a href="https://www.adelbibi.com/">Adel Bibi</a><sup>2</sup>&nbsp;&nbsp;
  <a href="https://www.bernardghanem.com/">Bernard Ghanem</a><sup>1</sup>
  <br>
  <sup>1</sup> KAUST,
  <sup>2</sup> University of Oxford,
</div>
  
<img src="https://i.ibb.co/PtxXHqc/ssl-teaser.jpg" alt="SynthCLIP Teaser" width="500"> <!-- Sets the width to 500 pixels -->

[![Paper](https://img.shields.io/badge/arXiv-Paper-red?style=for-the-badge&logo=arxiv)](https://arxiv.org/abs/2403.13808) 
[![GitHub stars](https://img.shields.io/github/stars/hammoudhasan/DiversitySSL?style=for-the-badge)](https://github.com/hammoudhasan/DiversitySSL/stargazers)
</div>

## Abstract 
We explore the impact of training with more diverse datasets, characterized by the number of unique samples, on the performance of self-supervised learning (SSL) under a fixed computational budget. Our findings consistently demonstrate that increasing pretraining data diversity enhances SSL performance, albeit only when the distribution distance to the downstream data is minimal. Notably, even with an exceptionally large pretraining data diversity achieved through methods like web crawling or diffusion-generated data, among other ways, the inherent distribution shift remains a challenge. Our experiments are comprehensive with seven SSL methods using large-scale datasets such as ImageNet and YFCC100M amounting to over 200 GPU days. 

## Instructions

Follow the steps below to set up the environment, prepare the dataset, and run the training pipeline:

1. **Create the Conda Environment**  
   Create a Conda environment named `ssl_diversity` with Python 3.10:  
   ```bash
   conda create -n ssl_diversity python=3.10
   conda activate ssl_diversity
   ```

2. **Install Required Packages**  
   Install the required Python packages specified in the `requirements.txt` file:  
   ```bash
   pip install -r requirements.txt
   ```

3. **Install NVIDIA DALI (Optional)**  
   If you plan to use NVIDIA DALI for augmentations, install it using the following command:  
   ```bash
   pip install nvidia-dali-cuda110
   ```

4. **Prepare the Dataset**  
   Run the `create_csv.py` script to generate a CSV file listing the image paths:  
   - Open the script and update the variables as needed:  
     ```python
     root_directory = "some_images"  # Replace with the root directory containing your images
     output_file = "image_paths.csv"  # Specify the desired name of the output CSV file
     ```
   - Execute the script:  
     ```bash
     python create_csv.py
     ```

5. **Update Your YAML Configuration File**  
   Configure the dataset section in your YAML file as follows:  
   ```yaml
   # Dataset configuration
   data:
     dataset: "custom"  # Using custom dataset type for CSV
     train_path: "/home/hammh0a/new/solo-learn/image_paths.csv"  # Path to the generated CSV file
     format: "csv"  # Specify CSV format
     num_workers: 8
     no_labels: True
     fraction: 1.0  # Adjust between 0.0-1.0 for partial dataset use
     root_dir: "./"  # Root directory for relative image paths
     path_column: "path"  # Name of the column containing image paths in CSV
   ```

6. **Control Training Data Fraction**  
   Set the `fraction` parameter in the YAML file to control the percentage of data used during training (e.g., `1.0` for full dataset, `0.5` for 50%).

7. **Run the Training Script**  
   Execute the training process by running the `runner.sh` script. Ensure the correct YAML file is specified in the script:  
   ```bash
   bash runner.sh
   ```
   

## 📖 Citation
If you find this work useful in your research, please consider citing:

```bibtex
@misc{hammoud2024pretraining,
      title={On Pretraining Data Diversity for Self-Supervised Learning}, 
      author={Hasan Abed Al Kader Hammoud and Tuhin Das and Fabio Pizzati and Philip Torr and Adel Bibi and Bernard Ghanem},
      year={2024},
      eprint={2403.13808},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```
