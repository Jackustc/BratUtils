# This file is part of BratUtils.
#
# BratUtils is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# BratUtils is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with BratUtils.  If not, see <http://www.gnu.org/licenses/>.
from bratutils import agreement as a


__author__ = 'Aleksandar Savkov'



dc = a.DocumentCollection('../res/samples/A/')
dc2 = a.DocumentCollection('../res/samples/B/')

dc.make_gold()
statistics = dc2.compare_to_gold(dc)

print statistics