import xlwings as xw
import pandas as pd


@xw.func
@xw.arg("df", pd.DataFrame)
@xw.ret(expand='table')
def describe(df, selection=None):
    if selection is not None:
        return df.loc[:, selection].describe()
    else:
        return df.describe()
