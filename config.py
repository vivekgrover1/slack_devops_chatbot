import logging

# This is a minimal configuration to get you started with the Text mode.
# If you want to connect Errbot to chat services, checkout
# the options in the more complete config-template.py from here:
# https://raw.githubusercontent.com/errbotio/errbot/master/errbot/config-template.py

BACKEND = 'Slack'  # Errbot will start in text mode (console only mode) and will answer commands from there.

BOT_DATA_DIR = r'/root/errbot/data'
BOT_EXTRA_PLUGIN_DIR = r'/root/errbot/plugins'

BOT_IDENTITY = {
    'token': 'xoxb-247103507941-7cHoMFmBi3ctJyLpDGnl9hjl'
}

BOT_LOG_FILE = r'/root/errbot/errbot.log'
BOT_LOG_LEVEL = logging.ERROR

BOT_ADMINS = ('@vivek271091', )  # !! Don't leave that to "@CHANGE_ME" if you connect your errbot to a chat system !!

CORE_PLUGINS = ('ACLs', 'Help','repomgr')
