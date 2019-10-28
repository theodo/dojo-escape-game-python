from peewee import CharField, Model, SqliteDatabase, IntegerField, BooleanField

db = SqliteDatabase('./riddle6.db')


class BaseModel(Model):
    class Meta:
        database = db


class Mafioso(BaseModel):
    bitcoin_ptf = CharField()
    category = CharField()
    is_active = BooleanField()
    latitude = CharField()
    longitude = CharField()
    level = IntegerField()

    def __str__(self):
        return self.bitcoin_ptf

    def to_json(self):
        return {
            "bitcoin_ptf": self.bitcoin_ptf,
            "is_active": self.is_active,
            "category": self.category,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "level": self.level,
        }


db.connect()

print(
    Mafioso.select()
    .filter(Mafioso.category == "C")
    .filter(Mafioso.is_active == True)
    .order_by(-Mafioso.level)
    .get()
    .to_json()
)
