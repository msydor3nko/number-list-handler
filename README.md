# API for data processing
The single endpoint API based on Flask framework.
Receive JSON object and handle passed number list using collection of functions from rule in string.

Endpoint: `POST http://0.0.0.0:5000/start/`

JSON example:

```
{
    "data": [1, 2, 3, 4, 5],
    "rule": "a b c d e f"
}
```

## Data processing modes

A number list can be handled in two ways.

1) Applying each function (rule) to all numbers in the list (using by default).

###### Example:
```
Data in request body:

    [1, 2, 3, 4, 5, 6]

Handling:

    [fun_a([1, 2, 3, 4, 5, 6]), ... fun_f([1, 2, 3, 4, 5, 6])]
    
Response result:

    { "result": [ 1, 4, 9, 16, 25, 3, 5, 7, 9, 11, 0, 1, 2, 3, 4, 0.1, 0.2, 0.3, 0.4, 0.5, 11, 12, 13, 14, 15, 0.5, 1.0, 1.5, 2.0, 2.5 ] }
```

2) Applying rules (functions) to ach numbers in the list by pairs.

###### Example:
```
Data in request body:

    [1, 2, 3, 4, 5, 6]

Handling:

    [fun_a(1), fun_b(2), ... fun_f(6)]
    
Response result:

    { "result": [ 1, 5, 2, 0.4, 15 ] }
```

To control handling mode use `RuleDataHandler class` methods:  
`.apply()` or `.apply_by_pairs()` respectively (in `app.py`).


## Project Setup

### You need
Git, Docker Engine, Docker Compose

### Clone project

`git clone https://github.com/msydor3nko/number-list-handler.git`

Enter to the project directory:

`cd number-list-handler`

### Run App in Docker

`docker-compose up`