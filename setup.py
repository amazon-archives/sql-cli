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
import re
import ast

from setuptools import setup, find_packages

install_requirements = [
    "click == 7.1.1",
    "prompt_toolkit == 3.0.5",
    "Pygments == 2.6.1",
    "cli_helpers[styles] == 1.2.1",
    "elasticsearch == 7.5.1",
    "pyfiglet == 0.8.post1",
    "boto3 == 1.9.181",
    "requests-aws4auth == 0.9",
]

_version_re = re.compile(r"__version__\s+=\s+(.*)")

with open("odfesql_cli/__init__.py", "rb") as f:
    version = str(
        ast.literal_eval(_version_re.search(f.read().decode("utf-8")).group(1))
    )

description = "CLI for Elasticsearch Open Distro SQL with auto-completion and syntax highlighting."

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="odfesql",
    author="Zhongnan",
    author_email="zhongnan.su@outlook.com",
    version=version,
    license="Apache 2.0",
    url="https://opendistro.github.io/for-elasticsearch-docs/",
    packages=find_packages(),
    package_data={"odfesql_cli": ["conf/clirc", "esliterals/esliterals.json"]},
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=install_requirements,
    entry_points={"console_scripts": ["odfesql=odfesql_cli.main:cli"]},
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: Unix",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: SQL",
        "Topic :: Database",
        "Topic :: Database :: Front-Ends",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires='>=3.0'
)
