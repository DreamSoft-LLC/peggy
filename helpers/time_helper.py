from datetime import datetime, timedelta

def today():
	return datetime.utcnow().date()

def yesterday():
	return datetime.utcnow().date() - timedelta(days=1)

def current_time():
	now = datetime.utcnow()
	return f"{now.minute} : {now.hour}"

