from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import UserUtteranceReverted

class ActionGreetUser(Action):

	def name(self) -> Text:
		return "action_greet_user"

	def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		dispatcher.utter_message("Hello! Welcome to the openWHO Support Chat. How may I help you?")

		return [UserUtteranceReverted()]