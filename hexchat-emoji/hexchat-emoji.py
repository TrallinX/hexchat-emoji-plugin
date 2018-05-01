__module_name__ = "Emojized"
__module_version__ = "1.0"
__module_description__ = "Replays emoji aliases to emoji symbols"

import emoji
import hexchat

def emojizemess_sb(word, word_eol, userdata):
	hexchat.command("say " + emoji.emojize(word_eol[1], use_aliases=True))

def unload_cb(userdata):
    print(__module_name__, 'version', __module_version__, 'unloaded.')






hexchat.hook_command("em", emojizemess_sb, help="/em <message> replays emoji aliases to emoji symbols")
hexchat.hook_unload(unload_cb)

print(__module_name__, 'version', __module_version__, 'loaded.')
print(emoji.emojize("Поддержка емодзей нахуй:japanese_ogre:!", use_aliases=True))

