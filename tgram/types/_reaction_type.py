import tgram
from .type_ import Type_

from typing import Optional


class ReactionType(Type_):
    """
    This object represents a reaction type.

    Telegram documentation: https://core.telegram.org/bots/api#reactiontype

    :param type: Type of the reaction
    :type type: :obj:`str`

    :return: Instance of the class
    :rtype: :class:`ReactionType`
    """

    def __init__(
        self,
        type: "str" = None,
        emoji: "str" = None,
        me: "tgram.TgBot" = None,
        json: "dict" = None,
    ):
        super().__init__(me=me, json=json)
        self.type = type
        self.emoji = emoji

    @staticmethod
    def _parse(
        me: "tgram.TgBot" = None, d: dict = None, force: bool = None
    ) -> Optional["tgram.types.ReactionType"]:
        return (
            ReactionType(me=me, json=d, type=d.get("type"), emoji=d.get("emoji"))
            if d and (force or me and __class__.__name__ not in me._custom_types)
            else None
            if not d
            else Type_._custom_parse(
                __class__._parse(me=me, d=d, force=True),
                me._custom_types.get(__class__.__name__),
            )
        )
