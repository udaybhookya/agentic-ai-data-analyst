import os
import pandas as pd
from typing import Dict, NamedTuple

class Table(NamedTuple):
    df: pd.DataFrame
    schema: pd.DataFrame

def load_data(
    input_files:  list[str],
    schema_files: list[str],
    data_path:    str,
    schema_path:  str,
    data_type:    str = "csv",
) -> Dict[str, Table]:
    
    print("\n==================")
    print("Loading data...")
    print("=================")
    """
    Load multiple tables and their corresponding schema files into DataFrames.

    Args:
        input_files (list[str]):
            List of base filenames (without extension) for the data tables.
        schema_files (list[str]):
            List of base filenames (without extension) for the schemas.
        data_path (str):
            Directory where data files reside.
        schema_path (str):
            Directory where schema files reside.
        data_type (str, optional):
            File type/extension to load (“csv” or “json”). Defaults to "csv".

    Returns:
        Dict[str, Table]:
            A mapping from each table’s base name to a Table(df, schema) tuple.
    """
    tables: Dict[str, Table] = {}

    for file_name, schema_name in zip(input_files, schema_files):
        data_fp   = os.path.join(data_path,   f"{file_name}.{data_type}")
        schema_fp = os.path.join(schema_path, f"{schema_name}.{data_type}")

        if data_type == "csv":
            df     = pd.read_csv(data_fp)
            schema = pd.read_csv(schema_fp)
        elif data_type == "json":
            df     = pd.read_json(data_fp)
            schema = pd.read_json(schema_fp)
        else:
            raise ValueError(f"Unsupported file type: {data_type!r}")

        tables[file_name] = Table(df=df, schema=schema)

    return tables
