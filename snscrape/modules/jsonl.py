import json

# parse JSONL with indentations
def parse(filename):
    # list of items
    items = []

    # open JSONL file
    with open(filename, 'r') as f:
        # remove first and last two characters
        data = f.read()[1:-2]
        
        # extract JSON items
        data = data.split('}\n{')
        
        # loop over data items
        for item in data:
            # parse item to python dictionary type
            item_dict = json.loads('{' + item + '}')
            
            # append parsed item to item list
            items.append(item_dict)
        
        # return list of parsed items
        return items

# tests
if __name__ == '__main__':
    # call parse
    data = parse(tweet.jsonl')
