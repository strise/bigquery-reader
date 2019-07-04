from google.cloud import bigquery
client = bigquery.Client()

query = (
  "SELECT * "
  "FROM `bank_trends.bank_trends` "
  "ORDER BY date desc "
)

# Start the query
query_job = client.query(
  query,
  location="EU",
)

# Fetch the results
for row in query_job:
  # Row values can be accessed by field name or index
  # See docs for more info: https://googleapis.github.io/google-cloud-python/latest/bigquery/index.html
  print(row)