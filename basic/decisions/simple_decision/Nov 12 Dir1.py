def directions():
  directions = ["Move forward", "Move Backward", "Turn Left", "Turn Right"]
  return directions

def run():
  print(directions())

run()


def(movements):
  path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1 ]
  return path

def run():
  print("Moving...")
  path = movements
  print(f"{path[0]} for {path[1]} steps")
  print(f"{path[2]} for {path[3]} steps")
  print(f"{path[4]} for {path[5]} steps")
  print("{} for {} steps".format(path[6],path[7]))
run()