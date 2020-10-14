from django.apps import AppConfig


class AccountConfig(AppConfig):
    name = "bookstore.account"

    def ready(self):
        super(AccountConfig, self).ready()

        # noinspection PyUnresolvedReferences
        import bookstore.account.signals
