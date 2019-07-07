def cycle_ckeck(node):

    marker1 = node
    marker2 = node

    while marker2 != None and marker2.nextnode != None:

        marker1 = node.nextnode
        marker2 = node.nextnode.nextnode

        if marker2 == marker1:
            return True

    return False


class Node(object):

    def __init__(self, value):
        self.value = value
        self.nextnode = None


def main():
    a = Node(1)
    b = Node(2)
    c = Node(3)

    a.nextnode = b
    b.nextnode = c
    c.nextnode = a
    print(cycle_ckeck(a))


if __name__ == "__main__":

    main()
