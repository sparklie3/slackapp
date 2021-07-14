import os
import logger #didn't import this before so logger didn't work
# Use the package we installed
from slack_bolt import App
from slack_sdk import WebClient
from flask import jsonify

# Initializes your app with your bot token and signing secret
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)

client = WebClient(token=os.environ.get("SLACK_BOT_TOKEN"))

# Add functionality here
@app.command("/start")
def handle_command(body, ack, respond, client, logger):
    # logger.debug(body) # there are different levels of logging, DEBUG, INFO, WARNING, ERROR, CRITICAL
    ack(#this is also part of the message acknol
        text="Accepted!",
        blocks=[
            {
                "type": "section",
                "block_id": "b",
                "text": {
                    "type": "mrkdwn",
                    "text": ":white_check_mark: Accepted!",
                },
            }
        ],
    )

    respond( #this is part of the msesage and handle a response id
        blocks=[
            {
                "type": "section",
                "block_id": "b",
                "text": {
                    "type": "mrkdwn",
                    "text": "You can add a button alongside text in your message. ",
                },
                "accessory": {
                    "type": "button",
                    "action_id": "a",
                    "text": {"type": "plain_text", "text": "Button"},
                    "value": "submit",
                },
            }
        ]
    )

    res = client.views_open(
        trigger_id=body["trigger_id"], #required to kick of the modal view
        view={
          "type": "modal",
          "submit": {
            "type": "plain_text",
            "text": "Submit",
            ""
            "emoji": True
          },
          "close": {
            "type": "plain_text",
            "text": "Cancel",
            "emoji": True
          },
          "title": {
            "type": "plain_text",
            "text": "Modal",
            "emoji": True
          },
          "blocks": [
            {
              "type": "section",
              "text": {
                "type": "plain_text",
                "text": ":wave: Hey {user}!\n\n Tell me something about yourself",
                "emoji": True
              }
            },
            {
              "type": "divider"
            },
            {
              "type": "input",
              "optional": True,
              "label": {
                "type": "plain_text",
                "text": "Select a channel to post the result on",
              },
              "element": {
                "action_id": "my_action_id",
                "type": "conversations_select",
                "default_to_current_conversation": True,
                "response_url_enabled": True
              },
            },
            {
              "type": "input",
              "label": {
                "type": "plain_text",
                "text": "What is the client's name?",
                "emoji": True
              },
              "element": {
                "type": "plain_text_input",
                "multiline": False
              }
            },
            {
              "type": "input",
              "label": {
                "type": "plain_text",
                "text": "What the the client's tier (based on ARR)",
                "emoji": True
              },
              "element": {
                "type": "multi_static_select",
                "placeholder": {
                  "type": "plain_text",
                  "text": "Select a tier",
                  "emoji": True
                },
                "options": [
                  {
                    "text": {
                      "type": "plain_text",
                      "text": ":one: Tier One",
                      "emoji": True
                    },
                    "value": "value-1"
                  },
                  {
                    "text": {
                      "type": "plain_text",
                      "text": ":two: Tier Two ",
                      "emoji": True
                    },
                    "value": "value-2"
                  },
                  {
                    "text": {
                      "type": "plain_text",
                      "text": ":three: Tier Three",
                      "emoji": True
                    },
                    "value": "value-3"
                  }
                ]
              }
            },
            {
              "type": "input",
              "label": {
                "type": "plain_text",
                "text": "Anything else you want to tell us?",
                "emoji": True
              },
              "element": {
                "type": "plain_text_input",
                "multiline": True
              },
              "optional": True
            }
          ]
        },
    )




# @app.view("view-id")
# def view_submission(ack, body, logger):
#     ack(
#         text="Submitted!",
#         blocks=[
#             {
#                 "type": "section",
#                 "text": {
#                     "type": "mrkdwn",
#                     "text": ":white_check_mark: Accepted!",
#                 },
#             }
#         ],
#     )
#     logger.debug(body["view"]["state"]["values"])

@app.view("")
def handle_submit(ack, body, logger):
  ack(
    {
      "response_action": "clear" # this is how I handle closing all views
    }
  )
  logger.info(body["view"]["state"]["values"])
  # logger.info(body["view"]["my_action_id"]) ## This is wrong, but how do I get this specific action ID?

  # Call the conversations.list method using the WebClient
  result = client.chat_postMessage(
      channel="UARE1U8F8",
      text="Hello world!"
      # You could also use a blocks[] array to send richer content
  )
  # Print result, which includes information about the message (like TS)
  print(result)




# @app.action("a")
# def submit(ack, say):
#   ack(
    
#   )
#   say("respond to something")


# @app.action("a")
# def button_click(ack, body, respond):
#     ack()

#     user_id = body["user"]["id"]
#     # in_channel / dict
#     respond(
#         {
#             "response_type": "in_channel",
#             "replace_original": False,
#             "text": f"<@{user_id}> clicked a button! (in_channel)",
#         }
#     )
#     # ephemeral / kwargs
#     respond(
#         replace_original=False,
#         text=":white_check_mark: Done!",
#     )



#Listens to the specific event type on the Homepage
@app.event("app_home_opened")  
def update_home_tab(client, event, logger):
  try:
    # views.publish is the method that your app uses to push a view to the Home tab
    client.views_publish(
      # the user that opened your app's app home
      user_id=event["user"],
      # the view object that appears in the app home
      view={
        "type": "home",
        "callback_id": "home_view",

        # body of the view
        "blocks": [
          {
            "type": "section",
            "text": {
              "type": "mrkdwn",
              "text": "*Welcome to your _App's Home_* :tada:"
            }
          },
          {
            "type": "divider"
          },
          {
            "type": "section",
            "text": {
              "type": "mrkdwn",
              "text": "This button won't do much for now but you can set up a listener for it using the `actions()` method and passing its unique `action_id`. See an example in the `examples` folder within your Bolt app."
            }
          },
          {
            "type": "actions",
            "elements": [
              {
                "type": "button",
                "text": {
                  "type": "plain_text",
                  "text": "Click me!"
                }
              }
            ]
          }
        ]
      }
    )
  
  except Exception as e:
    logger.error(f"Error publishing home tab: {e}")


# Start your app
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))