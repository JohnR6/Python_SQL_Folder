import pandas as pd

# Maximum value for a category
def max_val(df, category=str):
    return df[category].max()


# Minimum value for a category
def min_val(df, category=str):
    return df[category].min()


# Game with the highest numerical score in a category
def max_item(df, category=str) -> pd.DataFrame:
    return df.loc[df[category].idxmax()]


# Game with the lowest numerical score in a category
def min_item(df, category=str) -> pd.DataFrame:
    return df.loc[df[category].idxmin()]


# Average sales by platform and sales type
def avg_plat_sales(df, category=str) -> pd.Series:
    return df.groupby("Platform")[category].mean()


# Average sales by publisher and sales type
def avg_plat_sales(df, category=str) -> pd.Series:
    return df.groupby("Publisher")[category].mean()


# Number of games by platform
def games_by_platform(df) -> pd.Series:
    return df.groupby("Platform")["Name"].count()


# List of games by publisher (E optional)
def sort_by_publisher(df, exclude=0) -> pd.DataFrame:
    if exclude == 0:
        return df.loc[df['Rating']=="E"].sort_values("Publisher")
    else:
        return df.sort_values("Publisher")
    

# List of games E by Genre
def sort_by_genre(df) -> pd.DataFrame:
    return df.loc[df["Rating"]=="E"].sort_values("Genre")


# List of games by platform
def sort_by_platform(df) -> pd.DataFrame:
    return df.loc[df["Rating"]=="E"].sort_values("Genre")


# Update a row
def update_games(df, ind, col, val):
    df.loc[ind, col] = val
    df.to_csv("Video_Games_Sales_as_at_22_Dec_2016.csv", index=False)


# Add a row
def add_rows_to_games(**kwargs):
    ndf = pd.DataFrame(kwargs)
    ndf.to_csv("Video_Games_Sales_as_at_22_Dec_2016.csv", mode='a', index=False, header=False)


# Delete a row
def delete_row_from_games(df, col, val):
    df.drop(df.index[(df[col]==val)],axis=0,inplace=True)
    df.to_csv("Video_Games_Sales_as_at_22_Dec_2016.csv", index=False)