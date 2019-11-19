from rasa_sdk import Action, Tracker
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet

class ActionEmailForm(FormAction):

    RANDOMIZE = False

    @staticmethod
    def slot_mappings(self):
        return {
            "email": self.from_entity(entity="email"),
            "new_email": self.from_entity(entity="email"),
            "new_email_confirmed": self.from_intent(intent="conversation_confirm", value=True),
            "conversation_confirm": self.from_intent(intent="conversation_confirm", value=True),
            "conversation_cancel": self.from_intent(intent="conversation_cancel", value=False),
        }
        # return [
        #     EntityFormField("email", "new_email"),
        #     BooleanFormField("new_email_confirmed", "conversation_confirm", "conversation_cancel")
        # ]

    def name(self):
        return 'action_email_form'
    
    def submit(self, dispatcher, tracker, domain):
        email = tracker.get_slot("new_email")
        confirmed = tracker.get_slot("new_email_confirmed")

        print(str(email))

        tracker.update(SlotSet("new_email"))
        tracker.update(SlotSet("new_email_confirmed"))
