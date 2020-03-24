# Open Distro Elasticsearch SQL CLI

ODFE: Open Distro for Elasticsearch 

ODFE SQL CLI is a stand alone Python application and can be launched by a wake word `odfesql`. It serves as a support only for 
[Open Distro SQL plugin for Elasticsearch](https://opendistro.github.io/for-elasticsearch-docs/docs/sql/). You can run 
it on any OS we support, and connect to any valid remote endpoint without installing Elasticsearch.


## Installation
- `pip install odfesql` 
- odfe sql cli is compatible with Python 3, because Python 2 is no longer maintained since 01/01/2020 https://pythonclock.org/ 


## Configuration
- A config file is automatically created at `~/.config/escli/config` at first launch. 
See the file itself for a description of all available options.


## Features
- Multiline input
- Auto-completion with index suggestion
- Formatted output
    - Tabular format
    - Fields name with color
    - Enable horizontal display (by default) and vertical display when output is too wide
    - Pagination for long output
- Syntax highlighting
- Connect to Elasticsearch node/cluster with/without security on either **ES localhost, Open Distro ES, or AWS Elasticsearch Domain**.
Refer to [test plan](./tests/test_plan.md) on how to connect to different instance with/without security
- Load Config file
- Run single query from Command Line with parameters
    - *endpoint:* no need to specify a parameter, anything follow by wake word `odfesql` should be the endpoint. 
    By default, it’s http://localhost:9200
    - *--help:* help page for options and params
    - *-q:* follow by a single query user wants to run.
    - *-f:* support *jdbc/raw* format output
    - *-v:* display data vertically
    - *-u:* username to connect to Elasticsearch 
    - *-w:* password for username
    - *-e:* translate sql to DSL

- Run the CLI with parameters
    - *-p*: always use pager to display output
    - *--esclirc*: provide path of config file to load.



## Basic Usage
- The CLI supports all types of query that ODFE SQL supports. See [ODFE SQL basic usage](https://github.com/opendistro-for-elasticsearch/sql#basic-usage)
- ![](./screenshots/usage.gif)



## Code of Conduct

This project has adopted an [Open Source Code of Conduct](https://opendistro.github.io/for-elasticsearch/codeofconduct.html).


## Security issue notifications

If you discover a potential security issue in this project we ask that you notify AWS/Amazon Security 
via our [vulnerability reporting page](http://aws.amazon.com/security/vulnerability-reporting/). 
Please do **not** create a public GitHub issue.


## Licensing

See the [LICENSE](./LICENSE.TXT) file for our project's licensing. We will ask you to confirm the licensing of your contribution.


## Copyright

Copyright 2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
