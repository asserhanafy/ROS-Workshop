import random

class RPS:
  def random_num():
    num = random.randint(1, 3)
    return num
  # Rock: 1
  # Paper: 2
  # Scissors: 3

  def win(num1, num2):
    if num1 == 1 and num2 == 2:
      return -1
    if num1 == 2 and num2 == 1:
      return 1
    if num1 == 1 and num2 == 3:
      return 1
    if num1 == 3 and num2 == 1:
      return -1
    if num1 == 2 and num2 == 3:
      return -1
    if num1 == 3 and num2 == 2:
      return 1
    if num1 == num2:
      return 0

class player:
  def __init__(self, name):
    self.name = name
    self.score = 0
    self.RPS_num = 0

class game_system:
  def get_name(num):
    if num == 1:
      return "Rock"
    if num == 2:
      return "Paper"
    if num == 3:
      return "Scissors"
    
  def add_score(num, P1, P2):
    if num == 1:
      P1.score += 1
    if num == -1:
      P2.score += 1