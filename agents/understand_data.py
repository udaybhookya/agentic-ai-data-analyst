from state import ReportState

def data_understanding_node(state: ReportState) -> ReportState:
    
    """
    This node is responsible for understanding the data.
    It will load the data, analyze its schema, and prepare it for further processing.
    """
    
    print("\n==========================================")
    print("I am in the data understanding node ... ")
    print("============================================")
    
    llm_model = state['llm_model']
    processed_tables = state['processed_tables'] 
    
    tables_list = processed_tables.keys()
    
    input_table_schemas = ""
    
    for one_table in tables_list:
        
        one_table_schema = processed_tables[one_table].schema
        
        input_table_schemas += f"Table name: {one_table}\n"
        input_table_schemas += f"Table Description: {one_table_schema['table_description'].unique()[0]}\n\n"
        input_table_schemas += f"Columns description of table {one_table}:\n"
        
        for idx, one_row in one_table_schema.iterrows():
            input_table_schemas += f"Column name: {one_row['column_name']}\n"
            input_table_schemas += f"Column description: {one_row['column_description']}\n"
            input_table_schemas += f"Column type: {one_row['data_type']}\n\n"
    
        input_table_schemas += "\n\n"
        
    print(input_table_schemas)
    
        
    return state