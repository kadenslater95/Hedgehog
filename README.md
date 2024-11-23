### !!! Work in Progress !!!

## Hedgehog
A full stack Data Science application meant to be built upon.

---

### Setup

I recommend using VSCode (I am on Ubuntu, but you can be on Windows or Mac as well)

#### Python
Set up a Python `venv` and install the modules in the requirements.txt
```
python -m venv .venv
```
```
pip install -r requirements.txt
```

#### Database
. . . install Postgres . . .
(or a different db, but you'll have to configure the Alembic and SQLAlchemy setup in config/database.py)

#### dotenv
create a `.env.local` file for storing sensitive information, currently the keys to fill in are (replace fake values with your values)
```
DB_USERNAME=fakeusername
DB_PASSWORD=fakepassword123

```

---

Not ready to run yet.
Run with
```
uvicorn main:app --reload
```