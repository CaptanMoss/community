# Copyright (C) 2019 ditekshen
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from lib.cuckoo.common.abstracts import Signature


class DeletesSystemStateBackup(Signature):
    name = "deletes_system_state_backup"
    description = "Attempts to delete system state backup"
    severity = 3
    categories = ["ransomware"]
    authors = ["ditekshen"]
    minimum = "1.3"
    evented = True
    ttp = ["T1490"]

    def __init__(self, *args, **kwargs):
        Signature.__init__(self, *args, **kwargs)

    filter_apinames = set(["CreateProcessInternalW", "ShellExecuteExW"])

    def on_call(self, call, process):
        if call["api"] == "CreateProcessInternalW":
            cmdline = self.get_argument(call, "CommandLine").lower()
            if (
                "wbadmin" in cmdline
                and ("delete" in cmdline and "systemstatebackup" in cmdline)
                or ("delete" in cmdline and "catalog" in cmdline)
            ):
                return True
        elif call["api"] == "ShellExecuteExW":
            filepath = self.get_argument(call, "FilePath").lower()
            params = self.get_argument(call, "Parameters").lower()
            if (
                "wbadmin" in filepath
                and ("delete" in params and "systemstatebackup" in params)
                or ("delete" in params and "catalog" in params)
            ):
                return True
