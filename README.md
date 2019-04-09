# django_linking_databases
## Goals
1. Create two Django Projects linked by the same database.
2. Create two user sites with shared models.
3. Have one admin site for both sites.
4. Have independent users excusive to their respective sites.
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
### Single Admin Site
6. Repeat above code in dblink1
7. In dblink2.urls, change 'admin/' path to:
```
path('admin/', include('dblink1.urls')),
```
### prevent cross user login
8. Give users an attribute to denote their permission on sites
9. Check for permission on views
