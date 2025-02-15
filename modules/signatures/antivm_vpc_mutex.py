# Copyright (C) 2015 KillerInstinct
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


class VPCDetectMutex(Signature):
    name = "antivm_vpc_mutex"
    description = "Detects Virtual PC using a known mutex"
    severity = 3
    categories = ["anti-vm"]
    authors = ["KillerInstinct"]
    minimum = "1.2"
    mbc = ["B0009"]

    def run(self):
        indicators = ["MicrosoftVirtualPC7UserServiceMakeSureWe'reTheOnlyOneMutex"]

        for indicator in indicators:
            if self.check_mutex(pattern=indicator, regex=True):
                return True

        return False
