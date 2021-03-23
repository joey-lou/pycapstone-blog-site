# pycapstone-blog-site
python capstone project -- blog site


To initalize local dev enviornment, run the following commands
1. install poetry
2. install package dependencies
```
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
poetry install
```

To create new enviornment from requirement file
```
cat requirements.txt|xargs poetry add
```