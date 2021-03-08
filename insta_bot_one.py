from instapy import InstaPy

session = InstaPy(username="FlippinRedonkulous",
                  password="eNk{&4[*A)T+C)ZTUTft",
                  headless_browser=True)
session.login()

#Settings
session.set_do_like(enabled=True, percentage=100)
session.set_do_comment(enabled=True, percentage=75)
session.set_comments(['Nice!',u':fire:'])

#Activity
session.like_by_tags(['420'], amount=5)

session.end()
