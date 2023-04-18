class Triathlon:
    def __init__(self, first_name, last_name, location, swim_time, cycle_time, run_time):
        """
        Initializes a Triathlon object with athlete's information and competition times.

        Args:
            first_name (str): First name of the athlete.
            last_name (str): Last name of the athlete.
            location (str): Location of the competition.
            swim_time (float): Time taken for the swim discipline in minutes.
            cycle_time (float): Time taken for the cycle discipline in minutes.
            run_time (float): Time taken for the run discipline in minutes.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.swim_time = swim_time
        self.cycle_time = cycle_time
        self.run_time = run_time
        self.total_time = swim_time + cycle_time + run_time

    def print_details(self):
        """
        Prints the athlete's information and competition times in a single line.
        """
        print("Name: {} {}, Location: {}, Swim Time: {:.2f} mins, Cycle Time: {:.2f} mins, Run Time: {:.2f} mins, Total Time: {:.2f} mins".format(
            self.first_name, self.last_name, self.location, self.swim_time, self.cycle_time, self.run_time, self.total_time))


# Example usage:
athlete1 = Triathlon("John", "Doe", "London", 30.5, 60.25, 45.75)
athlete1.print_details()
# Output: Name: John Doe, Location: London, Swim Time: 30.50 mins, Cycle Time: 60.25 mins, Run Time: 45.75 mins, Total Time: 136.50 mins
