# Copyright (C) 2013,2015 Claudio "nex" Guarnieri (@botherder), Optiv, Inc. (brad.spengler@optiv.com)
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


class AntiVMBios(Signature):
    name = "antivm_generic_bios"
    description = "Checks the version of Bios, possibly for anti-virtualization"
    severity = 3
    categories = ["anti-vm"]
    authors = ["nex", "Optiv"]
    minimum = "1.2"
    ttp = ["T1057", "T1012"]
    mbc = ["B0009.024", "B0009.005"]

    def run(self):
        if self.check_read_key(
            pattern=".*\\\\HARDWARE\\\\DESCRIPTION\\\\System\\\\(SystemBiosVersion|VideoBiosVersion)$", regex=True
        ):
            return True
        return False
