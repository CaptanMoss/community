# Copyright (C) 2016 Brad Spengler
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


class HyperVDetectKeys(Signature):
    name = "antivm_hyperv_keys"
    description = "Detects Hyper-V through the presence of a registry key"
    severity = 3
    categories = ["anti-vm"]
    authors = ["Brad Spengler"]
    minimum = "0.5"
    ttp = ["T1057", "T1012"]
    mbc = ["B0009"]

    def run(self):
        indicators = [
            ".*\\\\SYSTEM\\\\(CurrentControlSet|ControlSet001)\\\\Enum\\\\ACPI\\\\Hyper_V_Gen_Counter_V1$",
        ]

        for indicator in indicators:
            if self.check_key(pattern=indicator, regex=True):
                return True

        return False
