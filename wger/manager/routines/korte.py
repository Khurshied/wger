# This file is part of wger Workout Manager.
#
# wger Workout Manager is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# wger Workout Manager is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License

import logging
import os

from django.utils.translation import ugettext as _

from wger.utils.routines import Routine
from wger.utils.routines import ExerciseConfig

logger = logging.getLogger('wger.custom')

MAX_SQUAT = 100
MAX_BENCH = 110
MAX_DEADLIFT = 120


class SquatConfig(ExerciseConfig):

    data = {
        1: {1: [1, 2, 3, 4, 5],
            2: [1, 2, 3, 4, 5],
            3: [1, 2, 3, 4, 5]},
        2: {1: [1, 2, 3, 4, 5],
            2: [1, 2, 3, 4, 5],
            3: [1, 2, 3, 4, 5]},
        3: {1: [1, 2, 3, 4, 5],
            2: [1, 2, 3, 4, 5],
            3: [1, 2, 3, 4, 5]},
        4: {1: [1, 2, 3, 4, 5],
            2: [1, 2, 3, 4, 5],
            3: [1, 2, 3, 4, 5]},
        5: {1: [1, 2, 3],
            2: [1, 2, 3],
            3: [1]},
        6: {1: [1, 2, 3],
            2: [1, 2, 3],
            3: [1]},
        7: {1: [1, 2, 3],
            2: [1, 2, 3],
            3: [1]},
        8: {1: [1, 2, 3],
            2: [1, 2, 3],
            3: [1]},
    }

    def get_routine(self):
        if self.current_week == 1:
            return 5, (MAX_SQUAT + 11) * 0.58
        elif self.current_week == 2:
            return 5, (MAX_SQUAT + 11) * 0.6
        elif self.current_week == 3:
            return 5, (MAX_SQUAT + 11) * 0.62
        elif self.current_week == 4:
            return 5, (MAX_SQUAT + 11) * 0.64
        elif self.current_week == 5:
            if self.current_day != 3:
                return 3, (MAX_SQUAT + 11) * 0.6
            else:
                return 1, (MAX_SQUAT + 11) * 0.80
        elif self.current_week == 6:
            if self.current_day != 3:
                return 3, (MAX_SQUAT + 11) * 0.6
            else:
                return 1, (MAX_SQUAT + 11) * 0.85
        elif self.current_week == 7:
            if self.current_day != 3:
                return 3, (MAX_SQUAT + 11) * 0.6
            else:
                return 1, (MAX_SQUAT + 11) * 0.90
        elif self.current_week == 8:
            if self.current_day != 3:
                return 3, (MAX_SQUAT + 11) * 0.6
            else:
                return 1, (MAX_SQUAT + 11) * 0.95


class BenchConfig(ExerciseConfig):
    data = {
        1: {1: [6, 7, 8, 9, 10],
            2: [6, 7, 8, 9, 10],
            3: [6, 7, 8, 9, 10]},
        2: {1: [6, 7, 8, 9, 10],
            2: [6, 7, 8, 9, 10],
            3: [6, 7, 8, 9, 10]},
        3: {1: [6, 7, 8, 9, 10],
            2: [6, 7, 8, 9, 10],
            3: [6, 7, 8, 9, 10]},
        4: {1: [6, 7, 8, 9, 10],
            2: [6, 7, 8, 9, 10],
            3: [6, 7, 8, 9, 10]},
        5: {1: [4, 5, 6, 7, 8],
            2: [4],
            3: [2, 3, 4, 5, 6]},
        6: {1: [4, 5, 6, 7, 8],
            2: [4],
            3: [2, 3, 4, 5, 6]},
        7: {1: [4, 5, 6, 7, 8],
            2: [4],
            3: [2, 3, 4, 5, 6]},
        8: {1: [4, 5, 6, 7, 8],
            2: [4],
            3: [2, 3, 4, 5, 6]},
    }

    def get_routine(self):
        if self.current_week == 1:
            return 5, (MAX_BENCH + 4) * 0.58
        elif self.current_week == 2:
            return 5, (MAX_BENCH + 4) * 0.6
        elif self.current_week == 3:
            return 5, (MAX_BENCH + 4) * 0.62
        elif self.current_week == 4:
            return 5, (MAX_BENCH + 4) * 0.64
        elif self.current_week == 5:
            if self.current_day != 2:
                return 4, (MAX_BENCH + 4) * 0.6
            else:
                return 1, (MAX_BENCH + 4) * 0.80
        elif self.current_week == 6:
            if self.current_day == 2:
                return 1, (MAX_BENCH + 4) * 0.85
            else:
                return 4, (MAX_BENCH + 4) * 0.6
        elif self.current_week == 7:
            if self.current_day == 2:
                return 1, (MAX_BENCH + 4) * 0.90
            else:
                return 4, (MAX_BENCH + 4) * 0.6
        elif self.current_week == 8:
            if self.current_day == 2:
                return 1, (MAX_BENCH + 4) * 0.95
            else:
                return 4, (MAX_BENCH + 4) * 0.6


