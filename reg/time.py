import re
from helpers.time_helper import today , yesterday,current_time

BOT_NAME = "peggy"

TIME_DATE_REG = {
	re.compile(f"{BOT_NAME}+ [\w\s] + today's date"):today,
	re.compile(f"{BOT_NAME}+ [\w\s] + the time"):current_time,
	re.compile(f"{BOT_NAME}+ [\w\s] + today's date"):yesterday,
}
