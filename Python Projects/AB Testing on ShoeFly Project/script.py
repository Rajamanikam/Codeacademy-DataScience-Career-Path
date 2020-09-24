import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')

print(ad_clicks.head(5))

# To find count of ad clicks through each utm_source's 
source_count = ad_clicks.groupby('utm_source').user_id.count().reset_index()

print(source_count)

# To check whether the ad is displayed
ad_clicks['is_click'] = ~ad_clicks.ad_click_timestamp.isnull()

print(ad_clicks)

# percent of people who clicked on ads from each utm_source

clicks_by_source = ad_clicks.groupby(['utm_source','is_click']).user_id.count().reset_index() 

print(clicks_by_source)

#Pivotting the table

clicks_pivot = clicks_by_source.pivot(columns = 'is_click',
index='utm_source',
values='user_id').reset_index()

print(clicks_pivot)

#  percent of users who clicked on the ad from each utm_source

clicks_pivot['percent_clicked'] =  clicks_pivot[True] / (clicks_pivot[True] + clicks_pivot[False])

print(clicks_pivot)

# Add groups view by No of users

Ad_group = ad_clicks.groupby('experimental_group').user_id.count().reset_index()

print(Ad_group)

# check to see if a greater percentage of users clicked on Ad A or Ad B.

Ad_group_percent = ad_clicks.groupby(['experimental_group','is_click']).user_id.count().reset_index().pivot(
index = 'experimental_group',
columns = 'is_click',
values = 'user_id'
).reset_index()

print(Ad_group_percent)

a_clicks = ad_clicks[ad_clicks.experimental_group == 'A']

b_clicks = ad_clicks[ad_clicks.experimental_group == 'B']

#For A

a_clicks_pivot = a_clicks.groupby(['is_click', 'day']).count().reset_index().pivot(
  index = 'day',
  columns = 'is_click',
  values = 'user_id'
).reset_index()

a_clicks_pivot['percent_clicked'] = a_clicks_pivot[True] / a_clicks_pivot[True] + a_clicks_pivot[False] 

print(a_clicks_pivot)

#For B

b_clicks_pivot = b_clicks.groupby(['is_click', 'day']).count().reset_index().pivot(
  index = 'day',
  columns = 'is_click',
  values = 'user_id'
).reset_index()

b_clicks_pivot['percent_clicked'] = b_clicks_pivot[True] / b_clicks_pivot[True] + b_clicks_pivot[False] 

print(b_clicks_pivot)