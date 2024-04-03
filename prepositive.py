import pandas as pd
from datetime import datetime

# Assuming you have a CSV file named 'Tweet.csv'
input_file_path = 'D:\\cr\\stock\\Tweet.csv'
#output_file_path = 'D:\\cr\\stock\\output1.csv'


df = pd.read_csv(input_file_path)


# Convert the 'timestamp' column to datetime
df['new_date'] = pd.to_datetime(df['post_date'], unit='s').dt.date

# Sort the DataFrame by date and other columns as needed
columns_to_sort = ['tweet_id','writer',	'post_date','body','comment_num','retweet_num','like_num','new_date']

df = df.sort_values(by=columns_to_sort, ascending=[True, False, False,False, False,False, False,False])

# Group by date and select the top 25 rows per date
top_25_per_date = df.groupby('new_date').head(25)

# Display the result
#print(top_25_per_date)

# Save the result to a new CSV file
top_25_per_date.to_csv('prepositive.csv', index=False)

df = pd.read_csv('prepositive.csv')

# Assuming your CSV has a 'date' column in datetime format, if not, you may need to convert it
df['new_date'] = pd.to_datetime(df['new_date'])

# Group by date and aggregate tweets into a list
grouped_data = df.groupby('new_date')['body'].agg(list).reset_index()

# Transpose the tweets from vertical to horizontal
transposed_tweets = pd.DataFrame(grouped_data['body'].tolist(), index=grouped_data['new_date'])

# Write the transposed data to a new CSV file
transposed_tweets.to_csv('prepositive.csv')
