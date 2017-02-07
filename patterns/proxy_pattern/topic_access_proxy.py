class Forum:

    def __init__(self, *topic_name):
        self.__topic_name = topic_name

    def load_topic(self, topic_name):
        if topic_name in self.__topic_name:
            print('requested topic {} loaded successfully!'.format(topic_name))
        else:
            print('there is no topic with requested name!')



