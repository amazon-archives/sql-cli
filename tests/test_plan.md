# Test Plan
 The purpose of this checklist is to guide you through the basic usage of ODFE SQL CLI, as well as a manual test process. 
 
## Display
 * [ ] Test pagination with different output length / width.
 * [ ] Test table formatted output.
 * [ ] Test successful conversion from horizontal to vertical display with confirmation.
 * [ ] Test warning message when output > 200 rows of data. (Limited by ODFE SQL syntax)


## Connection
* [ ] Test connection to a local Elasticsearch instance
  * [ ] Standard Elastic version, with/without authentication by [X-pack security](https://www.elastic.co/guide/en/elasticsearch/reference/7.6/security-getting-started.html)
  * [ ] OSS version, no authentication
  * [ ] OSS version, install [ODFE Security plugin](https://opendistro.github.io/for-elasticsearch-docs/docs/install/plugins/) to enable authentication and SSL
* [ ] Test connection to [AWS Elasticsearch domain](https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-gsg.html) (with ODFE SQL plugin installed by default)
* [ ] Test connection fail when connecting to invalid endpoint
* [ ] Test reconnection when connection lost during execution


## Execution
* [ ] Test successful execution given a query
* [ ] Test unsuccessful execution with an invalid SQL query
* [ ] Test load config file


## Nested commands with params
* [ ] Test dump query result to a file
* [ ] Test explain option `-e`
* [ ] Test query and format option `-q`, `-f`
* [ ] Test vertical option `-v`


## OS and Python compatibility
* [ ] Manually test on Linux(Ubuntu), Windows and mac-os.
* [ ] Test against python 3.X versions