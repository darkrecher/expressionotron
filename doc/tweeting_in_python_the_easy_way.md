# Tweeting in Python – the easy way

Origine du texte : https://wilsonericn.wordpress.com/2011/08/22/tweeting-in-python-the-easy-way/

Suppose you want to send tweets from Python code from your own Twitter account. How hard could that be? It’s Python, so the batteries are included right?

It turns out that the Python side is pretty slick, but there are some issues about interacting with Twitter that aren’t as easy as you could imagine.

## Do I need to use a library?

The mature Python Twitter libraries, ([Python Twitter Tools] (http://mike.verdone.ca/twitter/), and [Python Twitter] (http://code.google.com/p/python-twitter/)) will allow you to do anything that you could want with the Twitter API. But you’re just trying to send tweets, you don’t need to look at your friends’ timelines’. Maybe [this approach] (http://www.daniellanger.com/blog/2009/08/tweeting-with-python/) is more what you are looking for ?

Well not exactly like that. That approach uses Basic Authentication, which is no longer supported. Whatever you do will require OAuth, so it’s definitely going to take less time to use a library for novice twitter devs.

## The absolute easiest way

First install Python Twitter Tools (PTT) using easy_install. To allow PTT to access your account, type twitter at the command-line to initiate the authentication dance.

When that process is complete, you can tweet by executing the following command

`$ twitter -eyour.address@email.com set Put your tweet here!`

Now, the easiest way to tweet from Python, is to call the previous shell command from Python:

    >>> import subprocess
    >>> msg = 'tweeting from Python!'
    >>> command = 'twitter -eyour.address@email.com set %s' % msg
    >>> subprocess.call(command, shell=True)

Of course, this is ridiculous. We install a Python tool, so that we can call the command-line interface of that tool from Python? There must be a better way!

There is a better way, but because of the authentication complications, if you simply need to send tweets from one machine using one twitter account, there is no easier way.

## A better way

Alright, let’s do it right. If we take a look at the docs, we find that the first step is:

    |  Examples::
    |
    |    twitter = Twitter(
    |        auth=OAuth(token, token_key, con_secret, con_secret_key))
    |

which immediately raises at least four questions. The meta-question is this: Can’t I just use my username and password? No, you can’t, at least not with the Twitter API. Basic authentication has been phased out, in favor of a scheme that will allow Twitter applications to access others’ accounts without knowledge of their passwords, but with their permission.

If you read the PTT docs to understand what values to give the OAuth you will get nowhere. The PTT docs assume familiarity with the Twitter API. If you spend some time in the Twitter docs reading about OAuth, you will likely be frustrated with the disconnect between what OAuth is built to do, with this complicated handshake your app can perform with a twitter account, and the very simple task that you had in mind.

**The solution**: You need to register your application with Twitter. This sounds like overkill, we’re just talking about a script to tweet that the build broke, or something. But it can be quick and painless (if you read the rest of this post), and it’s the only way to get those required codes.

 - Sign in to http://dev.twitter.com and click on the button to create an application. You can put in a placeholder for the URL.
 - Since you want to send tweets, click on the ‘Settings’ tab change to ‘Read and Write,’ and click ‘Update.’
 - Now go back to the ‘Details’ tab. You will see a ‘Consumer key’ and ‘Consumer secret’ are visible, and there is a button to click to ‘Create my access token.’ Click that button to obtain all four codes. If you did this before step 2, you will need to recreate these codes, as they are connected to the particular settings.
 - There is some ambiguity (or error?) about which key/token/secret goes where. Here is the mapping from the names used within the Twitter docs to the variable names used in PTT:

 - Consumer key -> con_secret
 - Consumer secret ->con_secret_key
 - Access token -> token
 - Access token secret -> token_key

Don’t ask me, I’m just telling you what worked.

With that in place, it could hardly be easier:

    my_auth = twitter.OAuth(TOKEN,TOKEN_KEY,CON_SEC,CON_SEC_KEY)
    twit = twitter.Twitter(auth=my_auth)
    twit.statuses.update(status="I'm tweeting from Python!")
