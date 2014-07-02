
from find_dj.models import DJ

dj_name = ["mothershiester", "indanile", "rAt", "bent", "natty boom"]

username = ["mother1", "inda1", "rat1", "boom1", "bent1", "boom1"]

email = ["selina@codeforprogress.org", "indanile@gmail.com", "kikapika@gmail.com", "darby@gmail.com", "ebonydumas@gmail.com"]

password = ["mother1", "inda1", "rat1", "boom1", "bent1", "boom1"]

#Don't worry about indentation for dictionaries
for u in [0,1,2,3,4]:
	u = DJ(dj_name = dj_name[u], username = username[u], email = email[u], password = password[u],)	# Selina: Add comments about what this is about (related to dictionary passing)
	u.save()