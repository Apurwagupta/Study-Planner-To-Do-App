# Study Planner & To-Do App

A simple Streamlit mini app for students to plan study tasks, track deadlines, and monitor progress.

## Features

- Add a task with subject, due date, priority, and optional notes
- Mark tasks as completed or pending
- View total, completed, pending, and overdue task counts
- Filter tasks by status
- Sort tasks by due date, priority, or subject
- Delete individual tasks or clear all completed tasks
- Detect overdue tasks

## Technologies Used

- Python
- Streamlit

## Run Locally

1. Install Python 3.9 or newer.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Start the app:

   ```bash
   streamlit run app.py
   ```

6. Open the local URL shown in the terminal.

## Deploy on Streamlit Community Cloud

1. Upload `app.py`, `requirements.txt`, and this `README.md` to a GitHub repository.
2. Sign in to Streamlit Community Cloud using your GitHub account.
3. Choose **Create app** and select your repository, branch, and `app.py` as the main file.
4. Deploy the app and open the generated public URL.

## Important Note

This beginner version stores tasks in Streamlit session state. Tasks are not saved permanently in a database and may reset when the session restarts. Persistent storage can be added as an extension.

## Student Details

- **Student:** Apurwa
- **Roll Number:** 06
- **Faculty Guide:** Anil Walke
- **College:** ISBM College of Engineering, Nande, Pune
- **Department:** Artificial Intelligence and Data Science
- **Academic Year:** 2026–2027
