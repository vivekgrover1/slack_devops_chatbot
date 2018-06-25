# slack_chatbot
It is based on [errbot](http://errbot.io) project.

## Install plugin for errbot

```
!repos install https://github.com/vivekgrover1/err-jenkins-plugins.git
```


## setup with docker-compose
### Step 1 clone the project

```
git clone https://github.com/vivekgrover1/slack_chatbot.git
```
### Step 2 edit the config.py with SLACK BOT Token

You can add bot integration in your slack workspace by following [Slack Bot Integration](https://get.slack.help/hc/en-us/articles/115005265703-Create-a-bot-for-your-workspace)

With the bot account created on Slack, you may configure the account in errbot by setting up BOT_IDENTITY as follows in config.py:

```
BOT_IDENTITY = {
    'token': 'xoxb-4426949411-aEM7...',
}
```
### step 3 edit the docker-compose.yml

Set the AWS Acess Key and AWS Secret key in docker-compose.yml as follows.
```
environment:
     - AWS_ACCESS_KEY=Axhkh..
     - AWS_SECRET_KEY=AWkhljjlj..
```
Mount the ec2_key from host to the container as follows.
```
volumes:
      - type: bind
        source: Enter the source path
        target: /root/errbot/ec2_key.pem
```

### Run the slack chatbot with docker-compose command
```
docker-compose up
docker-compose up -d for daemon mode
```
