""" Pytest Configuration for Pytest-Suite-Execution"""
import json
import operator
import pytest

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
    suite.addoption("--precond",
                    action="store",
                    default=False,
                    help="Mention the test case for precond")

 
def pytest_sessionstart(session):
    session._ispc_fail = False
    session._pc_key = 'precond'

def pytest_runtest_makereport(item, call):
    markers = {str(marker.name).lower() for marker in item.iter_markers()}
    if call.excinfo is not None and item.session._pc_key in markers:
        item.session._ispc_fail = True
        
def pytest_runtest_setup(item):
    if item.session._ispc_fail:
        pytest.skip(item.name)
        

def pytest_collection_modifyitems(session, config, items):
    
    _pre_c_data = config.getoption('--precond')
    path = config.getoption('--suite_cfg')
    suite_name = config.getoption('--suite_name')
    if path and suite_name:
        try:
            with open(path) as f:
                data = json.load(f)
            if suite_name in data:
                if _pre_c_data:
                    t_pc_list = _pre_c_data.strip('][').split(",")
                    pc_list = [p_i.strip() for p_i in t_pc_list if len(p_i)>0]
                    if pc_list:
                        for c_pc in pc_list:
                            f=1
                            for c_i in items:
                                if str(c_pc).lower() in str(c_i).lower():
                                    f=0
                            if f == 1:
                                raise Exception("   PRECOND ERROR :Precondition Testcase "+str(c_pc)+" is not available     ")
                        { data[suite_name].update({pc_k:int(pc_v)+len(pc_list)}) for pc_k,pc_v in data[suite_name].items()}
                        for t_pc in enumerate(pc_list ,start = 1):
                            data[suite_name].update({t_pc[1]:int(t_pc[0])})
                    else:
                        raise Exception("   PRECOND ERROR : PRECONDTION ARRAY CANT BE EMPTY")
                        
                get_seq_no = operator.itemgetter(0)
                temp_group={}
                for k,v in data[suite_name].items():
                    f = 1
                    for i in items:
                        if str(k).lower() in str(i).lower():
                            f = 0
                            temp_group[i]=data[suite_name][k]
                            break
                    if f == 1:
                        raise Exception("   SUITE ERROR : TestCase "+str(k)+" is not available    ")
                _final_data={}
                { _final_data.setdefault(temp_group[k], []).append(k) for k,v in temp_group.items() } 
                _final_items_list = []
                temp_list = sorted( 
                                    (i for i in _final_data.items() if i[0] >= 0),key=get_seq_no
                                )
                _final_items_list.extend([i[1] for i in temp_list])
                items[:] = [item for sublist in _final_items_list for item in sublist]
            else:
                raise Exception ("   SUITE ERROR : CONFLICT IN SUITE NAME, RECHECK THE SUITE NAME ")    
        except Exception as e:
            pytest.exit(e)
    elif _pre_c_data:
        try:
            t_pc_list = _pre_c_data.strip('][').split(",")
            pc_list = [p_i.strip() for p_i in t_pc_list if len(p_i)>0]
            if pc_list:
                for c_pc in pc_list:
                    f=1
                    for c_i in items:
                        if str(c_pc).lower() in str(c_i).lower():
                            f=0
                    if f == 1:
                        raise Exception("   PRECOND ERROR :Precondition Testcase "+str(c_pc)+" is not available     ")
                pc_temp_list=[]
                [pc_temp_list.extend(j for i in pc_list for j in items if str(i).lower() in str(j).lower())]
                temp_items=[]
                [temp_items.extend(t_i for t_i in items if not t_i in pc_temp_list)]
                _final_items_list=[f_j for f_i in [pc_temp_list,temp_items] for f_j in f_i]
                items[:] = [item for item in _final_items_list]
            else:
                raise Exception("   PRECOND ERROR : PRECONDTION ARRAY CANT BE EMPTY     ")
        except Exception as e:
            pytest.exit(e)


    



