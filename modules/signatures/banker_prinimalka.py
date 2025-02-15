# Copyright (C) 2013 Claudio "nex" Guarnieri (@botherder)
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


class Prinimalka(Signature):
    name = "banker_prinimalka"
    description = "Detected Prinimalka banking trojan"
    severity = 3
    categories = ["banker"]
    families = ["Prinimalka"]
    authors = ["nex"]
    minimum = "1.0"
    evented = True

    filter_apinames = set(["RegSetValueExA", "RegSetValueExW"])

    def on_call(self, call, process):
        if self.get_argument(call, "ValueName").endswith("_opt_server1"):
            server = self.get_argument(call, "Buffer").rstrip("\\x00")
            self.description += " (C&C: {0})".format(server)
            return True
