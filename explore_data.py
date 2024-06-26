import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def department_2016(train):
    """
    Data Exploration on department, store and turnober

    """
  
    """
    Which department made the highest turnover in 2016?
    """
    train_2016 = train[train['year'] == 2016]
    dept_turnover_2016 = train_2016.groupby('dpt_num_department')['turnover'].sum()

    plt.figure(figsize=(10, 6))
    dept_turnover_2016.plot(kind='bar', color='skyblue')
    plt.title('Total Turnover by Department for 2016')
    plt.xlabel('Department')
    plt.ylabel('Total Turnover')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

    highest_turnover_2016 = dept_turnover_2016.idxmax()
    highest_turnover_value_2016 = dept_turnover_2016.max()
    millions = highest_turnover_value_2016 / 1_000_000
    millions_formatted = f"{millions:.2f} million"

    print(f"The highest turnover department in 2016 is {highest_turnover_2016} and their turnover is {millions_formatted}")

def department88_2015(train):

    """
    What are the top 5 week numbers (1 to 53) for department 88 in 2015 in terms of turnover over all stores?
    
    """

    # Filter data for the year 2015 and department 88
    train_2015_dept88 = train[(train['day_id'].dt.year == 2015) & (train['dpt_num_department'] == 88)]

    # Extract week numbers
    train_2015_dept88['week_number'] = train_2015_dept88['day_id'].dt.isocalendar().week

    # Sum the turnover for each week
    weekly_turnover_2015_dept88 = train_2015_dept88.groupby('week_number')['turnover'].sum()
    # Find the top 5 weeks by turnover
    top_5_weeks_2015_dept88 = weekly_turnover_2015_dept88.nlargest(5)

    top_5_weeks_2015_dept88 = top_5_weeks_2015_dept88.reset_index()

    # Renaming the columns
    top_5_weeks_2015_dept88.columns = ['weeknumber', 'turnover']


    #Convert it into a dataframe
    weekly_turnover_2015_dept88 = weekly_turnover_2015_dept88.reset_index()
    # Renaming the columns
    weekly_turnover_2015_dept88.columns = ['weeknumber', 'turnover']
    # Sort the DataFrame by turnover in descending order and get the top 5 rows
    top_5_weeks_2015_dept88 = weekly_turnover_2015_dept88.nlargest(5, 'turnover')

    # Plotting the trend line
    plt.figure(figsize=(10, 6))
    plt.plot(weekly_turnover_2015_dept88['weeknumber'], weekly_turnover_2015_dept88['turnover'], marker='o', linestyle='-', color='b', label='Turnover')

    # Marking the top 5 highest turnover values
    plt.scatter(top_5_weeks_2015_dept88['weeknumber'], top_5_weeks_2015_dept88['turnover'], color='r', label='Top 5 Turnovers')

    # Annotating the top 5 highest turnover values with clearer text
    for i, row in top_5_weeks_2015_dept88.iterrows():
        plt.annotate(f"{row['turnover']:.2f}", (row['weeknumber'], row['turnover']), 
                    textcoords="offset points", xytext=(0,10), ha='center', fontsize=9, color='red')

    plt.xlabel('Week Number')
    plt.ylabel('Turnover')
    plt.title('Weekly Turnover for Department 88 in 2015')
    plt.legend()
    plt.grid(True)
    plt.tight_layout() 
    plt.show()

def performerstore_2014(train):

    """
    What was the top performer store in 2014?

    """

    # Filter data for the year 2014
    train_2014 = train[train['day_id'].dt.year == 2014]

    # Sum the turnover for each store
    store_turnover_2014 = train_2014.groupby('but_num_business_unit')['turnover'].sum()

    # Find the store with the highest turnover
    top_performer_store_2014 = store_turnover_2014.idxmax()
    top_performer_store_value_2014 = store_turnover_2014.max()


    # Get the top 10 performing stores
    top_stores = store_turnover_2014.nlargest(10)

    # Print the top store turnovers
    print(top_stores)

    # Draw a bar chart for the top performing stores
    plt.figure(figsize=(10, 6))
    top_stores.plot(kind='bar', color='skyblue')
    plt.title('Top 10 Performing Stores by Turnover for 2014')
    plt.xlabel('Store')
    plt.ylabel('Total Turnover')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

    # Formatting in lakhs
    lakhs = top_performer_store_value_2014 / 100_000
    lakhs_formatted = f"{lakhs:.2f} lakh"

    print("The top performer store is " + str(top_performer_store_2014) + "and the turnover of the store is " + str(lakhs_formatted))

