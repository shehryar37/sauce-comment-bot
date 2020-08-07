# SauceCommentBot by u/wizardhecate

import praw
import os
import time
import re
import random
import data


def main():
    reddit = login()

    # Makes an objects from the list of subreddits
    subreddit = reddit.subreddit("+".join(data.subreddit_list))

    for comment in subreddit.stream.comments(skip_existing=True):
        # Checks for request
        if re.search(data.sauce_request, comment.body.lower()):
            print("{} is asking for sauce: ({}{})".format(
                comment.author.name,
                comment.link_permalink,
                comment.id
            ))

            # Gets the submission that the comment is from
            submission = reddit.submission(comment.submission)

            find_sauce(comment, submission, comment.link_permalink)

        elif re.search("{}|{}".format(data.sauce_provided_regex, data.sauce_regex), comment.body.lower()) and len(comment.body) < 35:
            print("{} has posted sauce on a submission: ({}{})".format(
                comment.author.name,
                comment.link_permalink,
                comment.id
            ))

            reply_sauce(data.sauce_reply, comment,
                        comment.link_permalink, " provided")


def login():
    try:
        reddit = praw.Reddit(username="SauceCommentBot",
                             password="@Reddit123",
                             client_id="wQULoIPX2p5vkg",
                             client_secret="f_smlHjE0zrvozuV9VYGooUJ4Kg",
                             user_agent="SauceCommentBot by u/wizardhecate"
                             )

        # reddit = praw.Reddit(username=os.environ["USERNAME"],
        #                      password=os.environ["PASSWORD"],
        #                      client_id=os.environ["CLIENT_ID"],
        #                      client_secret=os.environ["CLIENT_SECRET"],
        #                      user_agent=os.environ["USER_AGENT"]
        #                      )

        print("Logged in")

        return reddit
    except:
        print("Failed to log in")


def find_sauce(request_comment, submission, link, is_submitter=True):

    bot = None

    submission.comments.replace_more(limit=None)
    for comment in submission.comments.list():
        # Checks if the commenter is OP
        if comment.is_submitter == is_submitter:
            # Checks if commenter used appropriate tags
            if re.search(data.sauce_regex, comment.body):
                print("{} has posted the sauce: ({}{})".format(
                    comment.author.name, link, comment.id))

                # Checks if a bot replied to the comment
                for reply in comment.replies._comments:
                    if reply.author.name in data.bots:
                        print("u/{} has replied to {}: {}{}".format(
                            reply.author.name,
                            comment.author.name,
                            link,
                            reply.id))

                        reply_sauce(reply.body, request_comment, link)

                        return
                else:
                    print("A sauce bot has not replied to {}".format(
                        comment.author.name))

            elif re.search(data.sauce_provided_regex, comment.body.lower()):
                print("{} has posted the (custom) sauce: ({}{})".format(
                    comment.author.name, link, comment.id))

                # Checks if SauceCommentBot has already replied to this commenter or not

                reply_sauce(comment.body, request_comment, link)

                return
    else:
        if is_submitter:
            find_sauce(request_comment, submission,
                       link, False)
        else:
            reply = data.default_replies[random.randint(
                0, len(data.default_replies) - 1)]
            reply_sauce(reply, request_comment, link,
                        extra_word=" no")


def reply_sauce(reply, request_comment, link, extra_word=""):
    try:
        sauce_comment = request_comment.reply(reply)
        print("Replied with{} sauce message: ({}{})".format(
            extra_word, link, sauce_comment.id))
    except Exception as e:
        print(e)


main()
