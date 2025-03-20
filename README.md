# # Python + Flask + Postgres

This project provides a backend setup for the Practice Drill form using Python, Flask and Postgres

# # Project set-up

# Install dependancies via the requirements.txt file:

```
pip install -r requirements.txt
```

# Create a test and development database
```
 createdb CLIPPD-DB
 createdb CLIPPD-DB-TEST
```

# Seed the development database
```
python seed_dev_database.py
```

# Run the web server
```
; python app.py
```

# Now visit http://localhost:5001/drills in your browser

Currently the backend is setup to connect to an internal repo (https://github.com/clippd/clippd-app/apps/practice-drills.git ). 