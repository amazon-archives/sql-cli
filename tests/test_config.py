"""
Copyright 2020, Amazon Web Services Inc.
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
import os
import stat
import pytest

from odfesql_cli.config import ensure_dir_exists


class TestConfig:
    def test_ensure_file_parent(self, tmpdir):
        subdir = tmpdir.join("subdir")
        rcfile = subdir.join("rcfile")
        ensure_dir_exists(str(rcfile))

    def test_ensure_existing_dir(self, tmpdir):
        rcfile = str(tmpdir.mkdir("subdir").join("rcfile"))

        # should just not raise
        ensure_dir_exists(rcfile)

    def test_ensure_other_create_error(self, tmpdir):
        subdir = tmpdir.join("subdir")
        rcfile = subdir.join("rcfile")

        # trigger an oserror that isn't "directory already exists"
        os.chmod(str(tmpdir), stat.S_IREAD)

        with pytest.raises(OSError):
            ensure_dir_exists(str(rcfile))
