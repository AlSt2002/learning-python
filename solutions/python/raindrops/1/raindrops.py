def convert(number):
    if number % 3 != 0 and number %  5 != 0 and number % 7 != 0: 
        return str(number)
    raindrop = ''
    if number % 3 == 0:
        raindrop += 'Pling'
    if number % 5 == 0:
        raindrop += 'Plang'
    if number % 7 == 0:
        raindrop += 'Plong'
    return raindrop