class DeadliftConfig(ExerciseConfig):
    data = {
        1: {1: [11, 12, 13, 14, 15],
            2: [11, 12, 13, 14, 15],
            3: [11, 12, 13, 14, 15]},
        2: {1: [11, 12, 13, 14, 15],
            2: [11, 12, 13, 14, 15],
            3: [11, 12, 13, 14, 15]},
        3: {1: [11, 12, 13, 14, 15],
            2: [11, 12, 13, 14, 15],
            3: [11, 12, 13, 14, 15]},
        4: {1: [11, 12, 13, 14, 15],
            2: [11, 12, 13, 14, 15],
            3: [11, 12, 13, 14, 15]},
        5: {1: [9],
            2: [5, 6, 7],
            3: [7, 8, 9]},
        6: {1: [9],
            2: [5, 6, 7],
            3: [7, 8, 9]},
        7: {1: [9],
            2: [5, 6, 7],
            3: [7, 8, 9]},
        8: {1: [9],
            2: [5, 6, 7],
            3: [7, 8, 9]},
    }

    def get_routine(self):
        if self.current_week == 1:
            return 5, (MAX_DEADLIFT + 6) * 0.58
        elif self.current_week == 2:
            return 5, (MAX_DEADLIFT + 6) * 0.6
        elif self.current_week == 3:
            return 5, (MAX_DEADLIFT + 6) * 0.62
        elif self.current_week == 4:
            return 5, (MAX_DEADLIFT + 6) * 0.64
        elif self.current_week == 5:
            if self.current_day == 1:
                return 1, (MAX_DEADLIFT + 6) * 0.80
            else:
                return 3, (MAX_DEADLIFT + 6) * 0.60
        elif self.current_week == 6:
            if self.current_day == 1:
                return 1, (MAX_DEADLIFT + 6) * 0.85
            else:
                return 3, (MAX_DEADLIFT + 6) * 0.60
        elif self.current_week == 7:
            if self.current_day == 1:
                return 1, (MAX_DEADLIFT + 6) * 0.90
            else:
                return 3, (MAX_DEADLIFT + 6) * 0.60
        elif self.current_week == 8:
            if self.current_day == 1:
                return 1, (MAX_DEADLIFT + 6) * 0.95
            else:
                return 3, (MAX_DEADLIFT + 6) * 0.60

korte = Routine(weeks=8,
                name='Korte 3x3',
                short_name=os.path.basename(__file__).replace('.py', ''),
                description=_("Pure German volume training (GVT). You will squat, "
                              "bench, and deadlift. That's it. Good luck."))

e1 = SquatConfig('Squats', None)
e2 = BenchConfig('Bench', None)
e3 = DeadliftConfig('Deadlift', None)

korte.add(e1)
korte.add(e2)
korte.add(e3)