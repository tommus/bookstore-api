from django.apps import AppConfig


class AccountConfig(AppConfig):
    name = "account"

    def ready(self):
        super(AccountConfig, self).ready()

        # noinspection PyUnresolvedReferences
        import account.signals
