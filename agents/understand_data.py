from state import ReportState

def data_understanding_node(state: ReportState) -> ReportState:
    
    """
    This node is responsible for understanding the data.
    It will load the data, analyze its schema, and prepare it for further processing.
    """
    
    print("\n==========================================")
    print("I am in the data understanding node ... ")
    print("============================================")
        
    return state