""" Pytest Configuration for Pytest-Suite-Execution"""
import json
import operator

def pytest_addoption(parser):

    suite = parser.getgroup('suite')
    suite.addoption("--suite_name",
                    action="store",
                    default=False,
                    help="Mention the test case type specified in the json file")
    suite.addoption("--suite_cfg",
                    action="store",
                    default=False,
                    help="Test suite json file location")
 
def pytest_collection_modifyitems(session, config, items):

    path = config.getoption('--suite_cfg')
    suite_name = config.getoption('--suite_name')
    
    if path and suite_name:
        try:
            with open(path) as f:

                data = json.load(f)

            if suite_name in data:

                get_seq_no = operator.itemgetter(0)
                temp_group={}

                for k,v in data[suite_name].items():
                    for i in items:
                        if k.lower()in str(i):
                            temp_group[i]=data[suite_name][k]
                            break

                _final_data={}
                { _final_data.setdefault(temp_group[k], []).append(k) for k,v in temp_group.items() } 

                _final_items_list = []

                temp_list = sorted( 
                                    (i for i in _final_data.items() if i[0] >= 0),key=get_seq_no
                                )

                _final_items_list.extend([i[1] for i in temp_list])
                items[:] = [item for sublist in _final_items_list for item in sublist]
            else:
                raise Exception ("CONFLICT IN SUITE NAME, RECHECK THE SUITE NAME ")    

        except Exception as e:

            print(str(e).upper())


    



