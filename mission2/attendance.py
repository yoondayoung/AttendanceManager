import os

from mission2.player import Player


class AttendanceSystem(object):
    def __new__(cls):
        # singleton
        if not hasattr(cls, 'instance'):
            cls.instance = super(AttendanceSystem, cls).__new__(cls)
        cls.players_ = {}
        return cls.instance

    def add_new_player(self, name, day):
        player = Player(name, day)
        self.players_[name] = player

    def get_final_player_data(self):
        for p in self.players_.values():
            p.calculate_bonus_points()
            p.update_grade()

    def get_players_data(self):
        return self.players_

    def update_players_from_file(self, file):
        if not os.path.exists(file):
            raise FileNotFoundError()

        with open(file, encoding='utf-8') as f:
            for line in f.readlines():
                attendance = line.strip().split()
                if len(attendance) == 2:
                    player_name = attendance[0]
                    if player_name not in self.players_:
                        self.add_new_player(player_name, attendance[1])
                    else:
                        self.players_[player_name].update_data(attendance[1])

        self.get_final_player_data()

    def print_removed_players(self):
        print("\nRemoved player")
        print("==============")
        for p in self.players_.values():
            if p.is_removed():
                print(p.name)

    def print_attendance_system(self):
        for p in self.players_.values():
            p.print_data()

        self.print_removed_players()


if __name__ == "__main__":
    system = AttendanceSystem()
    system.update_players_from_file("attendance_weekday_500.txt")
    system.print_attendance_system()
