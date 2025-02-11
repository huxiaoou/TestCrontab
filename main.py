from typing import Union
import pandas as pd
from transmatrix.data_api import Database


def fetch(lib: str, table: str, names: Union[list[str], str], conds: str) -> pd.DataFrame:

    var_str = ",".join(names) if isinstance(names, list) else names
    cmd_sql = f"SELECT {var_str} FROM {table}{f' WHERE {conds}' if conds else ''}"
    print(f"{cmd_sql}:")
    db = Database(lib)
    _df = db.query(query=cmd_sql)
    return _df


if __name__ == "__main__":

    data = fetch(
        lib="meta_data",
        table="future_bar_1day_aft",
        names=["code", "real_code", "`open`", "high", "low", "`close`"],
        conds="datetime == '2025-01-02 15:00:00'",
    )
    print(data)
