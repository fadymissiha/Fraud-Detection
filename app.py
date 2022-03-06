import sys
!{sys.executable} -m pip install -r req.txt --quiet
!FLASK_ENV=development FLASK_APP=wsfraud.py flask run
!curl http://localhost:5000/status