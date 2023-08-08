

<!-- PROJECT LOGO -->
<p align="center">
  <a href="#">
    <img src="#" alt="Logo" width="80" height="80">
  </a>

  <h2 align="center">Manuscript Matcher</h2>

  <p align="center">
    A NLP Text Classification Project to match manuscripts or research articles with journals based on the title and abstract of the manuscript.
  </p>
</p>



<p align="center">
  <img src="#" width="800" />
</p>


<!-- TABLE OF CONTENTS -->
## Table of Contents

- [Table of Contents](#table-of-contents)
- [About The Project](#about-the-project)
  - [Data Collection](#data-collection)
  - [Model Training](#model-training)
  - [Deployment](#deployment)
  - [Demo](#demo)
- [Dataset](#dataset)
- [Built With](#built-with)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [License](#license)
- [Contact](#contact)
 

<!-- ABOUT THE PROJECT -->
## About The Project

A NLP Text Classification Project to match manuscripts or research articles with journals based on the title and abstract of the manuscript. A dataset of 30k+ manuscript metadata is scraped from DOAJ and a dataset of 18k+ journals is taken from a Journal Ranking project. State-of-the-art NLP models such as BERT, RoBERTa, and DistilBERT are used to train the model. The model is deployed using Flask and Render. The project is divided into 3 parts: Data Collection, Model Training, and Deployment.

### Data Collection

The data collection is done in 2 parts. The first part is to collect the metadata of the journals from DOAJ. The second part is to collect the metadata of the journals from the Journal Ranking project. The data collection is done using the Scrapy framework. The data is then cleaned and preprocessed to remove any null values and duplicates.

### Model Training

The model training is done using the Hugging Face Transformers library. The model is trained using the BERT, RoBERTa, and DistilBERT models. The model is trained using the title and abstract of the manuscript and the title of the journal. The model is trained using the PyTorch framework. The model is trained using the Google Colab platform.

### Deployment

The model is deployed using the Flask framework. The model is deployed using the Render platform. The model is deployed using the Docker containerization platform.

### Demo

The demo of the project is available at: https://manuscript-matcher.onrender.com/


<!-- DATASET -->
## Dataset

The dataset used in the project is available at: https://www.kaggle.com/


<!-- BUILT WITH -->
## Built With

* [Python](https://www.python.org/)
* [Selenium](https://www.selenium.dev/)
* [Hugging Face Transformers](https://huggingface.co/transformers/)
* [PyTorch](https://pytorch.org/)
* [Flask](https://flask.palletsprojects.com/)
* [Render](https://render.com/)


## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

* Python
* Selenium
* Hugging Face Transformers
* PyTorch
* Flask
* Render

### Installation

1. Clone the repo
```sh

```

2. Install Python packages
```sh

```

3. Run the project
```sh

```


<!-- OTHERS -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact
