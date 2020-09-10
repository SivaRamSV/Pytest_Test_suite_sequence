
def pytest_addoption(parser):
    

    suite = parser.getgroup('suite')
    suite.addoption("--suite",
                    action="store",
                    default=False,
                    help="Mention the test suite type specified in the json file")



def pytest_collection_modifyitems(session, config, items):

    path =config.getoption('suite')
    if path:
        import json
        import operator
        try:
            with open('./test_suite_sequence.json') as f:
                data = json.load(f)
            if path in data:  
               
                get_seq_no=operator.itemgetter(0)
                temp_group={}
                for k,v in data[path].items():
                    for i in items:
                        if k.lower()in str(i):
                            temp_group[i]=data[path][k]
                            break
                grouped_items = {} 
                for k,v in temp_group.items():
                    order=0
                    order=temp_group[k]
                    grouped_items.setdefault(order, []).append(k)
                sorted_items = []
                temp_list = sorted((i for i in grouped_items.items() if i[0] >= 0),
                                    key=get_seq_no)
               
                sorted_items.extend([i[1] for i in temp_list])
                items[:] = [item for sublist in sorted_items for item in sublist]
                print(items)
            
                
        except FileNotFoundError:
            print("File Not found")


    



