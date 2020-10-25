from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = "bookstore.accounts"

    def ready(self):
        super(AccountsConfig, self).ready()

        # noinspection PyUnresolvedReferences
        import bookstore.accounts.signals
