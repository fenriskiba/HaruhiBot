import configparser

config = configparser.RawConfigParser()

config.add_section('DiscordConfig')
config.set('DiscordConfig', 'UserToken', '1111111111111111111111')

with open('Config.cfg', 'w') as configfile:
    config.write(configfile)