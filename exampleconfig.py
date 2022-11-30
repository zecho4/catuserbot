from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 1141864
    API_HASH = "c8977b1d6b199cde071b2b9bab06e43a"
    # the name to display in your alive message
    ALIVE_NAME = "ril bot"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "postgres://hcqkqjrn:iNfxe5aFIXzJTLqpfU9iWXgdj7OzHSyB@hansken.db.elephantsql.com/hcqkqjrn"
    # After cloning the repo and installing requirements do python3 stringsetup.py an fill that value with this
    STRING_SESSION = "1BVtsOMEBuxPyA3_rMbEc-HWQyfMeXLsFhZbZ0CG70_Ssc8j0bEyolAK_GwAHcBQfy22o9NglDgvdSsNXamdL2eJ1FT5iLaljhl7WOzyOrqG2fwoSldIUCz1WUnSVOs-GEV-yDKwn7kzlyG8FppVpuRUDNBfpC321f_thlT-uYcZQtZIJy2vDXbmWs_ytJVJQ2aVu1wr-nt1lnh1Ff_ogrVQYeDq2IlNZYWbY5pNfVkDNmKXfgOQgHNIBBOgwll7DhmJHQcE-htMTGl2oB3h6ZZErW_Z-_Fg5COn2dZu9kX-tyhlGJjBUbqagGp30FkngtpkncL2nZpR1bYV0C-OAA_cu1SYWM="
    # create a new bot in @botfather and fill the following vales with bottoken
    TG_BOT_TOKEN = "5876358843:AAFBwdxL3Ev11aqLcQR8_xkvOTyrmDWStY0"
    # create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
    PRIVATE_GROUP_BOT_API_ID = -1001841648449
    # command handler
    COMMAND_HAND_LER = "."
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "."
    # External plugins repo
    EXTERNAL_REPO = "https://github.com/TgCatUB/CatPlugins"
    # if you need badcat plugins set "True"
    BADCAT = "True"
