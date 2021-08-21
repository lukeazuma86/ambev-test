# Google automated account create

## How to Run

1- Create a virtual enviroment
'''
python3 -m venv venv
'''

2- Activate your venv
'''
.\venv\Scripts\activate
'''

3-Export enviroment variables
'''
set $(cat .env | xargs)
'''

4-Install the dependencies
'''
pip install --no-cache-dir -r requirements.txt
'''

5-Run
'''
python -m google.py
'''