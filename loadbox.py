def load_box(fname):
    # Load pandas and box sdk
    from boxsdk import DeveloperTokenClient
    import pandas as pd
    
    client = DeveloperTokenClient()
    
    items = client.folder(folder_id='0').get_items(limit=100, offset=0)
    items = [str(i) for i in items]
    f = [i for i in items if fname in i]
    fid = int(f[0].split(' ')[3])
    
    file = client.file(file_id=fid).content()
    
    n = [i.split(',') for i in file.decode('UTF-8').split("\n")]
    return pd.DataFrame(n)
