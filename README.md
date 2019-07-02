# Generate a CSV of datasets on the portal 
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/a6745596a7d94b17804cdd22340c9fd4)](https://app.codacy.com/app/TownofChapelHill/ods-datasets?utm_source=github.com&utm_medium=referral&utm_content=townofchapelhill/ods-datasets&utm_campaign=Badge_Grade_Dashboard)

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


NOTE: a quick retrieval of this data in CSV is available via: https://www.chapelhillopendata.org/api/v2/catalog/exports/csv
### Output 
CSV File for upload to the portal
### Dependencies
OpenDataSoft API v2
