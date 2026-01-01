# Setup 

Once receives the zip:

1. **Extract** the zip to a folder, e.g., `..\resume-analyzer`

2. **Install prerequisites** (Python, Node, PostgreSQL)

3. **Backend Setup**:

```powershell
cd ..\resume-analyzer\src\backend

# Create virtual environment
python -m venv venv

# Activate it
.\venv\Scripts\activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt
```

4. **Database Setup**:

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

5. **Frontend Setup**:

```powershell
cd ..\resume-analyzer\src\frontend
npm install
npm start
```

6. **Run backend**:

```powershell
uvicorn server:app --reload --port 8000
or 
python server.py
```

7. **Run frontend**:

```powershell
cd src\frontend
npm start
```

---
