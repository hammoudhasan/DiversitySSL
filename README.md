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
