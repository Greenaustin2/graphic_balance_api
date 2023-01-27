import datetime

d = datetime.datetime.utcnow()
print(d.isoformat('T') + 'Z')

