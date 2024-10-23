# Dashboard Project for Grazioso Salvare

This repository contains the final code for the dashboard project for Grazioso Salvare. It includes both the dashboard code and the CRUD Python module used for MongoDB operations. The project allows Grazioso Salvare, a rescue-animal training company, to interact with their database of animal shelter data through an intuitive web dashboard. Below are my reflections on the work done for this project and how it fits into my learning as a computer science student.

<img width="795" alt="image" src="https://github.com/user-attachments/assets/34f23e40-dedf-43dd-abe8-3629ff046989">


## Reflections

To write maintainable, readable, and adaptable programs, I focus on using good coding practices such as writing modular code, using clear and descriptive variable names, and following consistent formatting. For this project, I created a reusable CRUD Python module to handle interactions with MongoDB. This module helped manage the database queries, and I was able to use it throughout the dashboard project without needing to rewrite code.

By keeping the code modular and organized, it is easier to maintain and update as needed. This also ensures that if any new features or changes are required in the future, they can be easily integrated without disrupting the overall functionality of the project. The CRUD module could be reused in future projects that require database operations, making it highly adaptable.

When approaching a problem, I start by understanding the requirements and breaking the task down into smaller steps. For the Grazioso Salvare project, the first task was to establish the database and build the CRUD operations. Once the database was functional, I worked on creating the dashboard interface, connecting the database queries to the widgets on the front-end.

I typically approach each problem incrementally, testing each part of the solution as I go. This way, I can catch any issues early on and ensure that each component works before moving on to the next. This project differed from previous assignments because of the added complexity of integrating a real-time database and a front-end dashboard. In the future, I plan to apply this step-by-step approach to similar projects involving client data and user interfaces.

Computer scientists solve real-world problems by designing and developing software that improves processes and solves complex issues. In this project, my role was to create a dashboard that allows Grazioso Salvare to easily identify dogs for rescue training. This software helps them save time, reduce errors, and improve the overall efficiency of their operations.

In a broader context, computer scientists build tools and systems that enable organizations to operate more efficiently and make better decisions. By handling large sets of data and creating intuitive interfaces, computer scientists play a critical role in driving innovation and improving the way organizations work.

## Repository Information

This repository contains the following artifacts:
- **ProjectTwoDashboard.ipynb** - The Jupyter Notebook containing the code for the dashboard.
- **animal_shelter.py** - The Python module used for MongoDB CRUD operations.
- **README.md** - Documentation that describes the functionality of the project and instructions for reproducing it.

## Instructions for Reproduction

To reproduce this project:
1. Install the necessary dependencies (MongoDB, Dash, pandas, etc.).
2. Set up a MongoDB database with the provided CSV data using the CRUD module.
3. Run the Jupyter Notebook file to start the dashboard.
4. The dashboard allows for filtering by rescue type and shows data dynamically in a table and charts.

For more detailed instructions, please refer to the comments in the code

## Challenges and Solutions

During this project, one challenge was integrating the CRUD module with the dashboard widgets to ensure real-time updates. By testing each query and widget individually, I was able to ensure that all components worked seamlessly together. Future projects will benefit from this modular approach, which allows for easy troubleshooting and testing.

---

