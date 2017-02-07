from patterns.proxy_pattern.topic_access_proxy import Forum


def forum_test_true():
    forum = Forum('admin')
    forum.load_topic('admin')


def forum_test_false():
    forum = Forum('admin')
    forum.load_topic('secret')


forum_test_true()
forum_test_false()