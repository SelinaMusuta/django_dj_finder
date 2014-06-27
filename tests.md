Browser displays 'hello world'. PASS

Browser displays template. FAIL

Browser displays template with form. FAIL

New user signs in with all of the required information (dj name, city(s), email address). FAIL

Dj logs in with valid password. FAIL

Dj logs in with an invalid password and page is redirected to the log-in. FAIL

Dj is able to log out and page is redirected to the log-in.  FAIL

Map displays dj data points. FAIL

DJ is able to change their profile information. FAIL

Promoters or fans write to dj and email is sent. FAIL

Dj has a mix on soundcloud or some other music sharing site and it displays on page. FAIL
=========================================================

DJ Table:
id
dj_name

Genres:
id
name

Performance Table:
id  
time
date
venue_id

Venue:
id
address
age_restriction
city_id


City Table:
id
name
state

Message Table:
id
message 
dj_id




