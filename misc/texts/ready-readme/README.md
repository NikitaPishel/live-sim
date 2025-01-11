# Live Simulator Project

## Contents
[Intro](#Introduction)
[Installation Guide](#Installation-Guide)
[Usage](#Usage)
[Example](#Example)
[Purpose](#Purpose)
[Features](#features-of-the-project)
[License](#./LICENSE.md)
[Contact](#Contact)

---

## Introduction  
The Live-sim project is a tool that can be used for creating and training Neural Networks. It gives a set of functions, which allow a user to create and control NNs. Although this project has a ready model and environment, it is more of a framework with an example than a project, which means it can be modified for any purpose, but main stucture of genome and training will stay the same.

---

## Installation Guide
**After the installation it is recommended to [read the manual](./manuals/manual-short.md).**

Downloading a model is easy and can be implemented if you follow the instructions described bellow.

1. Clone the repo
First of all you need to git clone the repository. Just open your bash and enter the command:
```bash
git clone https://github.com/NikitaPishel/live-sim.git
```

2. install and activate environment
After you have the project installed on your computer, you need to install the environment using command promt:
```bash
python -m venv env
```
Then you need to activate it depending from your command promt you launch one of the commands.
Power Shell:
```bash
env/Scripts/Activate.ps1
```
On other shells:
```bash
env/Scripts/activate.bat
```

3. install packages
After environment is turned on, you need to install python packages:
```bash
pip install -r requirements.txt
```

## Usage

There's 2 different manuals about this project
- [Quickstart](./manuals/manual-short.md): short and user-friendly text which gives the base of the project without any unnecessary details.
- [Full documentation](./manuals/manual-long.md): full with description of the code structure, its capabilities and limits. Good for people who want to deeply and correctly understand the framework and its capabilities.

## Example

There's a built-in example of a ready project, where small cells (agents) learn to move left. It is used for new users to understand how model works, what and how you use it. More detail info can be found on [user manuals](#Usage).

---

## Purpose 

Live-sim also was developed as a fundation for improving my understanding of computing science, its practical implementation and demonstrating my competence as a programmer. This project is not just a tool, it's a challenge to myself. The whole point of a project is to build an AI from scratch, which is a pretty long and complex task. I started it on a set of restrictions, to make it more challenging and interesting:

- The whole model should be built from scratch, so no AI modules or frameworks used (e. g. pyTorch or Tensorflow)
- Only custom data structures (except for built-in to python skeleton, e. g. array or set)
- Model must be able to train
- There should be an environment example that should be user-friendly, so it can be used for learning or showcasing to people who are not very familiar with programming or/and how AI works.
- No AI tools should be used (e. g. ChatGPT, Copilot)

In the end I came up with hybrid model trained by evolutional process. In creation I worked with following topics:

- **Artificial Intelligence:** Creating neural networks from scratch and training them
- **Optimization:** Making code space and time efficient as possible by different methods
- **Custom Data Structures:** Creating DIY queries, binary trees, and directed graphs with loops.  
- **Object-Oriented Programming:** Designing and managing objects for effective code abstraction.
- **Network and server system:** Work with HTTP requests and server-user communication.  
- **Testing:** Finding errors in code with unit tests.  

**Frameworks and Libs:**
- **Flask:** For creating a server.
- **Vue.js:** For frontend UI.  
- **Axios:** For creating HTTP requests.  

---

## Features of the Project  
The project has a range of features designed for model's efficiency and adaptability:  

1. **Hybrid NN Architecture:**  
   Combines features of both **Recurrent Neural Networks** and **Feedforward Neural Networks**. The model supports looped structures in a larger system, giving more dynamic adaptability for varied tasks.

2. **Customizability:**  
   The model is highly flexible. Its core can be trained and used in any imaginable task and will stay with no changes. This allows to use it in a wide range of tasks, from education and grocery to engineering and military.

3. **Efficieny:**  
   For its structute it gives optimal results by using a list of different algorithms and structures.

---

## Contact

For any bugs or this project discussion, **contact me on dedicated for this section** of the repo. For other reasons, use my email.
Email: pogerproger@gmail.com