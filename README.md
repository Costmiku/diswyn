# diswyn
A general-purpose, self-hostable Discord bot.
```yaml
NOTE: THIS VERSION OF THE BOT IS DISCONTINUED, DISCORD.JS VERSION SOON TO COME
```

## Self-hosting the bot.
### Prerequisites
* Latest version of Python 3
* pip
* Discord bot application<br>

Here are the step to creating a Discord Bot account. (from [https://www.freecodecamp.org/news/create-a-discord-bot-with-python/](https://www.freecodecamp.org/news/create-a-discord-bot-with-python/))

* Make sure you’re logged on to the Discord website.
* Navigate to the application page.
* Click on the “New Application” button.
* Give the application a name and click “Create”.
* Go to the “Bot” tab and then click “Add Bot”. You will have to confirm by clicking "Yes, do it!"

Keep the default settings for **Public Bot** (checked) and **Require OAuth2 Code Grant** (unchecked).<br>
Your bot has been created. The next step is to copy the token.<br>
This token is your bot's password so don't share it with anybody. It could allow someone to log in to your bot and do all sorts of bad things.<br>
You can regenerate the token if it accidentally gets shared.<br>
### env.json
When you first install the bot, you may run it with `name_of_python3_interpreter main.py setup`. It will create a default `env.json` file like this:
```json
{
    "DISCORD_TOKEN": "bot token here",
    "ADDITIONAL_OWN_PERMS": []
}
```
If you specify an argument after `setup`, it will be used for the token. If you don't, open `env.json` and set the `"DISCORD_TOKEN"` field to your bot's token.<br>
If something goes wrong, you can always start anew by running `name_of_python3_interpreter main.py setup` again.

When you set up the bot using the setup command, a `server_data.json` file will be created. This will be used to store long-term data specific to servers such as tempmutes, tempbans etc.