import pandas as pd

# EDA: TABLE
def resumetable(df):
    print(f'Dataset Shape: {df.shape}')
    summary = pd.DataFrame(df.dtypes, columns=['DataType'])
    summary = summary.reset_index()
    summary = summary.rename(columns={'index':'feature'})
    summary['n_missing_values'] = df.isnull().sum().values
    summary['n_unique_values'] = df.nunique().values
    summary['first_value'] = df.loc[0].values               #get row
    summary['second_value'] = df.loc[1].values
    summary['third_value'] = df.loc[2].values
    return summary

# EDA: GRAPH
def write_percent(ax, total_size):
    '''
    Write percentage(height over total size) over each patches
    '''
    for patch in ax.patches:
        height = patch.get_height()
        width = patch.get_width()
        left_coord = patch.get_x()
        percent = height/total_size*100

        ax.text(
            x=left_coord+width/2.0
            , y = height + total_size*0.001
            , s=f'{percent:1.1f}%' #string
            , ha = 'center' #horizontal alignment
            )