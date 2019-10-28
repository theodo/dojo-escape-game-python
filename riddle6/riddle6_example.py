from peewee import CharField, Model, SqliteDatabase, IntegerField, TextField

db = SqliteDatabase('./riddle6_example.db')


class YoutubeChannel(Model):
    """
        Exemple de modèle correspondant au contenu de la base de données
    """

    name = CharField()
    subscribers = IntegerField()
    cover_image_url = CharField()
    description = TextField()

    def __str__(self):
        """ Décrit comment s'affiche un objet "YoutubeChannel" dans le terminal """
        return self.name + " (" + str(self.subscribers) + " subs)"

    class Meta:
        database = db


db.connect()

sorted_youtube_channel = (
    YoutubeChannel.select()
    .order_by(YoutubeChannel.subscribers)
    .limit(10)
)

for channel in sorted_youtube_channel:
    print(channel)
