# GPT Exam Answer Validator

<p align="center">
<img src="https://github.com/alfaromeo13/chatGPT-validator/assets/60315689/c092ed10-4da7-47c7-89f1-5877f530419e" alt="drawing"/>
</p>

### Introduction

This script offers an efficient solution for validating free-text answers provided by pupils. By using OpenAI's ChatGPT model, it automates the validation process, saving countless hours that would otherwise be spent manually reviewing each student's response.
It takes a CSV file containing pupil responses, validates them against predefined questions and their expected answers, and updates the CSV with validation results.

### Prerequisites

- Python 3.x
- `csv` library
- `json` library
- `time` library
- `openai` library

### Installation

1. Ensure you have Python installed on your system.
2. Install the required libraries using pip:

```
pip install openai
```

### Usage

Replace "sk-...yTbC" with your OpenAI API key.
Ensure the CSV file (test.csv in this example) contains the questions and pupil responses.
Run the script:
    
```
python3 ./eval.py
```

### Important Notes
- The script uses multi-threading to speed up the validation process.
- Customize the questions and question titles according to your requirements.
