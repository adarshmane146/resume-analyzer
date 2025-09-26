# ResumeAnalyzer

## About

ResumeAnalyzer is a DCU Computer Science 4th year project that was created by Darragh McGonigle and Stephen McAleese.

## Description

ResumeAnalyzer is an online web application that enables software engineers to upload and analyze their resumes and learn which skills are in-demand in the job market for software engineers in Ireland.

Both features are powered by information that was acquired by analyzing and extracting insights from thousands of job posts.

<br />

![](./res/project-screenshot.png)

The resume analysis page (above) has the following features:
- **Overall resume score:** based on resume skills and length.
- **Skill frequencies panel:** shows the number of job posts matching each skill keyword.
- **Skill recommendations:** recommends skills similar to those found in the uploaded resume.
- **Matching jobs:** job posts that match the skills found in the resume.

The reports page shows information extracted from the collection of job posts to give an overview of the software engineering job market:
- **Years of experience distribution:** shows how many years of experience are typically required for roles in the tech industry.
- **Skill frequencies:** the number of job posts matching each skill keyword.
- **Job post locations:** shows which locations have the most job posts.
- **Soft skill frequencies:** shows the number of job posts that match each soft skill keyword.

The tree page contains a graph that shows several job roles in the tech industry. Clicking on each graph node shows a list of skills and job posts that match that role.

## Tech stack
- Frontend: ReactJS.
- Backend: FastAPI.
- Analysis: Python, NLTK, scikit-learn, Gensim.
- Database: PostgreSQL, SQLAlchemy.

## How to run the app locally

The app consists of a React front end application and a Python FastAPI server. The app can be run locally by running the front end and back end applications in two different terminals.

### Set up the backend

#### Server setup
1. Create a new virtual environment:
    - `python3 -m venv venv`
    - `source venv/bin/activate`
    - `pip install -r requirements.txt`
2. Run the server: `uvicorn server:app --reload`
3. Go to `http://127.0.0.1:8000` in the browser and check that the server is working correctly.

#### Database setup
The web server uses a PostgreSQL database to store job posts and other information. You need to install PostgreSQL and populate the database so that the server has the data it needs. 

1. First, you need to have PostgreSQL installed. You can install it on macOS with `brew install postgresql`.
2. Change to the `./src/backend` directory and run `python populate_database.py` to copy the job posts and other information stored in CSV files in the `./data` directory into the PostgreSQL database.
3. In a new terminal, log into the PostgreSQL database with `sudo -u postgres psql` and run the `\dt` command to check that the tables were created successfully.
4. Now that the database is populated, run the server with `uvicorn server:app --reload` so that it's ready to work with the frontend.

### Set up the frontend
The ReactJS frontend app displays the web app's user interface.

1. Open a new terminal for running the frontend web app.
2. Change to the `./src/frontend` directory and run `yarn` to install all necessary packages. Upgrade `node-sass` with `yarn add node-sass` if it's causing issues.
3. Run `yarn start` to start the frontend app.
3. Go to `http://localhost:3000` in the browser and upload a resume. If everything was set up correctly, the resume should be analyzed and the results should be displayed in the browser.

### Scraping Scripts
All the scraped data needed to run the app is already stored in CSV files in the `./data` directory.

If you want new data, you can use the scraping scripts to collect new job posts and store them in CSV files.

The LinkedIn scraping script can be run with the `python3 linkedin-jobs-scraping-script.py` command and outputs scraped data to `linkedin-scraped-data.csv`.

The Indeed scraping script can be run with the `python3 indeed-jobs-scraping-script.py` command and outputs scraped data to `indeed-scraped-data.csv`.

## Note
This project was originally created in GitLab before being moved to GitHub. The original GitLab repository can be found here:
https://gitlab.computing.dcu.ie/mcgonid3/2022-ca400-mcgonid3-mcalees2.


---

# Local Setup (Windows 11 + npm)

## 1️⃣ Backend Setup (FastAPI + Python)

```code
# Go to backend folder
cd ..\src\backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
.\venv\Scripts\activate

# Upgrade pip
python -m pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt
```

### Configure Database

```powershell
# Copy example env
copy .env-example .env
```

* Open `.env` in a text editor and set your PostgreSQL credentials, e.g.:

```
username=postgres
password=user_password
host=localhost
port=5432
database=database_name
DATABASE_URL=postgresql://postgres:YourPassword@localhost:5432/resume_analyzer
```

* Create the database:

```powershell
# Open PostgreSQL CLI
psql -U postgres

# Inside psql
CREATE DATABASE resume_analyzer;
\q
```

* Populate database with CSV data:

```powershell
python populate_database.py
```

* Run backend server:

```powershell
uvicorn server:app --reload --port 8000
```

Check FastAPI docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 2️⃣ Frontend Setup (React + npm)

Open **new PowerShell** window:

```powershell
cd E:\Projects\resume-analyzer\src\frontend

# Install dependencies
npm install

# If node-sass errors occur
npm install node-sass

# Start frontend
npm start
```

Frontend runs on: [http://localhost:3000](http://localhost:3000)

> React will call backend at `http://127.0.0.1:8000` by default. Ensure `.env` or API URLs in frontend code point to this URL if needed.

---

## 3️⃣ Quick Checks

* Backend running: visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* Frontend running: visit [http://localhost:3000](http://localhost:3000)
* Upload a resume → frontend calls backend → backend queries Postgres → results shown

---

## 4️⃣ Optional Tips

* To stop servers: **CTRL + C** in each terminal
* If port 3000 or 8000 is busy:

  * Backend: `uvicorn server:app --reload --port 8001`
  * Frontend: `set PORT=3001 && npm start`
* If `psycopg2` errors: `pip install psycopg2-binary`
* If spaCy errors: `python -m spacy download en_core_web_sm`

---

---

# Setup 

Once receives the zip:

1. **Extract** the zip to a folder, e.g., `E:\Projects\resume-analyzer`

2. **Install prerequisites** (Python, Node, PostgreSQL)

3. **Backend Setup**:

```powershell
cd E:\Projects\resume-analyzer\src\backend

# Create virtual environment
python -m venv venv

# Activate it
.\venv\Scripts\activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt
```

4. **Frontend Setup**:

```powershell
cd E:\Projects\resume-analyzer\src\frontend
npm install
npm start
```

5. **Database Setup**:

* Create PostgreSQL DB:

```powershell
psql -U postgres
CREATE DATABASE resume_analyzer;
\q
```

* Update `.env` in backend with correct DB password

* Populate database:

```powershell
cd src\backend
python populate_database.py
```

6. **Run backend**:

```powershell
uvicorn server:app --reload --port 8000
```

7. **Run frontend**:

```powershell
cd src\frontend
npm start
```

---
