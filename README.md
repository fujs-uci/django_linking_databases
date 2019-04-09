# django_linking_databases
## Goals
1. Create two Django Projects linked by the same database.
2. Create two user sites with shared models.
3. Have one admin site for both OR two admin sites with same admin users
## Steps

### Setup Projects
1. Create both projects, dblink1 and dblink2
2. Create test1 and test2 app in respective projects
### Linking AUTH_USER_MODEL
3. Create User1 auth_user_model in test1
4. Migrate changes for dblink1.test1
5. Link auth_user_model for dblink2 in settings:
```
import sys
sys.path.append('path/to/dblink1')
import test1
...
INSTALLED_APPS = [
    ...
    'test1.apps.User1Config',
]
...
AUTH_USER_MODEL = test1.User1
```
6. Repeat above code in dblink1 and admin sites will share model registration w/o repeat code.
