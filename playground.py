import datetime

def parse_expenses(expense_string):
    """Parse the list of expenses and return the list of triples (date, value, currency).
    Ignore lines starting with #.
    Parse the date using datetime.
    Example expenses string:
        2016-01-02 -34.01 USD
        2016-01-03 2.59 DKK
        2016-01-03 -2.72 EUR
        """    
    expenses = []
    for line in expense_string.splitlines():
        if line.startswith('#'):
            continue
        date, value, currency = line.split()
        date = datetime.datetime.strptime(date, '%Y-%m-%d')
        value = float(value)
        expenses.append((date, value, currency))
    return expenses

def over_sixty(date):
    """if else statement to check if value is more than 60 days old. If it is, return True, else return False""" 
    if date < datetime.datetime.now() - datetime.timedelta(days=60):
        return True
    else:
        return False




"""if else statement to check if value is more than 60 days old. If it is, return True, else return False"""



"""Create a new datapoint which will indicate whether a candidate has updated their data 
in the last 60 days or not. This will be used to filter out candidates who have not updated
their data in the last 60 days. 
"""

"""Create a new COLUMN in the table called 'OwnDate' which will
indicate whether a candidate has updated their data in the last 60 days or not. 
"""

def add_updated_cv_from_sixty_days(NC_AssociateInbox_table:str):

	query_updated_cv = f”””select OwnDate from {TARGET_SCHEMA}.{NC_AssociateInbox_table}"""

	df = spark.sql(query_updated_cv)
	df = df.withColumn(“UpdateData”), when(df.”UpdateData”.isNull(), “No").otherwise(“Yes”)) # datediff(df.”UpdateData”, current_timestamp()) > 60)
	
	df_add_regulated
 
 # when(date_diff(df.”UpdateData”, current_timestamp()) > 60, “No”).otherwise(“Yes”))
 # don't forget to import date_diff from pyspark.sql.functions
 