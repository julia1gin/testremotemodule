def guess_number(number, nach, con):
  '''
  This function guesses the number and prints the guesses.

  Parameters:
  number (int): the number to guess
  nach (int): the number of guesses
  con (bool): the condition to break the loop
  '''
  
  attempts = 0
  guessed = 0
  
  while nach != con:
    m = (nach + con) // 2
    attempts += 1
    if m < number:
      nach = m + 1
    else:
      con = m
  
  guessed = nach
  print(f"Вы загадали число {guessed} и оно было отгадано за {attempts} попыток")
