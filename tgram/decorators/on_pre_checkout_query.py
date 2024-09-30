import tgram

from typing import Callable
from tgram.handlers import Handler, Handlers
from tgram.filters import Filter, all


class OnPreCheckoutQuery:
    def on_pre_checkout_query(self=None, filters: Filter = None, group: int = 0):
        def decorator(func: Callable) -> Callable:
            handler = Handler(
                callback=func,
                type=Handlers.PRE_CHECKOUT_QUERY,
                filters=self if isinstance(self, Filter) else (filters or all),
            )
            if isinstance(self, tgram.TgBot):
                self.add_handler(handler, group)
            else:
                if not hasattr(func, "handlers"):
                    func.handlers = []

                func.handlers.append((handler, group))

            return func

        return decorator