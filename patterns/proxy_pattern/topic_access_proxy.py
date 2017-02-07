class Forum:

    def get_topics(self):
        return self.__topics

    def __init__(self, topic_access, topic_name):
        self.__topics = dict()
        self.__topics[topic_name] = topic_access

    def load_topic(self, topic_name):
        if topic_name in self.__topics:
            print('requested topic {} loaded successfully!'.format(topic_name))
        else:
            print('there is no topic with requested name!')


class UserAccess:

    GUEST = 'GUEST'
    USER = 'USER'
    ADMIN = 'ADMIN'


class User:

    def __init__(self, access):
        self.access = access


class ForumProxy:

    @staticmethod
    def load_topic(user: User, topic_name):
        forum = Forum(UserAccess.ADMIN, 'admin')
        topics = forum.get_topics()
        if topic_name in topics:
            if user.access == topics[topic_name]:
                forum.load_topic(topic_name)
            else:
                print('access denied! you have no required access! Yours is {}'
                      .format(user.access))
        else:
            print('there is no such topic on forum!')