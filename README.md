# Generate a CSV of datasets on the portal 

## Automate the ods-datasets-monitoring report

### Goal 
Create a script that will retrieve a list of datasets with the following parameters
#### 'Dataset Identifier'
#### '# of records'
#### 'Records Size'
#### 'Last Processed'
#### 'Has content'
#### 'Dataset Visible'
#### 'Popularity'
#### 'API Calls'
#### 'Downloads'
#### 'Keywords'
#### 'Theme'
### Purpose 
Create a dataset KPI spreadsheet for the open data portal content
### Methodology 
[Use the OpenDataSoft API](https://help.opendatasoft.com/apis/ods-search-v2/#search-api-v2)
### Data Source
[Catalog records](https://help.opendatasoft.com/apis/ods-search-v2/#catalog)

### Output 
CSV File for upload to the portal
### Dependencies
Requires the 're' python module

