from TikTokApi import TikTokApi as tiktok
import json
from helpers import process_results 
import pandas as pd
import sys

def get_data(hashtag):
    verifyFp = "verify_kq7orxlv_L0lstuOR_sJTU_40Xd_BLi5_feBnRda28JuI"
    api = tiktok.get_instance(custom_verifyFp=verifyFp, use_test_endpoints=True)
    
    trending = api.by_hashtag(hashtag)

    flattened_data = process_results(trending)

    df = pd.DataFrame.from_dict(flattened_data, orient='index')
    df.to_csv('tiktokdata.csv', index=False)

if __name__ == '__main__':
    get_data(sys.argv[1])
