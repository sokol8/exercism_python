import logging
import re

logging.basicConfig(level=logging.DEBUG,
                    format='%(funcName)s : %(message)s',)

class SgfTree(object):
    def __init__(self, properties=None, children=None):
        self.properties = properties or {}
        self.children = children or []

    def __eq__(self, other):
        if not isinstance(other, SgfTree):
            return False
        for k, v in self.properties.items():
            if k not in other.properties:
                return False
            if other.properties[k] != v:
                return False
        for k in other.properties.keys():
            if k not in self.properties:
                return False
        if len(self.children) != len(other.children):
            return False
        for a, b in zip(self.children, other.children):
            if a != b:
                return False
        return True

    def __ne__(self, other):
        return not self == other


def parse(input_string):

    #node_regexp = re.compile('([A-Z]+)\\[([a-z1-9\\s]+)\\]')
    node_regexp = re.compile('([A-Z]+)\\[([\\]a-z1-9\\s\\]+)\\]')
    # ([A-Z]+)\[([\]a-z1-9\s\\]+)\]

    ######---------------- FUNCTIONS ----------------######

    def parse_node_properties(p_start, p_end):
        logging.debug("p_start: {} p_end: {}".format(p_start, p_end))

        props_string = input_string[p_start[0]+1 : p_end[0]]
        logging.debug("props_string: '{}'".format(props_string))

        parse_properties(props_string)

    def parse_properties(props_string):
        if not props_string:
            raise ValueError("Empty property string")

        if props_string[0] != ';':
            raise ValueError("Invalid format - missing ';' inside '{}'".format(props_string))

        i = props_string[1:].find(';')
        if i == -1:
            parse_node(props_string[1:])
        else:
            parse_node(props_string[1:i + 1])


    def parse_node(node):
        if not node:
            raise ValueError("Empty node")

        logging.debug('node: {}'.format(node))
        matched_groups = node_regexp.findall(node)
        if not matched_groups:
            raise ValueError("Invalid Node format")

        logging.debug('matched_groups: {}'.format(matched_groups))
        
    ######---------------- PARSING CODE ----------------######

    logging.debug('Let the Parsing commence...')
    logging.debug('parsing string "{}"'.format(input_string))

    if not input_string:
        raise ValueError("empty input_string")

    input_string = input_string.replace("\t", " ")
    list_view = enumerate(input_string)
    p_list = [t for t in list_view if t[1] == '(' or t[1] == ')'] #get all parentheses
    
    tree_stack = []
    tree = SgfTree()

    for idx, c in p_list:
        if c[0] == '(':
            logging.debug('(')

            t = SgfTree()
            if (len(tree_stack) == 0): #create our parent tree
                tree = t
                logging.debug('Creating Parrent Tree')

            tree_stack.append(t)
            if len(p_list) <= idx + 1:
                raise ValueError("Cannot parse. Incorrect file format")
            
            parse_node_properties(p_list[idx], p_list[idx + 1])




