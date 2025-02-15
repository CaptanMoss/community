# Copyright (C) 2012 @threatlead
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


class BeebusMutexes(Signature):
    name = "rat_beebus_mutexes"
    description = "Creates known Beebus mutexes"
    severity = 3
    categories = ["rat"]
    families = ["Beebus"]
    authors = ["threatlead", "nex"]
    minimum = "0.5"
    references = [
        "http://www.fireeye.com/blog/technical/malware-research/2013/04/the-mutter-backdoor-operation-beebus-with-new-targets.html",
        "https://malwr.com/analysis/MjhmNmJhZjdjOWM4NDExZDkzOWMyMDQ2YzUzN2QwZDI/",
    ]

    def run(self):
        indicators = [
            ".*mqe45tex13fw14op0",
            ".*654234576804d",
        ]

        for indicator in indicators:
            if self.check_mutex(pattern=indicator, regex=True):
                return True

        return False
