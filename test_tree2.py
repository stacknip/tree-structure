class Node():
    node_list = []
    def __new__(cls, unique, name):
        if cls.in_node_list(klass=unique):
            cls.createnew = False
            return cls.get_node_from_list(unique=unique)
        cls.createnew = True
        return super().__new__(cls)

    def __init__(self, unique, name):
        if __class__.createnew == True:
            self.unique = unique
            self.name = name
            self.parents = []
            self.childeren = []
            self.node_list.append(self)
        del __class__.createnew

    def __repr__(self):
        return self.name

    def add_parents(self, parents):
        # check if parents have nodes in the "node_list".
        # check if parents are in the list "self.parents".
        for parent in parents:
            node = __class__(unique=parent, name=parent.__name__)
            if not node in self.parents:
                self.parents.append(node)
            if not self in node.childeren:
                node.childeren.append(self)

    @classmethod
    def in_node_list(cls, klass):
        for node in cls.node_list:
            if node.unique == klass:
                return True
        return False

    @classmethod
    def get_node_from_list(cls, unique):
        for node in cls.node_list:
            if node.unique == unique:
                return node
        return None

def get_node(klass):
    return Node(unique=klass, name=klass.__name__)

def handle_tuple(hier_tuple):
    node = get_node(hier_tuple[0])
    node.add_parents(hier_tuple[1])

def dispatch(hier_list):
    for item in hier_list:
        if type(item) is tuple:
            handle_tuple(item)
        elif type(item) is list:
            dispatch(hier_list=item)
    return Node.node_list
