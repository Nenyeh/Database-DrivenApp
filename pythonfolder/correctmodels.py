from peewee import *
import datetime

## 1. The name of your database here
db = 'chukwuemekan'
un = 'chukwuemekan' # likely root still
#pw = 'password' # initially it was also root

#introspector = Introspector.from_database(db)
#models = introspector.generate_models()
pg_db = PostgresqlDatabase(db, user=un)
#pg_db = PostgresqlDatabase(host="localhost", user="CHUKWUEMEKAN", passwd="PASSWORD", database="CHUKWUEMEKAN")
#pg_db = PostgresqlDatabase('chukwuemekan', user='chukwuemekan') #this works but does not work when you do from correctmodel import db
#pg_db = PostgresqlDatabase('chukwuemekan', user='chukwuemekan')

## This is the Base class that Peewee uses to interact with the Postgres DB.
## Don't change it!
## All your model classes should inherit from this BaseModel class
class BaseModel(Model):
        class Meta:
                database = pg_db

## 2. PUT YOUR MODELS HERE (replace the Stations class with your own classes)
class Science_organization(BaseModel):
        org_id      = PrimaryKeyField()
        org_name    = CharField(max_length = 1000)
        org_url     = CharField(max_length = 1000)
        org_type    = CharField(max_length = 300)
        #lat = CharField(max_length=20)
        #lng = CharField(max_length=20)

        def __str__(self):
                return str(self.org_name)


class Statements(BaseModel):
    statement_id        = PrimaryKeyField()
    statement_url       = CharField(max_length = 1000)
    date_posted          = DateTimeField(default=datetime.datetime.now)
    text                 = CharField(max_length = 5000)
    word_count           = IntegerField()
    twitter_post         = CharField(max_length = 100)
    text_format          = CharField(max_length = 1000)
    subtext_format       = CharField(max_length = 1000)
    image                = CharField(max_length = 500)
    image_accessibility  = CharField(max_length = 100)
    has_action_plans      = CharField(max_length = 100)
    post_writer          = CharField(max_length = 1000)
    org_id               = ForeignKeyField(Science_organization, backref = 'statements')

    def __str__(self):
            return str(self.statement_id)


## CALL .connect() on your database whenever you want to execute a query,
## and then .close() when the query is finished
## Make sure you save your result table!
#pg_db.connect()
#result = Statements.select()
#result = Science_organization.select()
#for r in result:
	#print(r)

#pg_db.close()
