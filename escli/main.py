"""
Copyright 2019, Amazon Web Services Inc.
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
from __future__ import unicode_literals

import click
import sys

from .config import config_location
from .esconnection import ESConnection
from .utils import OutputSettings
from .essqlcli import ESSqlCli
from .formatter import Formatter

click.disable_unicode_literals_warning = True


@click.command()
@click.argument("endpoint", default="http://localhost:9200")
@click.option("-q", "--query", "query", type=click.STRING, help="Run single query in non-interactive mode")
@click.option("-e", "--explain", "explain", is_flag=True, help="Explain SQL to ES DSL")
@click.option(
    "--esclirc",
    default=config_location() + "config",
    envvar="ESCLIRC",
    help="Location of esclirc file.",
    type=click.Path(dir_okay=False),
)
@click.option(
    "-f",
    "--format",
    "result_format",
    type=click.STRING,
    default="jdbc",
    help="Specify format of output, jdbc/csv. By default, it's jdbc",
)
@click.option(
    "-v",
    "--vertical",
    "is_vertical",
    is_flag=True,
    default=False,
    help="Convert output from horizontal to vertical. Only used for non-interactive mode",
)
@click.option("-u", "--username", help="Username to connect to the Elasticsearch")
@click.option("-w", "--password", help="password corresponding to username")
@click.option(
    "-p",
    "--pager",
    "always_use_pager",
    is_flag=True,
    default=False,
    help="Always use pager to display output. If not specified, smart pager mode will be used according to the \
         length/width of output",
)
@click.option(
    "--aws",
    "use_aws_credentials",
    is_flag=True,
    default=False,
    help="Use AWS sigV4 to connect to AWS ELasticsearch domain",
)
def cli(endpoint, query, explain, esclirc, result_format, is_vertical, username, password, always_use_pager,
        use_aws_credentials):
    """
    Provide endpoint for Elasticsearch client.
    By default, it uses http://localhost:9200 to connect.
    """

    if username and password:
        http_auth = (username, password)
    else:
        http_auth = None

    # TODO add validation for endpoint to avoid the cost of connecting to some obviously invalid endpoint

    # handle single query without more interaction with user
    if query:
        es_executor = ESConnection(endpoint, http_auth, use_aws_credentials)
        es_executor.set_connection()
        if explain:
            output = es_executor.execute_query(query, explain=True, use_console=False)
        else:
            output = es_executor.execute_query(query, output_format=result_format, use_console=False)
            if output and result_format == "jdbc":
                settings = OutputSettings(table_format="psql", is_vertical=is_vertical)
                formatter = Formatter(settings)
                output = formatter.format_output(output)
                output = "\n".join(output)

        click.echo(output)
        sys.exit(0)

    # use console to interact with user
    escli = ESSqlCli(esclirc_file=esclirc, always_use_pager=always_use_pager, use_aws_credentials=use_aws_credentials)
    escli.connect(endpoint, http_auth)
    escli.run_cli()


if __name__ == "__main__":
    cli()
