import pandas as pd
from pandas.errors import EmptyDataError

def switch_data():
    # Define file paths
    prerelease_file_path = r'prerelease\\anime_list.csv'
    release_file_path = r'release\\anime_list.csv'

    # List of file paths to read
    file_paths = [prerelease_file_path, release_file_path]
    data_frames = {}

    # Read CSV files into DataFrames
    for file_path in file_paths:
        try:
            df = pd.read_csv(file_path, header=0)
            if df.empty:
                print(f"The file {file_path} is empty.")
                data_frames[file_path] = pd.DataFrame()  # Store an empty DataFrame
            else:
                data_frames[file_path] = df
        except EmptyDataError:
            print(f"The file {file_path} is empty or does not contain valid data.")
            data_frames[file_path] = pd.DataFrame()  # Store an empty DataFrame

    # Extract DataFrames
    prerelease_anime_list = data_frames[prerelease_file_path]
    release_anime_list = data_frames[release_file_path]

    
    try:
        last_row_release = release_anime_list.iloc[-1]    
    except IndexError:
        last_row_release = None 


    # Iterate over the prerelease_anime_list rows
    for index, row in prerelease_anime_list.iterrows():
        

        if release_anime_list.empty or prerelease_anime_list.empty:
            release_anime_list = pd.DataFrame(columns=['Anime'])
            release_anime_list.loc[0] = row
            release_anime_list.to_csv(release_file_path, index=False)
            break



        if not ((release_anime_list == row).all(axis=1)).any():
            # Append the row to release_anime_list
            release_anime_list.loc[len(release_anime_list)] = row
            release_anime_list.to_csv(release_file_path, index=False)
            break  # Exit after the first occurrence

    return release_anime_list

# Call the function
result = switch_data()
print(result)
