def get_attr_number(node):
    score = len(node.attrib)
    
    for element in node:
        score = score + get_attr_number(element)
            
    return score