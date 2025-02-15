# Copyright (C) 2020 bartblaze
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


class QihooDetectLibs(Signature):
    name = "antiav_360_libs"
    description = "Detects Qihoo 360 Antivirus through the presence of a library"
    severity = 3
    categories = ["anti-av"]
    authors = ["bartblaze"]
    minimum = "1.2"
    evented = True
    ttp = ["T1063"]

    filter_apinames = set(["LdrLoadDll", "LdrGetDllHandle"])

    def on_call(self, call, process):
        dllname = self.get_argument(call, "FileName")
        if (
            "360net" in dllname.lower()
            or "360safemonpro" in dllname.lower()
            or "360base" in dllname.lower()
            or "360base64" in dllname.lower()
        ):
            return True