def sportdepartment73(train):

    """
    Based on sales can you guess what kind of sport represents departement 73?
    
    """
    train_dept73 = train[train['dpt_num_department'] == 73]
    train_dept73 = train_dept73.groupby('day_id')['turnover'].sum()
    #Convert it into a dataframe
    train_dept73 = train_dept73.reset_index()
    # Renaming the columns
    train_dept73.columns = ['day_id', 'turnover']
    # Convert the 'date' column to datetime format
    train_dept73['day_id'] = pd.to_datetime(train_dept73['day_id'])
    # Set the 'date' column as the index
    train_dept73.set_index('day_id', inplace=True)


    monthly_data = train_dept73.resample('M').sum()
    monthly_data['Year-Month'] = monthly_data.index.strftime('%Y-%m')
    # Plot the data
    plt.figure(figsize=(16, 8))
    plt.plot(monthly_data['Year-Month'], monthly_data['turnover'], marker='o', linestyle='-')
    plt.title('Monthly Sales Turnover Over Time', fontsize=16)
    plt.xlabel('Year-Month', fontsize=14)
    plt.ylabel('Turnover', fontsize=14)
    plt.xticks(rotation=45, fontsize=12)
    plt.yticks(fontsize=12)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    print("""
    Possible sports that had high sales could be these:

    1. Cycling: Spring and early summer are prime seasons for cycling. As the weather improves, more people take to biking, whether for commuting, fitness, or recreation.
    2. Running: Similar to cycling, running is popular in the spring and summer. Many people start their outdoor running routines as the weather warms up.
    3. Outdoor Sports: This includes hiking, camping, and other outdoor activities. Spring and early summer are peak times for outdoor adventures.
    4. Water Sports: While more aligned with summer, water sports like kayaking, paddleboarding, and swimming could also see an increase starting in late spring.
    5. Team Sports: Sports like soccer and tennis are also popular during these months, with many leagues and recreational play starting in the spring.

    2016 had particularly high sales, this could be due to several factors:

    1. Major Sporting Events: If there were major sporting events in 2016, such as the Olympics or European Football Championship, these could drive sales in specific sports.
    2. Product Launches: New product launches or marketing campaigns by Decathlon in 2016 could have driven higher sales.
    """)

def sportdepartment117(train):

    """
    e. Based on sales can you guess what kind of sport represents departement 117?
    """
    train_dept117 = train[train['dpt_num_department'] == 117]

    train_dept117 = train_dept117.groupby('day_id')['turnover'].sum()
    #Convert it into a dataframe
    train_dept117 = train_dept117.reset_index()
    # Renaming the columns
    train_dept117.columns = ['day_id', 'turnover']

    # Convert the 'date' column to datetime format
    train_dept117['day_id'] = pd.to_datetime(train_dept117['day_id'])
    # Set the 'date' column as the index
    train_dept117.set_index('day_id', inplace=True)

    monthly_data = train_dept117.resample('M').sum()
    monthly_data['Year-Month'] = monthly_data.index.strftime('%Y-%m')
    # Plot the data
    plt.figure(figsize=(16, 8))
    plt.plot(monthly_data['Year-Month'], monthly_data['turnover'], marker='o', linestyle='-')
    plt.title('Monthly Sales Turnover Over Time', fontsize=16)
    plt.xlabel('Year-Month', fontsize=14)
    plt.ylabel('Turnover', fontsize=14)
    plt.xticks(rotation=45, fontsize=12)
    plt.yticks(fontsize=12)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    print("""Sport departments that might see higher sales during these months:

    1. Winter Sports:
    - Skiing and Snowboarding: Sales for skiing and snowboarding equipment typically peak in these months as people prepare for the winter sports season.
    - Ice Skating: Equipment for ice skating, including skates and accessories, also sees higher sales in winter.

    2. Fitness and Gym Equipment: As outdoor conditions become less favorable, many people move to indoor fitness activities. Sales for gym equipment, fitness gear, and accessories can increase.
    - Yoga and Pilates: These indoor activities also see a rise in participation during colder months.

    3. Hiking and Camping (Winter Gear):
    - Winter Hiking: There is specialized gear for winter hiking and camping, such as thermal clothing, snowshoes, and winter tents, which can drive sales.

    4. Holiday and Gift Purchases: The holiday season in December leads to higher sales of a wide range of sporting goods as gifts, including bicycles, sportswear, and various sporting accessories.
    """)



def geographical_analysis(train, feat):
    """
    Analyze geographical sales turnover by region.
    
    Args:
        train (pd.DataFrame): The training dataset containing turnover data.
        feat (pd.DataFrame): The features dataset containing geographical information.
    """
    merged_df = train.merge(feat, left_on='but_num_business_unit', right_on='but_num_business_unit')
    region_turnover = merged_df.groupby('but_region_idr_region')['turnover'].sum().reset_index()

    plt.figure(figsize=(10, 6))
    sns.barplot(x='but_region_idr_region', y='turnover', data=region_turnover)
    plt.title('Total Turnover by Region')
    plt.xlabel('Region')
    plt.ylabel('Total Turnover')
    plt.show()

def seasonal_trends(train):
    """
    Plot seasonal trends of sales turnover on a monthly and weekly basis.
    
    Args:
        train (pd.DataFrame): The training dataset containing turnover data.
    """
    monthly_turnover = train.groupby(['year', 'month'])['turnover'].sum().reset_index()
    plt.figure(figsize=(14, 7))
    sns.lineplot(x='month', y='turnover', hue='year', data=monthly_turnover, palette='tab10', marker='o')
    plt.title('Monthly Turnover Trends')
    plt.xlabel('Month')
    plt.ylabel('Total Turnover')
    plt.legend(title='Year')
    plt.show()

    weekly_turnover = train.groupby(['year', 'week'])['turnover'].sum().reset_index()
    plt.figure(figsize=(14, 7))
    sns.lineplot(x='week', y='turnover', hue='year', data=weekly_turnover, palette='tab10', marker='o')
    plt.title('Weekly Turnover Trends')
    plt.xlabel('Week')
    plt.ylabel('Total Turnover')
    plt.legend(title='Year')
    plt.show()

def correlation_analysis(train, feat):
    """
    Perform correlation analysis between sales turnover and geographical features.
    
    Args:
        train (pd.DataFrame): The training dataset containing turnover data.
        feat (pd.DataFrame): The features dataset containing geographical information.
    """
    merged_df = train.merge(feat, left_on='but_num_business_unit', right_on='but_num_business_unit')
    corr_matrix = merged_df[['turnover', 'but_latitude', 'but_longitude', 'but_region_idr_region', 'zod_idr_zone_dgr']].corr()

    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Correlation Matrix')
    plt.show()
