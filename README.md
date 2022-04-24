# Comprehension Analyzer and Solver
A project for the subject - Natural Language Processing (UE19CS334) in PES University
## 📜 Abstract
Question Answering systems have become powerful platforms to understand and retrieve necessary data posed by humans in natural language i.e it’s an advanced form of information retrieval. However, most of the existing models focus on only one single question type like textual, boolean etc. <br>
In this project, the proposed model weighs the type of the question to rightly call appropriate and already established state-of-the-art models. This project establishes that a single model can’t be used across all three datasets namely, SQuAD, DROP and BoolQ. Our model achieves an F1 score of 0.69669 on a newly created dataset comprising data from DROP, SQuAD and BoolQ. <br>
The project involves a flask front end where the user can interact with the application.
## Architecture of the Project
![alt text](https://github.com/HariRaagavTR/comprehension-analyzer-and-solver/blob/main/images/final_high_level_design.png "High Level Design")
## ⚙️ Links to the Datasets
This project involves the use of a customd dataset that is a combination of the three datasets - SQuAD, DROP, BoolQ
The dataset used for this project can be found <a href="https://drive.google.com/drive/folders/1lefpxmGSmhxYmpn5OmUGwsr5RXvOysc3?usp=sharing">here</a>
The complete dataset can be found in the given links below
1. DROP : The link to this dataset can be found <a href="https://allenai.org/data/drop">here</a>
2. SQuAD : The link to this dataset can be found <a href="https://rajpurkar.github.io/SQuAD-explorer/">here</a>
3. BoolQ : The link to this dataset used for this project can be found <a href="https://huggingface.co/datasets/boolq">here</a>
## 💻 Setup and Running the Application
1. Clone the repository using the command
```
git clone git@github.com:HariRaagavTR/comprehension-analyzer-and-solver.git
```
2. Get the additional required python libraries
```
python3 pip install -r requirements.txt
```
3. Download the directories from this <a href="https://drive.google.com/drive/folders/1lefpxmGSmhxYmpn5OmUGwsr5RXvOysc3?usp=sharing">link</a>
4. Make a directory under the root called `resources` and put the above downloaded directories into the just created `resources` directory.
5. Run the application
```
python3 main.py
```
## ⌨️ Input
The input to the application is a context paragraph and a question that is based on the entered context.
## 🖨️ Output
The web front end built using Flask would look like as given below:
![alt text](https://github.com/HariRaagavTR/comprehension-analyzer-and-solver/blob/main/images/Front%20End.png "Output")
## 👨‍💻 Contributors
Member | SRN | Sec 
--- | --- | ---
[Geethika K](https://github.com/Geeth5) | PES2UG19CS127 | B<br>
[Hari Raagav T R](https://github.com/HariRaagavTR) | PES2UG19CS138 | C<br>
[Lakshmi Narayan P](https://github.com/LakshmiNarayanP) | PES2UG19CS200 | D
