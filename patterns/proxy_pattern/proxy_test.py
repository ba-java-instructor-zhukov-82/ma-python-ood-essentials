from patterns.proxy_pattern.topic_access_proxy import Forum
from patterns.proxy_pattern.topic_access_proxy import UserAccess
from patterns.proxy_pattern.topic_access_proxy import User
from patterns.proxy_pattern.topic_access_proxy import ForumProxy


def forum_test_true():
    forum = Forum(UserAccess.ADMIN, 'admin')
    forum.load_topic(UserAccess.ADMIN, 'admin')


def forum_test_false():
    forum = Forum(UserAccess.ADMIN, 'admin')
    forum.load_topic(UserAccess.ADMIN, 'secret')


def proxy_forum_test_access_true():
    admin = User(UserAccess.ADMIN)
    ForumProxy.load_topic(admin, 'admin')


def proxy_forum_test_access_false():
    guest = User(UserAccess.GUEST)
    ForumProxy.load_topic(guest, 'admin')

def proxy_forum_test_topic_name_false():
    guest = User(UserAccess.GUEST)
    ForumProxy.load_topic(guest, 'secret')

# forum_test_true()
# forum_test_false()

proxy_forum_test_access_true()
proxy_forum_test_access_false()
proxy_forum_test_topic_name_false()
