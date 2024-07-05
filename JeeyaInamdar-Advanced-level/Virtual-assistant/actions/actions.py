# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
# import webbrowser
# import os
# from typing import Any, Text, Dict, List
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
# import subprocess

# actions/actions.py
# from typing import Any, Text, Dict, List
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
# import os
# import webbrowser
# class ActionOpenApp(Action):

#     def name(self) -> Text:
#         return "action_open_app"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         dispatcher.utter_message(text="Hello World!")
# app_name = Tracker.get_latest_entity_values("app_name")

# if app_name:
#     dispatcher.utter_message(text=f"Opening {app_name}")
#     # os.system(f"start {app_name}")
# else:
#     dispatcher.utter_message(text="I couldn't find the application name.")

# return []


# class ActionSearchWeb(Action):

#     def name(self) -> Text:
#         return "action_search_web"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         query = tracker.get_slot('query')
#         if query:
#             webbrowser.open(f"https://www.google.com/search?q={query}")
#             dispatcher.utter_message(text=f"Searching for {query}...")
#         else:
#             dispatcher.utter_message(text="I don't know what to search for.")

#         return []

#
# #
# class ActionHelloWorld(Action):

#     def name(self) -> Text:
#         return "action_hello_world"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         dispatcher.utter_message(text="Hello World!")

#         return []
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import os
from rasa_sdk.events import SlotSet
import requests
from googlesearch import search
import webbrowser


class ActionOpenApp(Action):

    def name(self) -> Text:
        return "action_open_app"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        app_name = tracker.get_slot('app')

        if app_name:
            dispatcher.utter_message(text=f"Opening {app_name}")
            # Adjust these commands based on your OS and application paths
            if app_name == 'notepad':
                os.system("notepad.exe")
            elif app_name == 'calculator':
                os.system("calc.exe")
            elif app_name == 'browser':
                os.system("start chrome")  # Assuming Chrome is the browser
            else:
                dispatcher.utter_message(text=f"Sorry, I don't know how to open {app_name}")
        else:
            dispatcher.utter_message(text="I couldn't find the application name.")

        return []


class ActionSearchInBrowser(Action):

    def name(self) -> Text:
        return "action_search_web"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        query = tracker.latest_message.get("text")
        search_url = f"https://www.google.com/search?q={query}"
        webbrowser.open(search_url)
        dispatcher.utter_message(text=f"Opening browser with search results for '{query}'")

        return [SlotSet("query", query)]

# class ActionSearchWeb(Action):

#     def name(self) -> Text:
#         return "action_search_web"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         query = tracker.get_slot("query")
#         if query:
#             dispatcher.utter_message(text=f"Searching for {query}...")
#             search_results = []
#             for url in search(query, num_results=5):
#                 search_results.append(url)
#             response = "\n".join(search_results)
#             dispatcher.utter_message(text=response)
#         else:
#             dispatcher.utter_message(text="I need a query to search.")

#         return [SlotSet("query", None)]