from tobrot.sample_config import Config

#Fill your all data, read readme for reference

#FOR CUSTOM COMMANDS READ REAME AND FILL THEM...

class Config(Config):
    TG_BOT_TOKEN= "1602328104:AAH6-swUwRLGv4KUrFrXsJBvHGU15pgzajc"
    APP_ID = 3069192
    API_HASH = "6ac35bf0f4dc633fe98e57187b6adec6"
    OWNER_ID = 493291042
    AUTH_CHANNEL = [-515470340]
    DESTINATION_FOLDER = "TelegramBot" #Name of your folder read readme(not id of the folder)
    #Just don't fill RCLONE_CONFIG vars, insted copy your rclone.conf file in root directory
    #if your wanted to fill -- fill your rclone config like this(Your config may have some extra value or less. so Don't worry)
    RCLONE_CONFIG = """type = drive\n
client_id = 339402946333-7kqjcr4npd0jcbp8gjecbvdnl15081ia.apps.googleusercontent.com\n
client_secret = 146Viz2F4wiSCVkzYdrW1OIe\n
scope = drive\n
token = {"access_token":"ya29.A0AfH6SMCjf1lkBxSG5DK25Zm98pX_AQcDIO8hxR6ZmtyVHqGJqA9dUCmHf8LWsZlQOM-ml_gRNmDjDnCb1DRtsopb-aQaLKovqbpMxJbfhPOhqqlrX3TSQOn3-RDrf_ttixnCy5prWCoVIJjWuuYCiGbHBtkk","token_type":"Bearer","refresh_token":"1//0cW1aalFAyQAWCgYIARAAGAwSNwF-L9IrI4MapVj56WxdCyUSX3yTPMK_OtnBs1uXjVSvqrdZSXFptWwZb_wsGIpR_TeRpzBmprA","expiry":"2021-02-19T10:52:01.1612809+10:00"}"""
