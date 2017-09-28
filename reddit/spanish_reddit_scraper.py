# Alice Scott (260631443)
# For COMP 551 A1
# Reddit Scraper created for conversational spanish dataset collection.
# The top-level comments in each subreddit post mark the beginning of a new conversation.
# Nested comments are treated as replies to the top-most comment to prevent repetition.
# If the comment has a reply (i.e., there are at least two uid's in a conversation), then it is included in the dataset.
# A dictionary is used to keep track of which reddit username is associated with which uid.
# Creates an XML file with the following tags:
# <dialog>
# 	<s>
# 		<utt uid="1"></utt>
# 		<utt uid="2"></utt>
# 		...
# 	</s>
# </dialog>


import requests
import requests.auth
import praw
import pprint
from praw.models import MoreComments
import sys
from xml.sax.saxutils import escape

sys.stdout = open("/Users/alice/Dropbox/spanishCorpus3.xml", "w")

UserAgent = 'web:Ayikv0TdJZtd9g:v1.0 '
reddit = praw.Reddit(client_id='Ayikv0TdJZtd9g',
					 client_secret='g9hXw8LdXBPsKwUQuh3G8-bM5I0',
					 user_agent=UserAgent)

#use the top 1000 posts of the subreddit listed.
subreddit = reddit.subreddit("espanol").top(limit=1000)
			# reddit.subreddit("mexico").hot(limit=1000)
			# reddit.subreddit("es").top(limit=1000)
			# + reddit.subreddit("argentina").top(limit=1000)
			# + reddit.subreddit("redditores").top(limit=1000)
			# + reddit.subreddit("TechoBlanco").top(limit=1000)
			# + reddit.subreddit("animalesdeconsejo").top(limit=1000)
			# + reddit.subreddit("ateosmexicanos").top(limit=1000)
			# + reddit.subreddit("latinoamerica").top(limit=1000)
			# + reddit.subreddit("RolEnEspanol").top(limit=1000)
			# + reddit.subreddit("Cinefilos").top(limit=1000)
			# + reddit.subreddit("estadounidos").top(limit=1000)
			# + reddit.subreddit("penaajena").top(limit=1000)
			# + reddit.subreddit("ciencia").top(limit=1000)
			# + reddit.subreddit("programacion").top(limit=1000)
			# + reddit.subreddit("videojuego").top(limit=1000)

print '<dialog>'
for submission in subreddit:

	submission.comments.replace_more(limit=0)

	for comment in submission.comments.list():

		if comment.author is None: continue
		comment_id_dict = {comment.author.name : 1}

		#only creates a new conversation if there are replies to the comment.
		if (comment.replies):

			print '<s>'
			currentReplyUID = 1
			open_utt_tag = '<utt uid="%d">' % comment_id_dict[comment.author.name]
			close_utt_tag = '</utt>'
			print open_utt_tag + escape(comment.body.encode('utf-8', 'ignore')) + close_utt_tag
			
			for reply in comment.replies.list():

				if reply.author is None: continue
				if reply.author.name not in comment_id_dict:
					currentReplyUID += 1
					comment_id_dict.update({reply.author.name : currentReplyUID})
					open_utt_tag = '<utt uid="%d">' % comment_id_dict[reply.author.name]
					print  open_utt_tag + escape(reply.body.encode('utf-8', 'ignore')) + close_utt_tag
				else:
					open_utt_tag = '<utt uid="%d">' % comment_id_dict[reply.author.name]
					print  open_utt_tag + escape(reply.body.encode('utf-8', 'ignore')) + close_utt_tag

			print '</s>'
print '</dialog>'



		