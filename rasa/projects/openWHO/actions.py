from typing import Text, Dict, Any, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, SessionStarted
from sanic.request import Request
from rasa_sdk.executor import CollectingDispatcher

import requests
import json

class CourseSet(Action):
	def name(self):
		return "action_course_set"

	def run(self, dispatcher, tracker, domain):
		currentCourse = tracker.get_slot('current_course')
		if currentCourse:
			return [SlotSet('course-set', True)]
		else:
			return [SlotSet('course-set', False)]

class SetCurrentCourse(Action):
	def name(self):
		return "action_set_current_course"

	def run(self, dispatcher, tracker, domain):
		currentCourse = tracker.latest_message['text']
		return [SlotSet('current_course', currentCourse)]

class ActionGetCourses(Action):
	def name(self) -> Text:
		return "action_get_courses"

	def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		current_state = tracker.current_state()
		token = current_state['sender_id']
		r = requests.get('http://localhost:3000/bridges/chatbot/my_courses', headers={"content-type": "application/json",
		"Authorization": 'Bearer {0}'.format(token)})
		status = r.status_code
		if status == 200:
			response = json.loads(r.content)
			dispatcher.utter_message('You are currently enrolled in these courses:')
			for course in response:
				title = course['title']
				dispatcher.utter_message(title)
			return [SlotSet('all_courses', response)]
		else:
			return []

	class ActionGetAchievements(Action):
		def name(self) -> Text:
			return "action_get_achievements"

		def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
			current_state = tracker.current_state()
			token = current_state['sender_id']
			slots = tracker.slots
			print(slots)
			r = requests.get('http://localhost:3000/bridges/chatbot/my_courses/00000001-3300-4444-9999-000000000001/achievements', headers={"content-type": "application/json",
			"Authorization": 'Bearer {0}'.format(token)})
			status = r.status_code
			if status == 200:
				response = json.loads(r.content)
				dispatcher.utter_message('YEEEEAH')
				# print(response)
			return []