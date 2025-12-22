# AutoJudge: AI-Powered Coding Difficulty Estimator

### [Click Here to Try the Live Demo](https://autojudge-ai-evaluator-shb2ixjb3hyudd4brfvbdz.streamlit.app/)

## The Story Behind This Project
As a developer, People spend a lot of time solving coding problems on platforms like LeetCode. I realized that "difficulty" is often subjective. Sometimes an "Easy" problem feels tricky, and a "Medium" one feels straightforward.

I built **AutoJudge** to see if an AI could objectively rate these problems just by reading their descriptions. The goal was to create a tool that not only categorizes a problem (Easy/Medium/Hard) but also gives it a precise "complexity score" (1-100).

It was an exciting challenge to take raw text data and turn it into a functional, deployed web app!

## My Approach
This wasn't just about feeding data into a model. I had to design a pipeline that "understands" coding terminology. Here is how I broke it down:

### 1. Data Processing
I started with a dataset of coding problems. The text was messy, so I wrote a cleaning script to:
* Remove special characters (like HTML tags).
* Convert everything to lowercase for consistency.
* Remove common "stopwords" (like *the, is, and*) so the model focuses on important keywords.

### 2. Feature Extraction (TF-IDF)
Computers can't read English, so I used **TF-IDF (Term Frequency-Inverse Document Frequency)** to convert the problem descriptions into numbers. This technique highlights unique words (like "recursion" or "array") while ignoring generic words.

### 3. Machine Learning Models
I trained two separate models using **Random Forest**:
* **The Classifier:** To assign the broad label (Easy, Medium, Hard).
* **The Regressor:** To predict a specific score (1-100). This helps differentiate between a "very easy" problem (Score: 10) and a "hard easy" problem (Score: 30).

## Results & Observations
The results were really interesting! The model successfully learned to associate specific technical terms with difficulty:
* **Easy Problems:** Often contain words like *"basic"*, *"loop"*, or *"print"*.
* **Hard Problems:** Are heavily weighted by terms like *"dynamic programming"*, *"tree"*, and *"constraint"*.

The Random Forest model proved to be robust, handling the variations in problem descriptions much better than simpler models like Logistic Regression.

## Repository Structure
Here is a map of the files in this repo:

* `app.py` ➡ The heart of the project. This script runs the Streamlit interface you see in the live demo.
* `Auto_Judge.ipynb` ➡ **The Lab.** This notebook contains my full experiments: data cleaning, visualization, and model training steps.
* `requirements.txt` ➡ A list of libraries (like Scikit-Learn and Pandas) needed to run this in the cloud.
* `*.pkl files` ➡ The "frozen" brain of the AI (the trained models) ready to make predictions.

## 🛠️ Tech Stack
* **Python** (Core Logic)
* **Streamlit** (Frontend/Deployment)
* **Scikit-Learn** (Machine Learning)
* **Pandas & NumPy** (Data Manipulation)

## 💻 How to Run Locally
If you want to test this on your own machine:

1.  **Clone this repository:**
    ```bash
    git clone [https://github.com/DarkyKnight/AutoJudge-AI-Evaluator.git](https://github.com/DarkyKnight/AutoJudge-AI-Evaluator.git)
    ```
2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Launch the app:**
    ```bash
    streamlit run app.py
    ```
