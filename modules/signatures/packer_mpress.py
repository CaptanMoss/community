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


class MPressPacked(Signature):
    name = "packer_mpress"
    description = "Executable file is packed/obfuscated with MPRESS"
    severity = 2
    categories = ["packer"]
    authors = ["ditekshen"]
    minimum = "1.3"
    ttp = ["T1045"]

    def run(self):
        for section in self.results.get("static", {}).get("pe", {}).get("sections", []):
            if section["name"].lower().startswith(".mpress"):
                self.data.append({"section": section})
                return True

        return False
