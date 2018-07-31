from rasa_core.actions import Action


class ReplyWithName(Action):

    def name(self):
        # you can then use action_example in your stories
        return "reply_with_name"

    def run(self, dispatcher, tracker, domain):
        # what your action should do
        last_entity = next(tracker.get_latest_entity_values("name"),None)
        slots = tracker.current_slot_values()
        dispatcher.utter_message(f'Hallo {tracker.get_slot("name")}')
        dispatcher.utter_message(f'slots are ::::{slots}')
        return [] 
