import re
CALL_REG = ["hey peggy" , "hello peggy", "peggy" ] 

CALL_RESPONSE = [
"how can i help" , "do you need something" , "what do you need" ,"am here","yes","am listening"
]

TAGS = {"alarm" : 0 , "date":1 , "time":1 , "weather":2}


BASIC_COMMAND = [
	{
		re.compile("[\w\s]+ set alarm"):lambda alarmModule:alarmModule.set_alarm,
		re.compile("set alarm"):lambda alarmModule:alarmModule.set_alarm,
		re.compile("[\w\s]+ show alarms"):lambda alarmModule:alarmModule.show_alarms,
		re.compile("show alarms"):lambda alarmModule:alarmModule.show_alarms,
		re.compile("[\w\s]+ disable all alarm"):lambda alarmModule:alarmModule.remove_alarms,
		re.compile("[\w\s]+ disable all alarms"):lambda alarmModule:alarmModule.remove_alarms,
		re.compile("disable alarm"):lambda alarmModule:alarmModule.remove_alarms,
		re.compile("mute alarm"):lambda alarmModule:alarmModule.mute_alarm,
		re.compile("clear alarms"):lambda alarmModule:alarmModule.remove_alarms,
	},
	{
		re.compile("[\w\s]+ today's date"):lambda timeHelper:timeHelper.today,
		re.compile("[\w\s]+ the time"):lambda timeHelper:timeHelper.current_time,
		re.compile("[\w\s]+ time is it"):lambda timeHelper:timeHelper.current_time,
		re.compile("what time is it"):lambda timeHelper:timeHelper.current_time,
		re.compile("whats the time"):lambda timeHelper:timeHelper.current_time,
		re.compile("[\w\s]+ yesterdays's date"):lambda timeHelper:timeHelper.yesterday,
		re.compile("what date was yesterday"):lambda timeHelper:timeHelper.yesterday,
	},
	{
	
	}
]




