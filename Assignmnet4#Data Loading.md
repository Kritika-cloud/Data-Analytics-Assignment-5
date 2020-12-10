```python
#Importing Library Pandas
import pandas as pd
```


```python
#Loading Dataset
raw_df = pd.read_csv('youtube_dataset.csv',encoding='iso-8859-1')
raw_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>web-scraper-order</th>
      <th>web-scraper-start-url</th>
      <th>userID</th>
      <th>userID-href</th>
      <th>name</th>
      <th>uploads</th>
      <th>subscribers</th>
      <th>videoviews</th>
      <th>country</th>
      <th>channeltype</th>
      <th>usercreated</th>
      <th>grade</th>
      <th>YouTube_Link</th>
      <th>YouTube_Link-href</th>
      <th>TwitterHandle</th>
      <th>TwitterHandle-href</th>
      <th>InstagramHandle</th>
      <th>InstagramHandle-href</th>
      <th>MonthlyEarnings</th>
      <th>YearlyEarnings</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1553043067-5148</td>
      <td>https://socialblade.com/youtube/top/5000/mosts...</td>
      <td>PewDiePie</td>
      <td>https://socialblade.com/youtube/c/pewdiepie</td>
      <td>PewDiePie</td>
      <td>3779</td>
      <td>90210848</td>
      <td>20772365682</td>
      <td>US</td>
      <td>Entertainment</td>
      <td>Apr 29th, 2010</td>
      <td>A</td>
      <td>NaN</td>
      <td>https://youtube.com/channel/UC-lHJZR3Gqxm24_Vd...</td>
      <td>NaN</td>
      <td>https://twitter.com/pewdiepie</td>
      <td>NaN</td>
      <td>https://instagram.com/pewdiepie</td>
      <td>66.9K - 1.1M</td>
      <td>802.3K - 12.8M</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1553043063-5147</td>
      <td>https://socialblade.com/youtube/top/5000/mosts...</td>
      <td>T-Series</td>
      <td>https://socialblade.com/youtube/c/tseriesmusic</td>
      <td>T-Series</td>
      <td>13218</td>
      <td>90194329</td>
      <td>65092058996</td>
      <td>IN</td>
      <td>Music</td>
      <td>Mar 13th, 2006</td>
      <td>A++</td>
      <td>NaN</td>
      <td>https://youtube.com/channel/UCq-Fj5jknLsUf-MWS...</td>
      <td>NaN</td>
      <td>https://instagram.com/tseries.official</td>
      <td>NaN</td>
      <td>https://plus.google.com/115156822320080163368</td>
      <td>635.6K - 10.2M</td>
      <td>7.6M - 122M</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1553043059-5146</td>
      <td>https://socialblade.com/youtube/top/5000/mosts...</td>
      <td>Gaming</td>
      <td>https://socialblade.com/youtube/channel/UCOpNc...</td>
      <td>Gaming</td>
      <td>0</td>
      <td>81888222</td>
      <td>0</td>
      <td>NaN</td>
      <td>Games</td>
      <td>Dec 15th, 2013</td>
      <td>D-</td>
      <td>NaN</td>
      <td>https://youtube.com/channel/UCOpNcN46UbXVtpKMr...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>https://youtube.com/channel/UCOpNcN46UbXVtpKMr...</td>
      <td>0 - 0</td>
      <td>0 - 0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1553043055-5145</td>
      <td>https://socialblade.com/youtube/top/5000/mosts...</td>
      <td>YouTube Movies</td>
      <td>https://socialblade.com/youtube/channel/UClgRk...</td>
      <td>YouTube Movies</td>
      <td>0</td>
      <td>77413743</td>
      <td>0</td>
      <td>NaN</td>
      <td>Film</td>
      <td>Jun 10th, 2015</td>
      <td>D-</td>
      <td>NaN</td>
      <td>https://youtube.com/channel/UClgRkhTL3_hImCAmd...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>https://youtube.com/channel/UClgRkhTL3_hImCAmd...</td>
      <td>0 - 0</td>
      <td>0 - 0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1553043051-5144</td>
      <td>https://socialblade.com/youtube/top/5000/mosts...</td>
      <td>Sports</td>
      <td>https://socialblade.com/youtube/channel/UCEgdi...</td>
      <td>Sports</td>
      <td>0</td>
      <td>75622870</td>
      <td>0</td>
      <td>NaN</td>
      <td>Sports</td>
      <td>Dec 15th, 2013</td>
      <td>D-</td>
      <td>NaN</td>
      <td>https://youtube.com/channel/UCEgdi0XIXXZ-qJOFP...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>https://youtube.com/channel/UCEgdi0XIXXZ-qJOFP...</td>
      <td>0 - 0</td>
      <td>0 - 0</td>
    </tr>
  </tbody>
</table>
</div>




```python
#selecting top 1000 rows
first_1000=raw_df.iloc[:1000]
print(first_1000)
```

        web-scraper-order                              web-scraper-start-url  \
    0     1553043067-5148  https://socialblade.com/youtube/top/5000/mosts...   
    1     1553043063-5147  https://socialblade.com/youtube/top/5000/mosts...   
    2     1553043059-5146  https://socialblade.com/youtube/top/5000/mosts...   
    3     1553043055-5145  https://socialblade.com/youtube/top/5000/mosts...   
    4     1553043051-5144  https://socialblade.com/youtube/top/5000/mosts...   
    ..                ...                                                ...   
    995   1553037784-3900  https://socialblade.com/youtube/top/5000/mosts...   
    996   1553037792-3901  https://socialblade.com/youtube/top/5000/mosts...   
    997   1553037768-3897  https://socialblade.com/youtube/top/5000/mosts...   
    998   1553037724-3888  https://socialblade.com/youtube/top/5000/mosts...   
    999   1553037758-3896  https://socialblade.com/youtube/top/5000/mosts...   
    
                 userID                                        userID-href  \
    0         PewDiePie        https://socialblade.com/youtube/c/pewdiepie   
    1          T-Series     https://socialblade.com/youtube/c/tseriesmusic   
    2            Gaming  https://socialblade.com/youtube/channel/UCOpNc...   
    3    YouTube Movies  https://socialblade.com/youtube/channel/UClgRk...   
    4            Sports  https://socialblade.com/youtube/channel/UCEgdi...   
    ..              ...                                                ...   
    995   GloZell Green      https://socialblade.com/youtube/user/glozell1   
    996  ETV Jabardasth    https://socialblade.com/youtube/c/etvjabardasth   
    997  The Timeliners    https://socialblade.com/youtube/c/thetimeliners   
    998    Crafty Panda  https://socialblade.com/youtube/channel/UC03Rv...   
    999  Troom Troom PT  https://socialblade.com/youtube/channel/UCgCQl...   
    
                   name  uploads  subscribers   videoviews country    channeltype  \
    0         PewDiePie     3779     90210848  20772365682      US  Entertainment   
    1          T-Series    13218     90194329  65092058996      IN          Music   
    2            Gaming        0     81888222            0     NaN          Games   
    3    YouTube Movies        0     77413743            0     NaN           Film   
    4            Sports        0     75622870            0     NaN         Sports   
    ..              ...      ...          ...          ...     ...            ...   
    995   GloZell Green     2316      4719893    845298432      US         Comedy   
    996  ETV Jabardasth     3735      4719652   4290216700      IN         People   
    997  The Timeliners      191      4718880    459254149      IN  Entertainment   
    998    Crafty Panda       84      4712345    890158507      US          Howto   
    999  Troom Troom PT      444      4711742    880150449     NaN            NaN   
    
            usercreated grade YouTube_Link  \
    0    Apr 29th, 2010     A          NaN   
    1    Mar 13th, 2006   A++          NaN   
    2    Dec 15th, 2013    D-          NaN   
    3    Jun 10th, 2015    D-          NaN   
    4    Dec 15th, 2013    D-          NaN   
    ..              ...   ...          ...   
    995  Jan 26th, 2008    B-          NaN   
    996  Jul 14th, 2015     A          NaN   
    997   Feb 1st, 2014    B+          NaN   
    998   Dec 3rd, 2017     A          NaN   
    999  Apr 19th, 2015    A-          NaN   
    
                                         YouTube_Link-href TwitterHandle  \
    0    https://youtube.com/channel/UC-lHJZR3Gqxm24_Vd...           NaN   
    1    https://youtube.com/channel/UCq-Fj5jknLsUf-MWS...           NaN   
    2    https://youtube.com/channel/UCOpNcN46UbXVtpKMr...           NaN   
    3    https://youtube.com/channel/UClgRkhTL3_hImCAmd...           NaN   
    4    https://youtube.com/channel/UCEgdi0XIXXZ-qJOFP...           NaN   
    ..                                                 ...           ...   
    995  https://youtube.com/channel/UC7FhOuPmxz8spz_xv...           NaN   
    996  https://youtube.com/channel/UCnoqvTW4YZExfDeq7...           NaN   
    997  https://youtube.com/channel/UCTlnaHHQ75zlDg_fL...           NaN   
    998  https://youtube.com/channel/UC03RvJoIhm_fMwlUp...           NaN   
    999  https://youtube.com/channel/UCgCQlMYN2XypwYC2w...           NaN   
    
                               TwitterHandle-href InstagramHandle  \
    0               https://twitter.com/pewdiepie             NaN   
    1      https://instagram.com/tseries.official             NaN   
    2                                         NaN             NaN   
    3                                         NaN             NaN   
    4                                         NaN             NaN   
    ..                                        ...             ...   
    995            https://instagram.com/glozell/             NaN   
    996                                       NaN             NaN   
    997  https://www.instagram.com/thetimeliners/             NaN   
    998                                       NaN             NaN   
    999       https://www.facebook.com/troomhands             NaN   
    
                                      InstagramHandle-href   MonthlyEarnings  \
    0                      https://instagram.com/pewdiepie    66.9K - 1.1M   
    1        https://plus.google.com/115156822320080163368  635.6K - 10.2M   
    2    https://youtube.com/channel/UCOpNcN46UbXVtpKMr...           0 - 0   
    3    https://youtube.com/channel/UClgRkhTL3_hImCAmd...           0 - 0   
    4    https://youtube.com/channel/UCEgdi0XIXXZ-qJOFP...           0 - 0   
    ..                                                 ...               ...   
    995      https://plus.google.com/110057581739311657068      228 - 3.7K   
    996  https://youtube.com/channel/UCnoqvTW4YZExfDeq7...    50.5K - 808K   
    997      https://plus.google.com/102509388716102017341    5.6K - 90.3K   
    998  https://youtube.com/channel/UC03RvJoIhm_fMwlUp...  38.6K - 617.4K   
    999              https://www.instagram.com/troomtroom/  16.4K - 261.8K   
    
           YearlyEarnings  
    0    802.3K - 12.8M  
    1       7.6M - 122M  
    2             0 - 0  
    3             0 - 0  
    4             0 - 0  
    ..                ...  
    995    2.7K - 43.8K  
    996     606K - 9.7M  
    997    67.7K - 1.1M  
    998   463.1K - 7.4M  
    999   196.3K - 3.1M  
    
    [1000 rows x 20 columns]
    


```python
#CAlculating distribution of channel type
A = raw_df['channeltype'].value_counts()
print(A)
```

    Entertainment    1037
    Music             760
    Games             449
    People            392
    Comedy            275
    Howto             223
    Film              176
    Education         142
    Tech               78
    Sports             56
    News               55
    Autos              14
    Travel             11
    Animals             9
    Nonprofit           3
    Shows               1
    Name: channeltype, dtype: int64
    


```python
#Defining function to extract top 1000 rows and show distribution of channel type

def  distribution_channel_type(dataframe, number_of_rows):
     dataframe = dataframe.iloc[:number_of_rows]
     youtube = dataframe['channeltype'].value_counts()
     return youtube
distribution_channel_type(raw_df,1000)
```




    Entertainment    284
    Music            240
    Games            115
    Comedy            76
    People            72
    Howto             49
    Film              36
    Education         30
    Tech              19
    Sports            17
    News              17
    Autos              3
    Animals            2
    Nonprofit          1
    Travel             1
    Name: channeltype, dtype: int64




```python
# Selecting top 1000 rows
Loaded_csv = raw_df.iloc[:1000]
# Converting to csv file
Loaded_csv.to_csv('top1000.csv')

```


```python

```
