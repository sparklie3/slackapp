import os
import logger
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
@app.command("/cspal")
def handle_command(body, ack, respond, client, logger):
    logger.info(body) # there are different levels of logging, DEBUG, INFO, WARNING, ERROR, CRITICAL
    ack(#this is also part of the message acknol
        text="Accepted!",
        blocks=[
		{
			"type": "actions",
			"elements": [
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "Journey",
						"emoji": True
					},
					"value": "journey",
					"action_id": "actionId-0"
				}
			]
		},
		{
			"type": "actions",
			"elements": [
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "Business Review",
						"emoji": True
					},
					"value": "business-review",
					"action_id": "actionId-1"
				}
			]
		}
	],
    )

    respond( #this is part of the msesage and handle a response id
        # blocks=[
        #     {
        #         "type": "section",
        #         "block_id": "b",
        #         "text": {
        #             "type": "mrkdwn",
        #             "text": "You can add a button alongside text in your message. ",
        #         },
        #         "accessory": {
        #             "type": "button",
        #             "action_id": "a",
        #             "text": {"type": "plain_text", "text": "Button"},
        #             "value": "submit",
        #         },
        #     }
        # ]
    )

@app.action("actionId-1")
def handle_action(body, ack, respond, logger):
  logger.info(body)
  ack()
  respond( #this is part of the msesage and handle a response id
        # blocks=[
        #     {
        #         "type": "section",
        #         "block_id": "b",
        #         "text": {
        #             "type": "mrkdwn",
        #             "text": "You can add a button alongside text in your message. ",
        #         },
        #         "accessory": {
        #             "type": "button",
        #             "action_id": "a",
        #             "text": {"type": "plain_text", "text": "Button"},
        #             "value": "submit",
        #         },
        #     }
        # ]
    )
  # say("I see you clicked a button") #result in error, channel not found
  res = client.views_open(
        trigger_id=body["trigger_id"], #required to kick of the modal view
        view={
              "type": "modal",
              "title": {
                "type": "plain_text",
                "text": "Business Review",
                "emoji": True
              },
              "submit": {
                "type": "plain_text",
                "text": "Send",
                "emoji": True
              },
              "close": {
                "type": "plain_text",
                "text": "Cancel",
                "emoji": True
              },
              "blocks": [
                {
                  "type": "divider"
                },
                {
                  "type": "input",
                  "label": {
                    "type": "plain_text",
                    "text": "To"
                  },
                  "element": {
                    "action_id": "my_action_id",
                    "type": "conversations_select",
                    "default_to_current_conversation": True,
                    "response_url_enabled": True
                  }
                },
                {
                  "type": "input",
                  "element": {
                    "type": "static_select",
                    "placeholder": {
                      "type": "plain_text",
                      "text": "Select an item",
                      "emoji": True
                    },
                    "options": [
                      {
                        "text": {
                          "type": "plain_text",
                          "text": "*this is plain_text text*",
                          "emoji": True
                        },
                        "value": "value-0"
                      },
                      {
                        "text": {
                          "type": "plain_text",
                          "text": "*this is plain_text text*",
                          "emoji": True
                        },
                        "value": "value-1"
                      },
                      {
                        "text": {
                          "type": "plain_text",
                          "text": "*this is plain_text text*",
                          "emoji": True
                        },
                        "value": "value-2"
                      }
                    ],
                    "action_id": "static_select-action"
                  },
                  "label": {
                    "type": "plain_text",
                    "text": "Customer",
                    "emoji": True
                  }
                },
                {
                  "type": "input",
                  "element": {
                    "type": "static_select",
                    "placeholder": {
                      "type": "plain_text",
                      "text": "Select an item",
                      "emoji": True
                    },
                    "options": [
                      {
                        "text": {
                          "type": "plain_text",
                          "text": "*this is plain_text text*",
                          "emoji": True
                        },
                        "value": "value-0"
                      },
                      {
                        "text": {
                          "type": "plain_text",
                          "text": "*this is plain_text text*",
                          "emoji": True
                        },
                        "value": "value-1"
                      },
                      {
                        "text": {
                          "type": "plain_text",
                          "text": "*this is plain_text text*",
                          "emoji": True
                        },
                        "value": "value-2"
                      }
                    ],
                    "action_id": "static_select-action"
                  },
                  "label": {
                    "type": "plain_text",
                    "text": "Template",
                    "emoji": True
                  }
                },
                {
                  "type": "input",
                  "element": {
                    "type": "static_select",
                    "placeholder": {
                      "type": "plain_text",
                      "text": "Select an item",
                      "emoji": True
                    },
                    "options": [
                      {
                        "text": {
                          "type": "plain_text",
                          "text": "*this is plain_text text*",
                          "emoji": True
                        },
                        "value": "value-0"
                      },
                      {
                        "text": {
                          "type": "plain_text",
                          "text": "*this is plain_text text*",
                          "emoji": True
                        },
                        "value": "value-1"
                      },
                      {
                        "text": {
                          "type": "plain_text",
                          "text": "*this is plain_text text*",
                          "emoji": True
                        },
                        "value": "value-2"
                      }
                    ],
                    "action_id": "static_select-action"
                  },
                  "label": {
                    "type": "plain_text",
                    "text": "Ask",
                    "emoji": True
                  }
                },
                {
                  "type": "input",
                  "optional": True,
                  "element": {
                    "type": "plain_text_input",
                    "multiline": True,
                    "action_id": "plain_text_input-action"
                  },
                  "label": {
                    "type": "plain_text",
                    "text": "Message",
                    "emoji": True
                  }
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

# @app.view("")
# def handle_submit(ack, body, logger):
#   ack(
#     {
#       "response_action": "clear" # this is how I handle closing all views
#     }
#   )
#   logger.info(body["view"]["state"]["values"])
#   # logger.info(body["view"]["my_action_id"]) ## This is wrong, but how do I get this specific action ID?

#   # Call the conversations.list method using the WebClient
#   result = client.chat_postMessage(
#       channel="UARE1U8F8",
#       text="Hello world!"
#       # You could also use a blocks[] array to send richer content
#   )
#   # Print result, which includes information about the message (like TS)
#   print(result)




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