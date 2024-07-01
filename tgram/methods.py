# This is auto generated file, if you found any issue, please report me here: https://github.com/2ei/tgram/issues/new

from typing import List, Union
import tgram
from .types import (
    Update,
    InputFile,
    WebhookInfo,
    User,
    Message,
    MessageEntity,
    LinkPreviewOptions,
    ReplyParameters,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    ForceReply,
    MessageId,
    InputPollOption,
    ReactionType,
    UserProfilePhotos,
    File,
    ChatPermissions,
    ChatInviteLink,
    ChatFullInfo,
    ChatMember,
    Sticker,
    ForumTopic,
    UserChatBoosts,
    BusinessConnection,
    BotCommand,
    BotCommandScope,
    BotName,
    BotDescription,
    BotShortDescription,
    MenuButton,
    ChatAdministratorRights,
    InputMedia,
    Poll,
    StickerSet,
    InputSticker,
    MaskPosition,
    InlineQueryResult,
    InlineQueryResultsButton,
    SentWebAppMessage,
    LabeledPrice,
    ShippingOption,
    StarTransactions,
    PassportElementError,
    GameHighScore,
    InputPaidMedia,
)


class TelegramBotMethods:
    async def get_updates(
        self: "tgram.TgBot",
        offset: int = None,
        limit: int = None,
        timeout: int = None,
        allowed_updates: List[str] = None,
    ) -> List[Update]:
        """https://core.telegram.org/bots/api/#getupdates"""
        result = await self._send_request(
            "getUpdates",
            offset=offset,
            limit=limit,
            timeout=timeout,
            allowed_updates=allowed_updates,
        )
        return [Update._parse(me=self, d=i) for i in result["result"]]

    async def set_webhook(
        self: "tgram.TgBot",
        url: str,
        certificate: InputFile = None,
        ip_address: str = None,
        max_connections: int = None,
        allowed_updates: List[str] = None,
        drop_pending_updates: bool = None,
        secret_token: str = None,
    ) -> bool:
        """https://core.telegram.org/bots/api/#setwebhook"""
        result = await self._send_request(
            "setWebhook",
            url=url,
            certificate=certificate,
            ip_address=ip_address,
            max_connections=max_connections,
            allowed_updates=allowed_updates,
            drop_pending_updates=drop_pending_updates,
            secret_token=secret_token,
        )
        return result["result"]

    async def delete_webhook(
        self: "tgram.TgBot", drop_pending_updates: bool = None
    ) -> bool:
        """https://core.telegram.org/bots/api/#deletewebhook"""
        result = await self._send_request(
            "deleteWebhook",
            drop_pending_updates=drop_pending_updates,
        )
        return result["result"]

    async def get_webhook_info(self: "tgram.TgBot") -> WebhookInfo:
        """https://core.telegram.org/bots/api/#getwebhookinfo"""
        result = await self._send_request(
            "getWebhookInfo",
        )
        return WebhookInfo._parse(me=self, d=result["result"])

    async def get_me(self: "tgram.TgBot") -> User:
        """https://core.telegram.org/bots/api/#getme"""
        result = await self._send_request(
            "getMe",
        )
        return User._parse(me=self, d=result["result"])

    async def log_out(self: "tgram.TgBot") -> bool:
        """https://core.telegram.org/bots/api/#logout"""
        result = await self._send_request(
            "logOut",
        )
        return result["result"]

    async def close(self: "tgram.TgBot") -> bool:
        """https://core.telegram.org/bots/api/#close"""
        result = await self._send_request(
            "close",
        )
        return result["result"]

    async def send_message(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        text: str,
        business_connection_id: str = None,
        message_thread_id: int = None,
        parse_mode: str = None,
        entities: List[MessageEntity] = None,
        link_preview_options: LinkPreviewOptions = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        message_effect_id: str = None,
        reply_parameters: ReplyParameters = None,
        reply_markup: Union[
            InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply
        ] = None,
    ) -> Message:
        """https://core.telegram.org/bots/api/#sendmessage"""
        result = await self._send_request(
            "sendMessage",
            chat_id=chat_id,
            text=text,
            business_connection_id=business_connection_id,
            message_thread_id=message_thread_id,
            parse_mode=parse_mode or self.parse_mode,
            entities=entities,
            link_preview_options=link_preview_options or self.link_preview_options,
            disable_notification=disable_notification,
            protect_content=protect_content
            if protect_content is not None
            else self.protect_content,
            message_effect_id=message_effect_id,
            reply_parameters=reply_parameters,
            reply_markup=reply_markup,
        )
        return Message._parse(me=self, d=result["result"])

    async def forward_message(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        from_chat_id: Union[int, str],
        message_id: int,
        message_thread_id: int = None,
        disable_notification: bool = None,
        protect_content: bool = None,
    ) -> Message:
        """https://core.telegram.org/bots/api/#forwardmessage"""
        result = await self._send_request(
            "forwardMessage",
            chat_id=chat_id,
            from_chat_id=from_chat_id,
            message_id=message_id,
            message_thread_id=message_thread_id,
            disable_notification=disable_notification,
            protect_content=protect_content
            if protect_content is not None
            else self.protect_content,
        )
        return Message._parse(me=self, d=result["result"])

    async def forward_messages(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        from_chat_id: Union[int, str],
        message_ids: List[int],
        message_thread_id: int = None,
        disable_notification: bool = None,
        protect_content: bool = None,
    ) -> List[MessageId]:
        """https://core.telegram.org/bots/api/#forwardmessages"""
        result = await self._send_request(
            "forwardMessages",
            chat_id=chat_id,
            from_chat_id=from_chat_id,
            message_ids=message_ids,
            message_thread_id=message_thread_id,
            disable_notification=disable_notification,
            protect_content=protect_content
            if protect_content is not None
            else self.protect_content,
        )
        return [MessageId._parse(me=self, d=i) for i in result["result"]]

    async def copy_message(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        from_chat_id: Union[int, str],
        message_id: int,
        message_thread_id: int = None,
        caption: str = None,
        parse_mode: str = None,
        caption_entities: List[MessageEntity] = None,
        show_caption_above_media: bool = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        reply_parameters: ReplyParameters = None,
        reply_markup: Union[
            InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply
        ] = None,
    ) -> MessageId:
        """https://core.telegram.org/bots/api/#copymessage"""
        result = await self._send_request(
            "copyMessage",
            chat_id=chat_id,
            from_chat_id=from_chat_id,
            message_id=message_id,
            message_thread_id=message_thread_id,
            caption=caption,
            parse_mode=parse_mode or self.parse_mode,
            caption_entities=caption_entities,
            show_caption_above_media=show_caption_above_media,
            disable_notification=disable_notification,
            protect_content=protect_content
            if protect_content is not None
            else self.protect_content,
            reply_parameters=reply_parameters,
            reply_markup=reply_markup,
        )
        return MessageId._parse(me=self, d=result["result"])

    async def copy_messages(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        from_chat_id: Union[int, str],
        message_ids: List[int],
        message_thread_id: int = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        remove_caption: bool = None,
    ) -> List[MessageId]:
        """https://core.telegram.org/bots/api/#copymessages"""
        result = await self._send_request(
            "copyMessages",
            chat_id=chat_id,
            from_chat_id=from_chat_id,
            message_ids=message_ids,
            message_thread_id=message_thread_id,
            disable_notification=disable_notification,
            protect_content=protect_content
            if protect_content is not None
            else self.protect_content,
            remove_caption=remove_caption,
        )
        return [MessageId._parse(me=self, d=i) for i in result["result"]]

    async def send_photo(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        photo: Union[InputFile, str],
        business_connection_id: str = None,
        message_thread_id: int = None,
        caption: str = None,
        parse_mode: str = None,
        caption_entities: List[MessageEntity] = None,
        show_caption_above_media: bool = None,
        has_spoiler: bool = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        message_effect_id: str = None,
        reply_parameters: ReplyParameters = None,
        reply_markup: Union[
            InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply
        ] = None,
    ) -> Message:
        """https://core.telegram.org/bots/api/#sendphoto"""
        result = await self._send_request(
            "sendPhoto",
            chat_id=chat_id,
            photo=photo,
            business_connection_id=business_connection_id,
            message_thread_id=message_thread_id,
            caption=caption,
            parse_mode=parse_mode or self.parse_mode,
            caption_entities=caption_entities,
            show_caption_above_media=show_caption_above_media,
            has_spoiler=has_spoiler,
            disable_notification=disable_notification,
            protect_content=protect_content
            if protect_content is not None
            else self.protect_content,
            message_effect_id=message_effect_id,
            reply_parameters=reply_parameters,
            reply_markup=reply_markup,
        )
        return Message._parse(me=self, d=result["result"])

    async def send_audio(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        audio: Union[InputFile, str],
        business_connection_id: str = None,
        message_thread_id: int = None,
        caption: str = None,
        parse_mode: str = None,
        caption_entities: List[MessageEntity] = None,
        duration: int = None,
        performer: str = None,
        title: str = None,
        thumbnail: Union[InputFile, str] = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        message_effect_id: str = None,
        reply_parameters: ReplyParameters = None,
        reply_markup: Union[
            InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply
        ] = None,
    ) -> Message:
        """https://core.telegram.org/bots/api/#sendaudio"""
        result = await self._send_request(
            "sendAudio",
            chat_id=chat_id,
            audio=audio,
            business_connection_id=business_connection_id,
            message_thread_id=message_thread_id,
            caption=caption,
            parse_mode=parse_mode or self.parse_mode,
            caption_entities=caption_entities,
            duration=duration,
            performer=performer,
            title=title,
            thumbnail=thumbnail,
            disable_notification=disable_notification,
            protect_content=protect_content
            if protect_content is not None
            else self.protect_content,
            message_effect_id=message_effect_id,
            reply_parameters=reply_parameters,
            reply_markup=reply_markup,
        )
        return Message._parse(me=self, d=result["result"])

    async def send_document(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        document: Union[InputFile, str],
        business_connection_id: str = None,
        message_thread_id: int = None,
        thumbnail: Union[InputFile, str] = None,
        caption: str = None,
        parse_mode: str = None,
        caption_entities: List[MessageEntity] = None,
        disable_content_type_detection: bool = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        message_effect_id: str = None,
        reply_parameters: ReplyParameters = None,
        reply_markup: Union[
            InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply
        ] = None,
    ) -> Message:
        """https://core.telegram.org/bots/api/#senddocument"""
        result = await self._send_request(
            "sendDocument",
            chat_id=chat_id,
            document=document,
            business_connection_id=business_connection_id,
            message_thread_id=message_thread_id,
            thumbnail=thumbnail,
            caption=caption,
            parse_mode=parse_mode or self.parse_mode,
            caption_entities=caption_entities,
            disable_content_type_detection=disable_content_type_detection,
            disable_notification=disable_notification,
            protect_content=protect_content
            if protect_content is not None
            else self.protect_content,
            message_effect_id=message_effect_id,
            reply_parameters=reply_parameters,
            reply_markup=reply_markup,
        )
        return Message._parse(me=self, d=result["result"])

    async def send_video(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        video: Union[InputFile, str],
        business_connection_id: str = None,
        message_thread_id: int = None,
        duration: int = None,
        width: int = None,
        height: int = None,
        thumbnail: Union[InputFile, str] = None,
        caption: str = None,
        parse_mode: str = None,
        caption_entities: List[MessageEntity] = None,
        show_caption_above_media: bool = None,
        has_spoiler: bool = None,
        supports_streaming: bool = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        message_effect_id: str = None,
        reply_parameters: ReplyParameters = None,
        reply_markup: Union[
            InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply
        ] = None,
    ) -> Message:
        """https://core.telegram.org/bots/api/#sendvideo"""
        result = await self._send_request(
            "sendVideo",
            chat_id=chat_id,
            video=video,
            business_connection_id=business_connection_id,
            message_thread_id=message_thread_id,
            duration=duration,
            width=width,
            height=height,
            thumbnail=thumbnail,
            caption=caption,
            parse_mode=parse_mode or self.parse_mode,
            caption_entities=caption_entities,
            show_caption_above_media=show_caption_above_media,
            has_spoiler=has_spoiler,
            supports_streaming=supports_streaming,
            disable_notification=disable_notification,
            protect_content=protect_content
            if protect_content is not None
            else self.protect_content,
            message_effect_id=message_effect_id,
            reply_parameters=reply_parameters,
            reply_markup=reply_markup,
        )
        return Message._parse(me=self, d=result["result"])

    async def send_animation(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        animation: Union[InputFile, str],
        business_connection_id: str = None,
        message_thread_id: int = None,
        duration: int = None,
        width: int = None,
        height: int = None,
        thumbnail: Union[InputFile, str] = None,
        caption: str = None,
        parse_mode: str = None,
        caption_entities: List[MessageEntity] = None,
        show_caption_above_media: bool = None,
        has_spoiler: bool = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        message_effect_id: str = None,
        reply_parameters: ReplyParameters = None,
        reply_markup: Union[
            InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply
        ] = None,
    ) -> Message:
        """https://core.telegram.org/bots/api/#sendanimation"""
        result = await self._send_request(
            "sendAnimation",
            chat_id=chat_id,
            animation=animation,
            business_connection_id=business_connection_id,
            message_thread_id=message_thread_id,
            duration=duration,
            width=width,
            height=height,
            thumbnail=thumbnail,
            caption=caption,
            parse_mode=parse_mode or self.parse_mode,
            caption_entities=caption_entities,
            show_caption_above_media=show_caption_above_media,
            has_spoiler=has_spoiler,
            disable_notification=disable_notification,
            protect_content=protect_content
            if protect_content is not None
            else self.protect_content,
            message_effect_id=message_effect_id,
            reply_parameters=reply_parameters,
            reply_markup=reply_markup,
        )
        return Message._parse(me=self, d=result["result"])

    async def send_voice(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        voice: Union[InputFile, str],
        business_connection_id: str = None,
        message_thread_id: int = None,
        caption: str = None,
        parse_mode: str = None,
        caption_entities: List[MessageEntity] = None,
        duration: int = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        message_effect_id: str = None,
        reply_parameters: ReplyParameters = None,
        reply_markup: Union[
            InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply
        ] = None,
    ) -> Message:
        """https://core.telegram.org/bots/api/#sendvoice"""
        result = await self._send_request(
            "sendVoice",
            chat_id=chat_id,
            voice=voice,
            business_connection_id=business_connection_id,
            message_thread_id=message_thread_id,
            caption=caption,
            parse_mode=parse_mode or self.parse_mode,
            caption_entities=caption_entities,
            duration=duration,
            disable_notification=disable_notification,
            protect_content=protect_content
            if protect_content is not None
            else self.protect_content,
            message_effect_id=message_effect_id,
            reply_parameters=reply_parameters,
            reply_markup=reply_markup,
        )
        return Message._parse(me=self, d=result["result"])

    async def send_video_note(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        video_note: Union[InputFile, str],
        business_connection_id: str = None,
        message_thread_id: int = None,
        duration: int = None,
        length: int = None,
        thumbnail: Union[InputFile, str] = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        message_effect_id: str = None,
        reply_parameters: ReplyParameters = None,
        reply_markup: Union[
            InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply
        ] = None,
    ) -> Message:
        """https://core.telegram.org/bots/api/#sendvideonote"""
        result = await self._send_request(
            "sendVideoNote",
            chat_id=chat_id,
            video_note=video_note,
            business_connection_id=business_connection_id,
            message_thread_id=message_thread_id,
            duration=duration,
            length=length,
            thumbnail=thumbnail,
            disable_notification=disable_notification,
            protect_content=protect_content
            if protect_content is not None
            else self.protect_content,
            message_effect_id=message_effect_id,
            reply_parameters=reply_parameters,
            reply_markup=reply_markup,
        )
        return Message._parse(me=self, d=result["result"])

    async def send_paid_media(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        star_count: int,
        media: List[InputPaidMedia],
        caption: str = None,
        parse_mode: str = None,
        caption_entities: List[MessageEntity] = None,
        show_caption_above_media: bool = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        reply_parameters: ReplyParameters = None,
        reply_markup: Union[
            InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply
        ] = None,
    ) -> Message:
        """https://core.telegram.org/bots/api#sendpaidmedia"""
        result = await self._send_request(
            "sendPaidMedia",
            chat_id=chat_id,
            star_count=star_count,
            media=media,
            caption=caption,
            parse_mode=parse_mode or self.parse_mode,
            caption_entities=caption_entities,
            show_caption_above_media=show_caption_above_media,
            disable_notification=disable_notification,
            protect_content=protect_content
            if protect_content is not None
            else self.protect_content,
            reply_parameters=reply_parameters,
            reply_markup=reply_markup,
        )
        return Message._parse(me=self, d=result["result"])

    async def send_media_group(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        media: List[InputMedia],
        business_connection_id: str = None,
        message_thread_id: int = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        message_effect_id: str = None,
        reply_parameters: ReplyParameters = None,
    ) -> List[Message]:
        """https://core.telegram.org/bots/api/#sendmediagroup"""
        result = await self._send_request(
            "sendMediaGroup",
            chat_id=chat_id,
            media=media,
            business_connection_id=business_connection_id,
            message_thread_id=message_thread_id,
            disable_notification=disable_notification,
            protect_content=protect_content
            if protect_content is not None
            else self.protect_content,
            message_effect_id=message_effect_id,
            reply_parameters=reply_parameters,
        )
        return [Message._parse(me=self, d=i) for i in result["result"]]

    async def send_location(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        latitude: float,
        longitude: float,
        business_connection_id: str = None,
        message_thread_id: int = None,
        horizontal_accuracy: float = None,
        live_period: int = None,
        heading: int = None,
        proximity_alert_radius: int = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        message_effect_id: str = None,
        reply_parameters: ReplyParameters = None,
        reply_markup: Union[
            InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply
        ] = None,
    ) -> Message:
        """https://core.telegram.org/bots/api/#sendlocation"""
        result = await self._send_request(
            "sendLocation",
            chat_id=chat_id,
            latitude=latitude,
            longitude=longitude,
            business_connection_id=business_connection_id,
            message_thread_id=message_thread_id,
            horizontal_accuracy=horizontal_accuracy,
            live_period=live_period,
            heading=heading,
            proximity_alert_radius=proximity_alert_radius,
            disable_notification=disable_notification,
            protect_content=protect_content
            if protect_content is not None
            else self.protect_content,
            message_effect_id=message_effect_id,
            reply_parameters=reply_parameters,
            reply_markup=reply_markup,
        )
        return Message._parse(me=self, d=result["result"])

    async def send_venue(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        latitude: float,
        longitude: float,
        title: str,
        address: str,
        business_connection_id: str = None,
        message_thread_id: int = None,
        foursquare_id: str = None,
        foursquare_type: str = None,
        google_place_id: str = None,
        google_place_type: str = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        message_effect_id: str = None,
        reply_parameters: ReplyParameters = None,
        reply_markup: Union[
            InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply
        ] = None,
    ) -> Message:
        """https://core.telegram.org/bots/api/#sendvenue"""
        result = await self._send_request(
            "sendVenue",
            chat_id=chat_id,
            latitude=latitude,
            longitude=longitude,
            title=title,
            address=address,
            business_connection_id=business_connection_id,
            message_thread_id=message_thread_id,
            foursquare_id=foursquare_id,
            foursquare_type=foursquare_type,
            google_place_id=google_place_id,
            google_place_type=google_place_type,
            disable_notification=disable_notification,
            protect_content=protect_content
            if protect_content is not None
            else self.protect_content,
            message_effect_id=message_effect_id,
            reply_parameters=reply_parameters,
            reply_markup=reply_markup,
        )
        return Message._parse(me=self, d=result["result"])

    async def send_contact(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        phone_number: str,
        first_name: str,
        business_connection_id: str = None,
        message_thread_id: int = None,
        last_name: str = None,
        vcard: str = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        message_effect_id: str = None,
        reply_parameters: ReplyParameters = None,
        reply_markup: Union[
            InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply
        ] = None,
    ) -> Message:
        """https://core.telegram.org/bots/api/#sendcontact"""
        result = await self._send_request(
            "sendContact",
            chat_id=chat_id,
            phone_number=phone_number,
            first_name=first_name,
            business_connection_id=business_connection_id,
            message_thread_id=message_thread_id,
            last_name=last_name,
            vcard=vcard,
            disable_notification=disable_notification,
            protect_content=protect_content
            if protect_content is not None
            else self.protect_content,
            message_effect_id=message_effect_id,
            reply_parameters=reply_parameters,
            reply_markup=reply_markup,
        )
        return Message._parse(me=self, d=result["result"])

    async def send_poll(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        question: str,
        options: List[InputPollOption],
        business_connection_id: str = None,
        message_thread_id: int = None,
        question_parse_mode: str = None,
        question_entities: List[MessageEntity] = None,
        is_anonymous: bool = None,
        type: str = None,
        allows_multiple_answers: bool = None,
        correct_option_id: int = None,
        explanation: str = None,
        explanation_parse_mode: str = None,
        explanation_entities: List[MessageEntity] = None,
        open_period: int = None,
        close_date: int = None,
        is_closed: bool = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        message_effect_id: str = None,
        reply_parameters: ReplyParameters = None,
        reply_markup: Union[
            InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply
        ] = None,
    ) -> Message:
        """https://core.telegram.org/bots/api/#sendpoll"""
        result = await self._send_request(
            "sendPoll",
            chat_id=chat_id,
            question=question,
            options=options,
            business_connection_id=business_connection_id,
            message_thread_id=message_thread_id,
            question_parse_mode=question_parse_mode,
            question_entities=question_entities,
            is_anonymous=is_anonymous,
            type=type,
            allows_multiple_answers=allows_multiple_answers,
            correct_option_id=correct_option_id,
            explanation=explanation,
            explanation_parse_mode=explanation_parse_mode,
            explanation_entities=explanation_entities,
            open_period=open_period,
            close_date=close_date,
            is_closed=is_closed,
            disable_notification=disable_notification,
            protect_content=protect_content
            if protect_content is not None
            else self.protect_content,
            message_effect_id=message_effect_id,
            reply_parameters=reply_parameters,
            reply_markup=reply_markup,
        )
        return Message._parse(me=self, d=result["result"])

    async def send_dice(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        business_connection_id: str = None,
        message_thread_id: int = None,
        emoji: str = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        message_effect_id: str = None,
        reply_parameters: ReplyParameters = None,
        reply_markup: Union[
            InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply
        ] = None,
    ) -> Message:
        """https://core.telegram.org/bots/api/#senddice"""
        result = await self._send_request(
            "sendDice",
            chat_id=chat_id,
            business_connection_id=business_connection_id,
            message_thread_id=message_thread_id,
            emoji=emoji,
            disable_notification=disable_notification,
            protect_content=protect_content
            if protect_content is not None
            else self.protect_content,
            message_effect_id=message_effect_id,
            reply_parameters=reply_parameters,
            reply_markup=reply_markup,
        )
        return Message._parse(me=self, d=result["result"])

    async def send_chat_action(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        action: str,
        business_connection_id: str = None,
        message_thread_id: int = None,
    ) -> bool:
        """https://core.telegram.org/bots/api/#sendchataction"""
        result = await self._send_request(
            "sendChatAction",
            chat_id=chat_id,
            action=action,
            business_connection_id=business_connection_id,
            message_thread_id=message_thread_id,
        )
        return result["result"]

    async def set_message_reaction(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        message_id: int,
        reaction: List[ReactionType] = None,
        is_big: bool = None,
    ) -> bool:
        """https://core.telegram.org/bots/api/#setmessagereaction"""
        result = await self._send_request(
            "setMessageReaction",
            chat_id=chat_id,
            message_id=message_id,
            reaction=reaction,
            is_big=is_big,
        )
        return result["result"]

    async def get_user_profile_photos(
        self: "tgram.TgBot", user_id: int, offset: int = None, limit: int = None
    ) -> UserProfilePhotos:
        """https://core.telegram.org/bots/api/#getuserprofilephotos"""
        result = await self._send_request(
            "getUserProfilePhotos",
            user_id=user_id,
            offset=offset,
            limit=limit,
        )
        return UserProfilePhotos._parse(me=self, d=result["result"])

    async def get_file(self: "tgram.TgBot", file_id: str) -> File:
        """https://core.telegram.org/bots/api/#getfile"""
        result = await self._send_request(
            "getFile",
            file_id=file_id,
        )
        return File._parse(me=self, d=result["result"])

    async def ban_chat_member(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        user_id: int,
        until_date: int = None,
        revoke_messages: bool = None,
    ) -> bool:
        """https://core.telegram.org/bots/api/#banchatmember"""
        result = await self._send_request(
            "banChatMember",
            chat_id=chat_id,
            user_id=user_id,
            until_date=until_date,
            revoke_messages=revoke_messages,
        )
        return result["result"]

    async def unban_chat_member(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        user_id: int,
        only_if_banned: bool = None,
    ) -> bool:
        """https://core.telegram.org/bots/api/#unbanchatmember"""
        result = await self._send_request(
            "unbanChatMember",
            chat_id=chat_id,
            user_id=user_id,
            only_if_banned=only_if_banned,
        )
        return result["result"]

    async def restrict_chat_member(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        user_id: int,
        permissions: ChatPermissions,
        use_independent_chat_permissions: bool = None,
        until_date: int = None,
    ) -> bool:
        """https://core.telegram.org/bots/api/#restrictchatmember"""
        result = await self._send_request(
            "restrictChatMember",
            chat_id=chat_id,
            user_id=user_id,
            permissions=permissions,
            use_independent_chat_permissions=use_independent_chat_permissions,
            until_date=until_date,
        )
        return result["result"]

    async def promote_chat_member(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        user_id: int,
        is_anonymous: bool = None,
        can_manage_chat: bool = None,
        can_delete_messages: bool = None,
        can_manage_video_chats: bool = None,
        can_restrict_members: bool = None,
        can_promote_members: bool = None,
        can_change_info: bool = None,
        can_invite_users: bool = None,
        can_post_stories: bool = None,
        can_edit_stories: bool = None,
        can_delete_stories: bool = None,
        can_post_messages: bool = None,
        can_edit_messages: bool = None,
        can_pin_messages: bool = None,
        can_manage_topics: bool = None,
    ) -> bool:
        """https://core.telegram.org/bots/api/#promotechatmember"""
        result = await self._send_request(
            "promoteChatMember",
            chat_id=chat_id,
            user_id=user_id,
            is_anonymous=is_anonymous,
            can_manage_chat=can_manage_chat,
            can_delete_messages=can_delete_messages,
            can_manage_video_chats=can_manage_video_chats,
            can_restrict_members=can_restrict_members,
            can_promote_members=can_promote_members,
            can_change_info=can_change_info,
            can_invite_users=can_invite_users,
            can_post_stories=can_post_stories,
            can_edit_stories=can_edit_stories,
            can_delete_stories=can_delete_stories,
            can_post_messages=can_post_messages,
            can_edit_messages=can_edit_messages,
            can_pin_messages=can_pin_messages,
            can_manage_topics=can_manage_topics,
        )
        return result["result"]

    async def set_chat_administrator_custom_title(
        self: "tgram.TgBot", chat_id: Union[int, str], user_id: int, custom_title: str
    ) -> bool:
        """https://core.telegram.org/bots/api/#setchatadministratorcustomtitle"""
        result = await self._send_request(
            "setChatAdministratorCustomTitle",
            chat_id=chat_id,
            user_id=user_id,
            custom_title=custom_title,
        )
        return result["result"]

    async def ban_chat_sender_chat(
        self: "tgram.TgBot", chat_id: Union[int, str], sender_chat_id: int
    ) -> bool:
        """https://core.telegram.org/bots/api/#banchatsenderchat"""
        result = await self._send_request(
            "banChatSenderChat",
            chat_id=chat_id,
            sender_chat_id=sender_chat_id,
        )
        return result["result"]

    async def unban_chat_sender_chat(
        self: "tgram.TgBot", chat_id: Union[int, str], sender_chat_id: int
    ) -> bool:
        """https://core.telegram.org/bots/api/#unbanchatsenderchat"""
        result = await self._send_request(
            "unbanChatSenderChat",
            chat_id=chat_id,
            sender_chat_id=sender_chat_id,
        )
        return result["result"]

    async def set_chat_permissions(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        permissions: ChatPermissions,
        use_independent_chat_permissions: bool = None,
    ) -> bool:
        """https://core.telegram.org/bots/api/#setchatpermissions"""
        result = await self._send_request(
            "setChatPermissions",
            chat_id=chat_id,
            permissions=permissions,
            use_independent_chat_permissions=use_independent_chat_permissions,
        )
        return result["result"]

    async def export_chat_invite_link(
        self: "tgram.TgBot", chat_id: Union[int, str]
    ) -> str:
        """https://core.telegram.org/bots/api/#exportchatinvitelink"""
        result = await self._send_request(
            "exportChatInviteLink",
            chat_id=chat_id,
        )
        return result["result"]

    async def create_chat_invite_link(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        name: str = None,
        expire_date: int = None,
        member_limit: int = None,
        creates_join_request: bool = None,
    ) -> ChatInviteLink:
        """https://core.telegram.org/bots/api/#createchatinvitelink"""
        result = await self._send_request(
            "createChatInviteLink",
            chat_id=chat_id,
            name=name,
            expire_date=expire_date,
            member_limit=member_limit,
            creates_join_request=creates_join_request,
        )
        return ChatInviteLink._parse(me=self, d=result["result"])

    async def edit_chat_invite_link(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        invite_link: str,
        name: str = None,
        expire_date: int = None,
        member_limit: int = None,
        creates_join_request: bool = None,
    ) -> ChatInviteLink:
        """https://core.telegram.org/bots/api/#editchatinvitelink"""
        result = await self._send_request(
            "editChatInviteLink",
            chat_id=chat_id,
            invite_link=invite_link,
            name=name,
            expire_date=expire_date,
            member_limit=member_limit,
            creates_join_request=creates_join_request,
        )
        return ChatInviteLink._parse(me=self, d=result["result"])

    async def revoke_chat_invite_link(
        self: "tgram.TgBot", chat_id: Union[int, str], invite_link: str
    ) -> ChatInviteLink:
        """https://core.telegram.org/bots/api/#revokechatinvitelink"""
        result = await self._send_request(
            "revokeChatInviteLink",
            chat_id=chat_id,
            invite_link=invite_link,
        )
        return ChatInviteLink._parse(me=self, d=result["result"])

    async def approve_chat_join_request(
        self: "tgram.TgBot", chat_id: Union[int, str], user_id: int
    ) -> bool:
        """https://core.telegram.org/bots/api/#approvechatjoinrequest"""
        result = await self._send_request(
            "approveChatJoinRequest",
            chat_id=chat_id,
            user_id=user_id,
        )
        return result["result"]

    async def decline_chat_join_request(
        self: "tgram.TgBot", chat_id: Union[int, str], user_id: int
    ) -> bool:
        """https://core.telegram.org/bots/api/#declinechatjoinrequest"""
        result = await self._send_request(
            "declineChatJoinRequest",
            chat_id=chat_id,
            user_id=user_id,
        )
        return result["result"]

    async def set_chat_photo(
        self: "tgram.TgBot", chat_id: Union[int, str], photo: InputFile
    ) -> bool:
        """https://core.telegram.org/bots/api/#setchatphoto"""
        result = await self._send_request(
            "setChatPhoto",
            chat_id=chat_id,
            photo=photo,
        )
        return result["result"]

    async def delete_chat_photo(self: "tgram.TgBot", chat_id: Union[int, str]) -> bool:
        """https://core.telegram.org/bots/api/#deletechatphoto"""
        result = await self._send_request(
            "deleteChatPhoto",
            chat_id=chat_id,
        )
        return result["result"]

    async def set_chat_title(
        self: "tgram.TgBot", chat_id: Union[int, str], title: str
    ) -> bool:
        """https://core.telegram.org/bots/api/#setchattitle"""
        result = await self._send_request(
            "setChatTitle",
            chat_id=chat_id,
            title=title,
        )
        return result["result"]

    async def set_chat_description(
        self: "tgram.TgBot", chat_id: Union[int, str], description: str = None
    ) -> bool:
        """https://core.telegram.org/bots/api/#setchatdescription"""
        result = await self._send_request(
            "setChatDescription",
            chat_id=chat_id,
            description=description,
        )
        return result["result"]

    async def pin_chat_message(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        message_id: int,
        disable_notification: bool = None,
    ) -> bool:
        """https://core.telegram.org/bots/api/#pinchatmessage"""
        result = await self._send_request(
            "pinChatMessage",
            chat_id=chat_id,
            message_id=message_id,
            disable_notification=disable_notification,
        )
        return result["result"]

    async def unpin_chat_message(
        self: "tgram.TgBot", chat_id: Union[int, str], message_id: int = None
    ) -> bool:
        """https://core.telegram.org/bots/api/#unpinchatmessage"""
        result = await self._send_request(
            "unpinChatMessage",
            chat_id=chat_id,
            message_id=message_id,
        )
        return result["result"]

    async def unpin_all_chat_messages(
        self: "tgram.TgBot", chat_id: Union[int, str]
    ) -> bool:
        """https://core.telegram.org/bots/api/#unpinallchatmessages"""
        result = await self._send_request(
            "unpinAllChatMessages",
            chat_id=chat_id,
        )
        return result["result"]

    async def leave_chat(self: "tgram.TgBot", chat_id: Union[int, str]) -> bool:
        """https://core.telegram.org/bots/api/#leavechat"""
        result = await self._send_request(
            "leaveChat",
            chat_id=chat_id,
        )
        return result["result"]

    async def get_chat(self: "tgram.TgBot", chat_id: Union[int, str]) -> ChatFullInfo:
        """https://core.telegram.org/bots/api/#getchat"""
        result = await self._send_request(
            "getChat",
            chat_id=chat_id,
        )
        return ChatFullInfo._parse(me=self, d=result["result"])

    async def get_chat_administrators(
        self: "tgram.TgBot", chat_id: Union[int, str]
    ) -> List[ChatMember]:
        """https://core.telegram.org/bots/api/#getchatadministrators"""
        result = await self._send_request(
            "getChatAdministrators",
            chat_id=chat_id,
        )
        return [ChatMember._parse(me=self, d=i) for i in result["result"]]

    async def get_chat_member_count(
        self: "tgram.TgBot", chat_id: Union[int, str]
    ) -> int:
        """https://core.telegram.org/bots/api/#getchatmembercount"""
        result = await self._send_request(
            "getChatMemberCount",
            chat_id=chat_id,
        )
        return result["result"]

    async def get_chat_member(
        self: "tgram.TgBot", chat_id: Union[int, str], user_id: int
    ) -> ChatMember:
        """https://core.telegram.org/bots/api/#getchatmember"""
        result = await self._send_request(
            "getChatMember",
            chat_id=chat_id,
            user_id=user_id,
        )
        return ChatMember._parse(me=self, d=result["result"])

    async def set_chat_sticker_set(
        self: "tgram.TgBot", chat_id: Union[int, str], sticker_set_name: str
    ) -> bool:
        """https://core.telegram.org/bots/api/#setchatstickerset"""
        result = await self._send_request(
            "setChatStickerSet",
            chat_id=chat_id,
            sticker_set_name=sticker_set_name,
        )
        return result["result"]

    async def delete_chat_sticker_set(
        self: "tgram.TgBot", chat_id: Union[int, str]
    ) -> bool:
        """https://core.telegram.org/bots/api/#deletechatstickerset"""
        result = await self._send_request(
            "deleteChatStickerSet",
            chat_id=chat_id,
        )
        return result["result"]

    async def get_forum_topic_icon_stickers(self: "tgram.TgBot") -> List[Sticker]:
        """https://core.telegram.org/bots/api/#getforumtopiciconstickers"""
        result = await self._send_request(
            "getForumTopicIconStickers",
        )
        return [Sticker._parse(me=self, d=i) for i in result["result"]]

    async def create_forum_topic(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        name: str,
        icon_color: int = None,
        icon_custom_emoji_id: str = None,
    ) -> ForumTopic:
        """https://core.telegram.org/bots/api/#createforumtopic"""
        result = await self._send_request(
            "createForumTopic",
            chat_id=chat_id,
            name=name,
            icon_color=icon_color,
            icon_custom_emoji_id=icon_custom_emoji_id,
        )
        return ForumTopic._parse(me=self, d=result["result"])

    async def edit_forum_topic(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        message_thread_id: int,
        name: str = None,
        icon_custom_emoji_id: str = None,
    ) -> bool:
        """https://core.telegram.org/bots/api/#editforumtopic"""
        result = await self._send_request(
            "editForumTopic",
            chat_id=chat_id,
            message_thread_id=message_thread_id,
            name=name,
            icon_custom_emoji_id=icon_custom_emoji_id,
        )
        return result["result"]

    async def close_forum_topic(
        self: "tgram.TgBot", chat_id: Union[int, str], message_thread_id: int
    ) -> bool:
        """https://core.telegram.org/bots/api/#closeforumtopic"""
        result = await self._send_request(
            "closeForumTopic",
            chat_id=chat_id,
            message_thread_id=message_thread_id,
        )
        return result["result"]

    async def reopen_forum_topic(
        self: "tgram.TgBot", chat_id: Union[int, str], message_thread_id: int
    ) -> bool:
        """https://core.telegram.org/bots/api/#reopenforumtopic"""
        result = await self._send_request(
            "reopenForumTopic",
            chat_id=chat_id,
            message_thread_id=message_thread_id,
        )
        return result["result"]

    async def delete_forum_topic(
        self: "tgram.TgBot", chat_id: Union[int, str], message_thread_id: int
    ) -> bool:
        """https://core.telegram.org/bots/api/#deleteforumtopic"""
        result = await self._send_request(
            "deleteForumTopic",
            chat_id=chat_id,
            message_thread_id=message_thread_id,
        )
        return result["result"]

    async def unpin_all_forum_topic_messages(
        self: "tgram.TgBot", chat_id: Union[int, str], message_thread_id: int
    ) -> bool:
        """https://core.telegram.org/bots/api/#unpinallforumtopicmessages"""
        result = await self._send_request(
            "unpinAllForumTopicMessages",
            chat_id=chat_id,
            message_thread_id=message_thread_id,
        )
        return result["result"]

    async def edit_general_forum_topic(
        self: "tgram.TgBot", chat_id: Union[int, str], name: str
    ) -> bool:
        """https://core.telegram.org/bots/api/#editgeneralforumtopic"""
        result = await self._send_request(
            "editGeneralForumTopic",
            chat_id=chat_id,
            name=name,
        )
        return result["result"]

    async def close_general_forum_topic(
        self: "tgram.TgBot", chat_id: Union[int, str]
    ) -> bool:
        """https://core.telegram.org/bots/api/#closegeneralforumtopic"""
        result = await self._send_request(
            "closeGeneralForumTopic",
            chat_id=chat_id,
        )
        return result["result"]

    async def reopen_general_forum_topic(
        self: "tgram.TgBot", chat_id: Union[int, str]
    ) -> bool:
        """https://core.telegram.org/bots/api/#reopengeneralforumtopic"""
        result = await self._send_request(
            "reopenGeneralForumTopic",
            chat_id=chat_id,
        )
        return result["result"]

    async def hide_general_forum_topic(
        self: "tgram.TgBot", chat_id: Union[int, str]
    ) -> bool:
        """https://core.telegram.org/bots/api/#hidegeneralforumtopic"""
        result = await self._send_request(
            "hideGeneralForumTopic",
            chat_id=chat_id,
        )
        return result["result"]

    async def unhide_general_forum_topic(
        self: "tgram.TgBot", chat_id: Union[int, str]
    ) -> bool:
        """https://core.telegram.org/bots/api/#unhidegeneralforumtopic"""
        result = await self._send_request(
            "unhideGeneralForumTopic",
            chat_id=chat_id,
        )
        return result["result"]

    async def unpin_all_general_forum_topic_messages(
        self: "tgram.TgBot", chat_id: Union[int, str]
    ) -> bool:
        """https://core.telegram.org/bots/api/#unpinallgeneralforumtopicmessages"""
        result = await self._send_request(
            "unpinAllGeneralForumTopicMessages",
            chat_id=chat_id,
        )
        return result["result"]

    async def answer_callback_query(
        self: "tgram.TgBot",
        callback_query_id: str,
        text: str = None,
        show_alert: bool = None,
        url: str = None,
        cache_time: int = None,
    ) -> bool:
        """https://core.telegram.org/bots/api/#answercallbackquery"""
        result = await self._send_request(
            "answerCallbackQuery",
            callback_query_id=callback_query_id,
            text=text,
            show_alert=show_alert,
            url=url,
            cache_time=cache_time,
        )
        return result["result"]

    async def get_user_chat_boosts(
        self: "tgram.TgBot", chat_id: Union[int, str], user_id: int
    ) -> UserChatBoosts:
        """https://core.telegram.org/bots/api/#getuserchatboosts"""
        result = await self._send_request(
            "getUserChatBoosts",
            chat_id=chat_id,
            user_id=user_id,
        )
        return UserChatBoosts._parse(me=self, d=result["result"])

    async def get_business_connection(
        self: "tgram.TgBot", business_connection_id: str
    ) -> BusinessConnection:
        """https://core.telegram.org/bots/api/#getbusinessconnection"""
        result = await self._send_request(
            "getBusinessConnection",
            business_connection_id=business_connection_id,
        )
        return BusinessConnection._parse(me=self, d=result["result"])

    async def set_my_commands(
        self: "tgram.TgBot",
        commands: List[BotCommand],
        scope: BotCommandScope = None,
        language_code: str = None,
    ) -> bool:
        """https://core.telegram.org/bots/api/#setmycommands"""
        result = await self._send_request(
            "setMyCommands",
            commands=commands,
            scope=scope,
            language_code=language_code,
        )
        return result["result"]

    async def delete_my_commands(
        self: "tgram.TgBot", scope: BotCommandScope = None, language_code: str = None
    ) -> bool:
        """https://core.telegram.org/bots/api/#deletemycommands"""
        result = await self._send_request(
            "deleteMyCommands",
            scope=scope,
            language_code=language_code,
        )
        return result["result"]

    async def get_my_commands(
        self: "tgram.TgBot", scope: BotCommandScope = None, language_code: str = None
    ) -> List[BotCommand]:
        """https://core.telegram.org/bots/api/#getmycommands"""
        result = await self._send_request(
            "getMyCommands",
            scope=scope,
            language_code=language_code,
        )
        return [BotCommand._parse(me=self, d=i) for i in result["result"]]

    async def set_my_name(
        self: "tgram.TgBot", name: str = None, language_code: str = None
    ) -> bool:
        """https://core.telegram.org/bots/api/#setmyname"""
        result = await self._send_request(
            "setMyName",
            name=name,
            language_code=language_code,
        )
        return result["result"]

    async def get_my_name(self: "tgram.TgBot", language_code: str = None) -> BotName:
        """https://core.telegram.org/bots/api/#getmyname"""
        result = await self._send_request(
            "getMyName",
            language_code=language_code,
        )
        return BotName._parse(me=self, d=result["result"])

    async def set_my_description(
        self: "tgram.TgBot", description: str = None, language_code: str = None
    ) -> bool:
        """https://core.telegram.org/bots/api/#setmydescription"""
        result = await self._send_request(
            "setMyDescription",
            description=description,
            language_code=language_code,
        )
        return result["result"]

    async def get_my_description(
        self: "tgram.TgBot", language_code: str = None
    ) -> BotDescription:
        """https://core.telegram.org/bots/api/#getmydescription"""
        result = await self._send_request(
            "getMyDescription",
            language_code=language_code,
        )
        return BotDescription._parse(me=self, d=result["result"])

    async def set_my_short_description(
        self: "tgram.TgBot", short_description: str = None, language_code: str = None
    ) -> bool:
        """https://core.telegram.org/bots/api/#setmyshortdescription"""
        result = await self._send_request(
            "setMyShortDescription",
            short_description=short_description,
            language_code=language_code,
        )
        return result["result"]

    async def get_my_short_description(
        self: "tgram.TgBot", language_code: str = None
    ) -> BotShortDescription:
        """https://core.telegram.org/bots/api/#getmyshortdescription"""
        result = await self._send_request(
            "getMyShortDescription",
            language_code=language_code,
        )
        return BotShortDescription._parse(me=self, d=result["result"])

    async def set_chat_menu_button(
        self: "tgram.TgBot", chat_id: int = None, menu_button: MenuButton = None
    ) -> bool:
        """https://core.telegram.org/bots/api/#setchatmenubutton"""
        result = await self._send_request(
            "setChatMenuButton",
            chat_id=chat_id,
            menu_button=menu_button,
        )
        return result["result"]

    async def get_chat_menu_button(
        self: "tgram.TgBot", chat_id: int = None
    ) -> MenuButton:
        """https://core.telegram.org/bots/api/#getchatmenubutton"""
        result = await self._send_request(
            "getChatMenuButton",
            chat_id=chat_id,
        )
        return MenuButton._parse(me=self, d=result["result"])

    async def set_my_default_administrator_rights(
        self: "tgram.TgBot",
        rights: ChatAdministratorRights = None,
        for_channels: bool = None,
    ) -> bool:
        """https://core.telegram.org/bots/api/#setmydefaultadministratorrights"""
        result = await self._send_request(
            "setMyDefaultAdministratorRights",
            rights=rights,
            for_channels=for_channels,
        )
        return result["result"]

    async def get_my_default_administrator_rights(
        self: "tgram.TgBot", for_channels: bool = None
    ) -> ChatAdministratorRights:
        """https://core.telegram.org/bots/api/#getmydefaultadministratorrights"""
        result = await self._send_request(
            "getMyDefaultAdministratorRights",
            for_channels=for_channels,
        )
        return ChatAdministratorRights._parse(me=self, d=result["result"])

    async def edit_message_text(
        self: "tgram.TgBot",
        text: str,
        business_connection_id: str = None,
        chat_id: Union[int, str] = None,
        message_id: int = None,
        inline_message_id: str = None,
        parse_mode: str = None,
        entities: List[MessageEntity] = None,
        link_preview_options: LinkPreviewOptions = None,
        reply_markup: InlineKeyboardMarkup = None,
    ) -> Union[Message, bool]:
        """https://core.telegram.org/bots/api/#editmessagetext"""
        result = await self._send_request(
            "editMessageText",
            text=text,
            business_connection_id=business_connection_id,
            chat_id=chat_id,
            message_id=message_id,
            inline_message_id=inline_message_id,
            parse_mode=parse_mode or self.parse_mode,
            entities=entities,
            link_preview_options=link_preview_options or self.link_preview_options,
            reply_markup=reply_markup,
        )
        return (
            Message._parse(me=self, d=result["result"])
            if isinstance(result["result"], dict)
            else result["result"]
        )

    async def edit_message_caption(
        self: "tgram.TgBot",
        business_connection_id: str = None,
        chat_id: Union[int, str] = None,
        message_id: int = None,
        inline_message_id: str = None,
        caption: str = None,
        parse_mode: str = None,
        caption_entities: List[MessageEntity] = None,
        show_caption_above_media: bool = None,
        reply_markup: InlineKeyboardMarkup = None,
    ) -> Union[Message, bool]:
        """https://core.telegram.org/bots/api/#editmessagecaption"""
        result = await self._send_request(
            "editMessageCaption",
            business_connection_id=business_connection_id,
            chat_id=chat_id,
            message_id=message_id,
            inline_message_id=inline_message_id,
            caption=caption,
            parse_mode=parse_mode or self.parse_mode,
            caption_entities=caption_entities,
            show_caption_above_media=show_caption_above_media,
            reply_markup=reply_markup,
        )
        return (
            Message._parse(me=self, d=result["result"])
            if isinstance(result["result"], dict)
            else result["result"]
        )

    async def edit_message_media(
        self: "tgram.TgBot",
        media: InputMedia,
        business_connection_id: str = None,
        chat_id: Union[int, str] = None,
        message_id: int = None,
        inline_message_id: str = None,
        reply_markup: InlineKeyboardMarkup = None,
    ) -> Union[Message, bool]:
        """https://core.telegram.org/bots/api/#editmessagemedia"""
        result = await self._send_request(
            "editMessageMedia",
            media=media,
            business_connection_id=business_connection_id,
            chat_id=chat_id,
            message_id=message_id,
            inline_message_id=inline_message_id,
            reply_markup=reply_markup,
        )
        return (
            Message._parse(me=self, d=result["result"])
            if isinstance(result["result"], dict)
            else result["result"]
        )

    async def edit_message_live_location(
        self: "tgram.TgBot",
        latitude: float,
        longitude: float,
        business_connection_id: str = None,
        chat_id: Union[int, str] = None,
        message_id: int = None,
        inline_message_id: str = None,
        live_period: int = None,
        horizontal_accuracy: float = None,
        heading: int = None,
        proximity_alert_radius: int = None,
        reply_markup: InlineKeyboardMarkup = None,
    ) -> Union[Message, bool]:
        """https://core.telegram.org/bots/api/#editmessagelivelocation"""
        result = await self._send_request(
            "editMessageLiveLocation",
            latitude=latitude,
            longitude=longitude,
            business_connection_id=business_connection_id,
            chat_id=chat_id,
            message_id=message_id,
            inline_message_id=inline_message_id,
            live_period=live_period,
            horizontal_accuracy=horizontal_accuracy,
            heading=heading,
            proximity_alert_radius=proximity_alert_radius,
            reply_markup=reply_markup,
        )
        return (
            Message._parse(me=self, d=result["result"])
            if isinstance(result["result"], dict)
            else result["result"]
        )

    async def stop_message_live_location(
        self: "tgram.TgBot",
        business_connection_id: str = None,
        chat_id: Union[int, str] = None,
        message_id: int = None,
        inline_message_id: str = None,
        reply_markup: InlineKeyboardMarkup = None,
    ) -> Union[Message, bool]:
        """https://core.telegram.org/bots/api/#stopmessagelivelocation"""
        result = await self._send_request(
            "stopMessageLiveLocation",
            business_connection_id=business_connection_id,
            chat_id=chat_id,
            message_id=message_id,
            inline_message_id=inline_message_id,
            reply_markup=reply_markup,
        )
        return (
            Message._parse(me=self, d=result["result"])
            if isinstance(result["result"], dict)
            else result["result"]
        )

    async def edit_message_reply_markup(
        self: "tgram.TgBot",
        business_connection_id: str = None,
        chat_id: Union[int, str] = None,
        message_id: int = None,
        inline_message_id: str = None,
        reply_markup: InlineKeyboardMarkup = None,
    ) -> Union[Message, bool]:
        """https://core.telegram.org/bots/api/#editmessagereplymarkup"""
        result = await self._send_request(
            "editMessageReplyMarkup",
            business_connection_id=business_connection_id,
            chat_id=chat_id,
            message_id=message_id,
            inline_message_id=inline_message_id,
            reply_markup=reply_markup,
        )
        return (
            Message._parse(me=self, d=result["result"])
            if isinstance(result["result"], dict)
            else result["result"]
        )

    async def stop_poll(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        message_id: int,
        business_connection_id: str = None,
        reply_markup: InlineKeyboardMarkup = None,
    ) -> Poll:
        """https://core.telegram.org/bots/api/#stoppoll"""
        result = await self._send_request(
            "stopPoll",
            chat_id=chat_id,
            message_id=message_id,
            business_connection_id=business_connection_id,
            reply_markup=reply_markup,
        )
        return Poll._parse(me=self, d=result["result"])

    async def delete_message(
        self: "tgram.TgBot", chat_id: Union[int, str], message_id: int
    ) -> bool:
        """https://core.telegram.org/bots/api/#deletemessage"""
        result = await self._send_request(
            "deleteMessage",
            chat_id=chat_id,
            message_id=message_id,
        )
        return result["result"]

    async def delete_messages(
        self: "tgram.TgBot", chat_id: Union[int, str], message_ids: List[int]
    ) -> bool:
        """https://core.telegram.org/bots/api/#deletemessages"""
        result = await self._send_request(
            "deleteMessages",
            chat_id=chat_id,
            message_ids=message_ids,
        )
        return result["result"]

    async def send_sticker(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        sticker: Union[InputFile, str],
        business_connection_id: str = None,
        message_thread_id: int = None,
        emoji: str = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        message_effect_id: str = None,
        reply_parameters: ReplyParameters = None,
        reply_markup: Union[
            InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply
        ] = None,
    ) -> Message:
        """https://core.telegram.org/bots/api/#sendsticker"""
        result = await self._send_request(
            "sendSticker",
            chat_id=chat_id,
            sticker=sticker,
            business_connection_id=business_connection_id,
            message_thread_id=message_thread_id,
            emoji=emoji,
            disable_notification=disable_notification,
            protect_content=protect_content
            if protect_content is not None
            else self.protect_content,
            message_effect_id=message_effect_id,
            reply_parameters=reply_parameters,
            reply_markup=reply_markup,
        )
        return Message._parse(me=self, d=result["result"])

    async def get_sticker_set(self: "tgram.TgBot", name: str) -> StickerSet:
        """https://core.telegram.org/bots/api/#getstickerset"""
        result = await self._send_request(
            "getStickerSet",
            name=name,
        )
        return StickerSet._parse(me=self, d=result["result"])

    async def get_custom_emoji_stickers(
        self: "tgram.TgBot", custom_emoji_ids: List[str]
    ) -> List[Sticker]:
        """https://core.telegram.org/bots/api/#getcustomemojistickers"""
        result = await self._send_request(
            "getCustomEmojiStickers",
            custom_emoji_ids=custom_emoji_ids,
        )
        return [Sticker._parse(me=self, d=i) for i in result["result"]]

    async def upload_sticker_file(
        self: "tgram.TgBot", user_id: int, sticker: InputFile, sticker_format: str
    ) -> File:
        """https://core.telegram.org/bots/api/#uploadstickerfile"""
        result = await self._send_request(
            "uploadStickerFile",
            user_id=user_id,
            sticker=sticker,
            sticker_format=sticker_format,
        )
        return File._parse(me=self, d=result["result"])

    async def create_new_sticker_set(
        self: "tgram.TgBot",
        user_id: int,
        name: str,
        title: str,
        stickers: List[InputSticker],
        sticker_type: str = None,
        needs_repainting: bool = None,
    ) -> bool:
        """https://core.telegram.org/bots/api/#createnewstickerset"""
        result = await self._send_request(
            "createNewStickerSet",
            user_id=user_id,
            name=name,
            title=title,
            stickers=stickers,
            sticker_type=sticker_type,
            needs_repainting=needs_repainting,
        )
        return result["result"]

    async def add_sticker_to_set(
        self: "tgram.TgBot", user_id: int, name: str, sticker: InputSticker
    ) -> bool:
        """https://core.telegram.org/bots/api/#addstickertoset"""
        result = await self._send_request(
            "addStickerToSet",
            user_id=user_id,
            name=name,
            sticker=sticker,
        )
        return result["result"]

    async def set_sticker_position_in_set(
        self: "tgram.TgBot", sticker: str, position: int
    ) -> bool:
        """https://core.telegram.org/bots/api/#setstickerpositioninset"""
        result = await self._send_request(
            "setStickerPositionInSet",
            sticker=sticker,
            position=position,
        )
        return result["result"]

    async def delete_sticker_from_set(self: "tgram.TgBot", sticker: str) -> bool:
        """https://core.telegram.org/bots/api/#deletestickerfromset"""
        result = await self._send_request(
            "deleteStickerFromSet",
            sticker=sticker,
        )
        return result["result"]

    async def replace_sticker_in_set(
        self: "tgram.TgBot",
        user_id: int,
        name: str,
        old_sticker: str,
        sticker: InputSticker,
    ) -> bool:
        """https://core.telegram.org/bots/api/#replacestickerinset"""
        result = await self._send_request(
            "replaceStickerInSet",
            user_id=user_id,
            name=name,
            old_sticker=old_sticker,
            sticker=sticker,
        )
        return result["result"]

    async def set_sticker_emoji_list(
        self: "tgram.TgBot", sticker: str, emoji_list: List[str]
    ) -> bool:
        """https://core.telegram.org/bots/api/#setstickeremojilist"""
        result = await self._send_request(
            "setStickerEmojiList",
            sticker=sticker,
            emoji_list=emoji_list,
        )
        return result["result"]

    async def set_sticker_keywords(
        self: "tgram.TgBot", sticker: str, keywords: List[str] = None
    ) -> bool:
        """https://core.telegram.org/bots/api/#setstickerkeywords"""
        result = await self._send_request(
            "setStickerKeywords",
            sticker=sticker,
            keywords=keywords,
        )
        return result["result"]

    async def set_sticker_mask_position(
        self: "tgram.TgBot", sticker: str, mask_position: MaskPosition = None
    ) -> bool:
        """https://core.telegram.org/bots/api/#setstickermaskposition"""
        result = await self._send_request(
            "setStickerMaskPosition",
            sticker=sticker,
            mask_position=mask_position,
        )
        return result["result"]

    async def set_sticker_set_title(self: "tgram.TgBot", name: str, title: str) -> bool:
        """https://core.telegram.org/bots/api/#setstickersettitle"""
        result = await self._send_request(
            "setStickerSetTitle",
            name=name,
            title=title,
        )
        return result["result"]

    async def set_sticker_set_thumbnail(
        self: "tgram.TgBot",
        name: str,
        user_id: int,
        format: str,
        thumbnail: Union[InputFile, str] = None,
    ) -> bool:
        """https://core.telegram.org/bots/api/#setstickersetthumbnail"""
        result = await self._send_request(
            "setStickerSetThumbnail",
            name=name,
            user_id=user_id,
            format=format,
            thumbnail=thumbnail,
        )
        return result["result"]

    async def set_custom_emoji_sticker_set_thumbnail(
        self: "tgram.TgBot", name: str, custom_emoji_id: str = None
    ) -> bool:
        """https://core.telegram.org/bots/api/#setcustomemojistickersetthumbnail"""
        result = await self._send_request(
            "setCustomEmojiStickerSetThumbnail",
            name=name,
            custom_emoji_id=custom_emoji_id,
        )
        return result["result"]

    async def delete_sticker_set(self: "tgram.TgBot", name: str) -> bool:
        """https://core.telegram.org/bots/api/#deletestickerset"""
        result = await self._send_request(
            "deleteStickerSet",
            name=name,
        )
        return result["result"]

    async def answer_inline_query(
        self: "tgram.TgBot",
        inline_query_id: str,
        results: List[InlineQueryResult],
        cache_time: int = None,
        is_personal: bool = None,
        next_offset: str = None,
        button: InlineQueryResultsButton = None,
    ) -> bool:
        """https://core.telegram.org/bots/api/#answerinlinequery"""
        result = await self._send_request(
            "answerInlineQuery",
            inline_query_id=inline_query_id,
            results=results,
            cache_time=cache_time,
            is_personal=is_personal,
            next_offset=next_offset,
            button=button,
        )
        return result["result"]

    async def answer_web_app_query(
        self: "tgram.TgBot", web_app_query_id: str, result: InlineQueryResult
    ) -> SentWebAppMessage:
        """https://core.telegram.org/bots/api/#answerwebappquery"""
        result = await self._send_request(
            "answerWebAppQuery",
            web_app_query_id=web_app_query_id,
            result=result,
        )
        return SentWebAppMessage._parse(me=self, d=result["result"])

    async def send_invoice(
        self: "tgram.TgBot",
        chat_id: Union[int, str],
        title: str,
        description: str,
        payload: str,
        currency: str,
        prices: List[LabeledPrice],
        message_thread_id: int = None,
        provider_token: str = None,
        max_tip_amount: int = None,
        suggested_tip_amounts: List[int] = None,
        start_parameter: str = None,
        provider_data: str = None,
        photo_url: str = None,
        photo_size: int = None,
        photo_width: int = None,
        photo_height: int = None,
        need_name: bool = None,
        need_phone_number: bool = None,
        need_email: bool = None,
        need_shipping_address: bool = None,
        send_phone_number_to_provider: bool = None,
        send_email_to_provider: bool = None,
        is_flexible: bool = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        message_effect_id: str = None,
        reply_parameters: ReplyParameters = None,
        reply_markup: InlineKeyboardMarkup = None,
    ) -> Message:
        """https://core.telegram.org/bots/api/#sendinvoice"""
        result = await self._send_request(
            "sendInvoice",
            chat_id=chat_id,
            title=title,
            description=description,
            payload=payload,
            currency=currency,
            prices=prices,
            message_thread_id=message_thread_id,
            provider_token=provider_token,
            max_tip_amount=max_tip_amount,
            suggested_tip_amounts=suggested_tip_amounts,
            start_parameter=start_parameter,
            provider_data=provider_data,
            photo_url=photo_url,
            photo_size=photo_size,
            photo_width=photo_width,
            photo_height=photo_height,
            need_name=need_name,
            need_phone_number=need_phone_number,
            need_email=need_email,
            need_shipping_address=need_shipping_address,
            send_phone_number_to_provider=send_phone_number_to_provider,
            send_email_to_provider=send_email_to_provider,
            is_flexible=is_flexible,
            disable_notification=disable_notification,
            protect_content=protect_content
            if protect_content is not None
            else self.protect_content,
            message_effect_id=message_effect_id,
            reply_parameters=reply_parameters,
            reply_markup=reply_markup,
        )
        return Message._parse(me=self, d=result["result"])

    async def create_invoice_link(
        self: "tgram.TgBot",
        title: str,
        description: str,
        payload: str,
        currency: str,
        prices: List[LabeledPrice],
        provider_token: str = None,
        max_tip_amount: int = None,
        suggested_tip_amounts: List[int] = None,
        provider_data: str = None,
        photo_url: str = None,
        photo_size: int = None,
        photo_width: int = None,
        photo_height: int = None,
        need_name: bool = None,
        need_phone_number: bool = None,
        need_email: bool = None,
        need_shipping_address: bool = None,
        send_phone_number_to_provider: bool = None,
        send_email_to_provider: bool = None,
        is_flexible: bool = None,
    ) -> str:
        """https://core.telegram.org/bots/api/#createinvoicelink"""
        result = await self._send_request(
            "createInvoiceLink",
            title=title,
            description=description,
            payload=payload,
            currency=currency,
            prices=prices,
            provider_token=provider_token,
            max_tip_amount=max_tip_amount,
            suggested_tip_amounts=suggested_tip_amounts,
            provider_data=provider_data,
            photo_url=photo_url,
            photo_size=photo_size,
            photo_width=photo_width,
            photo_height=photo_height,
            need_name=need_name,
            need_phone_number=need_phone_number,
            need_email=need_email,
            need_shipping_address=need_shipping_address,
            send_phone_number_to_provider=send_phone_number_to_provider,
            send_email_to_provider=send_email_to_provider,
            is_flexible=is_flexible,
        )
        return result["result"]

    async def answer_shipping_query(
        self: "tgram.TgBot",
        shipping_query_id: str,
        ok: bool,
        shipping_options: List[ShippingOption] = None,
        error_message: str = None,
    ) -> bool:
        """https://core.telegram.org/bots/api/#answershippingquery"""
        result = await self._send_request(
            "answerShippingQuery",
            shipping_query_id=shipping_query_id,
            ok=ok,
            shipping_options=shipping_options,
            error_message=error_message,
        )
        return result["result"]

    async def answer_pre_checkout_query(
        self: "tgram.TgBot",
        pre_checkout_query_id: str,
        ok: bool,
        error_message: str = None,
    ) -> bool:
        """https://core.telegram.org/bots/api/#answerprecheckoutquery"""
        result = await self._send_request(
            "answerPreCheckoutQuery",
            pre_checkout_query_id=pre_checkout_query_id,
            ok=ok,
            error_message=error_message,
        )
        return result["result"]

    async def get_star_transactions(
        self: "tgram.TgBot", offset: int = None, limit: int = None
    ) -> StarTransactions:
        """https://core.telegram.org/bots/api/#getstartransactions"""
        result = await self._send_request(
            "getStarTransactions",
            offset=offset,
            limit=limit,
        )
        return StarTransactions._parse(me=self, d=result["result"])

    async def refund_star_payment(
        self: "tgram.TgBot", user_id: int, telegram_payment_charge_id: str
    ) -> bool:
        """https://core.telegram.org/bots/api/#refundstarpayment"""
        result = await self._send_request(
            "refundStarPayment",
            user_id=user_id,
            telegram_payment_charge_id=telegram_payment_charge_id,
        )
        return result["result"]

    async def set_passport_data_errors(
        self: "tgram.TgBot", user_id: int, errors: List[PassportElementError]
    ) -> bool:
        """https://core.telegram.org/bots/api/#setpassportdataerrors"""
        result = await self._send_request(
            "setPassportDataErrors",
            user_id=user_id,
            errors=errors,
        )
        return result["result"]

    async def send_game(
        self: "tgram.TgBot",
        chat_id: int,
        game_short_name: str,
        business_connection_id: str = None,
        message_thread_id: int = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        message_effect_id: str = None,
        reply_parameters: ReplyParameters = None,
        reply_markup: InlineKeyboardMarkup = None,
    ) -> Message:
        """https://core.telegram.org/bots/api/#sendgame"""
        result = await self._send_request(
            "sendGame",
            chat_id=chat_id,
            game_short_name=game_short_name,
            business_connection_id=business_connection_id,
            message_thread_id=message_thread_id,
            disable_notification=disable_notification,
            protect_content=protect_content
            if protect_content is not None
            else self.protect_content,
            message_effect_id=message_effect_id,
            reply_parameters=reply_parameters,
            reply_markup=reply_markup,
        )
        return Message._parse(me=self, d=result["result"])

    async def set_game_score(
        self: "tgram.TgBot",
        user_id: int,
        score: int,
        force: bool = None,
        disable_edit_message: bool = None,
        chat_id: int = None,
        message_id: int = None,
        inline_message_id: str = None,
    ) -> Union[Message, bool]:
        """https://core.telegram.org/bots/api/#setgamescore"""
        result = await self._send_request(
            "setGameScore",
            user_id=user_id,
            score=score,
            force=force,
            disable_edit_message=disable_edit_message,
            chat_id=chat_id,
            message_id=message_id,
            inline_message_id=inline_message_id,
        )
        return (
            Message._parse(me=self, d=result["result"])
            if isinstance(result["result"], dict)
            else result["result"]
        )

    async def get_game_high_scores(
        self: "tgram.TgBot",
        user_id: int,
        chat_id: int = None,
        message_id: int = None,
        inline_message_id: str = None,
    ) -> List[GameHighScore]:
        """https://core.telegram.org/bots/api/#getgamehighscores"""
        result = await self._send_request(
            "getGameHighScores",
            user_id=user_id,
            chat_id=chat_id,
            message_id=message_id,
            inline_message_id=inline_message_id,
        )
        return [GameHighScore._parse(me=self, d=i) for i in result["result"]]
