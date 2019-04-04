""" Opendatasoft API query """

import secrets
import filename_secrets

import csv
import json
import requests

# initialize local variables
json_messages={}
result_d={}
response=""
rec_count=0

# Set CSV Header & line format
csv_header = ['Name','Dataset Identifier','# of records','Records Size','Last Processed','Has content','Dataset Visible','Popularity','API Calls','Downloads','Publisher','License','Keywords','Theme']

# construct api parameters
ods_URI="https://www.chapelhillopendata.org/api/v2/catalog/datasets/"
querystring="?apikey=" + secrets.ODS_api + "&start=0&include_app_metas=True&rows=-1"
url=ods_URI + querystring
api_headers={'Content-Type': 'application/json','Accept': 'application/json'}

# Retrieve content from API
try:
   response = requests.get(url, headers=api_headers)
except Exception:
   raise Exception("API get request failed")

if response.status_code != 200:
   if response.status_code == 429:
        print("API Limit Exceeded: " + response.status)
   else:
        print("API Retrieval failed: " + str(response.status_code))
   exit(1)

# load content
result_set=json.loads(response.text)
# retrieved record count
num_records=result_set['total_count']
if num_records == 0:
   print("No content retrieved from API")
   exit(1)

# create output file & write header row
try:
   output_file = open(filename_secrets.ods_output_file, 'w')
   csvwriter = csv.writer(output_file, dialect='excel')
except IOError:
   print("Output file creation failed")
   exit(1)

csvwriter.writerow(csv_header)


# ETL processing result set
for i in range(0, num_records):
   # convert to a Dict for key lookup
   result_d=result_set['datasets'][i]
   # build the output values in key order
   csv_output=['null']*14
   csv_output[0] = result_d['dataset']['metas']['default']['title']
   csv_output[1] = result_d['dataset']['dataset_id']
   csv_output[2] = result_d['dataset']['metas']['default']['records_count']
   csv_output[3] = result_d['dataset']['metas']['processing']['records_size']
   csv_output[4] = result_d['dataset']['metas']['default']['data_processed']
   csv_output[5] = result_d['dataset']['has_records']
   csv_output[6] = result_d['dataset']['data_visible']
   csv_output[7] = result_d['dataset']['metas']['explore']['popularity_score']
   csv_output[8] = result_d['dataset']['metas']['explore']['api_call_count']
   csv_output[9] = result_d['dataset']['metas']['explore']['download_count']
   csv_output[10]= result_d['dataset']['metas']['default']['publisher']
   csv_output[11]= result_d['dataset']['metas']['default']['license']
   if result_d['dataset']['metas']['default']['keyword'] is not None:
      csv_output[12] = ", ".join(result_d['dataset']['metas']['default']['keyword'])
   if result_d['dataset']['metas']['default']['theme'] is not None:
      csv_output[13] = ", ".join(result_d['dataset']['metas']['default']['theme'])
   csvwriter.writerow(csv_output)
   rec_count += 1

# cleanup and exit
output_file.close()
