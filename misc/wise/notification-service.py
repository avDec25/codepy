from abc import ABC, abstractmethod
from typing import Dict


class NotificationProvider(ABC):
    @abstractmethod
    def send(self, recipient: str, message: str):
        pass


class EmailSenderProvider(NotificationProvider):
    def send(self, recipient: str, message: str):
        print(f"Success: Email has been sent to {recipient}")
        return True


class SMSSenderProvider(NotificationProvider):
    def send(self, recipient: str, message: str):
        print(f"Success: SMS has been sent to {recipient}")
        return True


class PushSenderProvider(NotificationProvider):
    def send(self, recipient: str, message: str):
        print(f"Success: Push has been sent to {recipient}")
        return True


class NotificationService:
    def __init__(self):
        self.providers: Dict[str, NotificationProvider] = {}

    def register_provider(self, channel: str, provider: NotificationProvider):
        self.providers[channel] = provider

    def send_notification(self, channel: str, recipient: str, message: str):
        provider = self.providers[channel]
        if not provider:
            raise Exception("No providers are registered for this channel")

        try:
            hasSucceeded = provider.send(recipient, message)
            if hasSucceeded:
                print(f"Success: Notification sent to {recipient}")
            else:
                print("Error: Could not notify")
        except Exception as e:
            print("Error: Could not notify")
            raise e
