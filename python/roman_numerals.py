def to_roman(num):
    roman_num = ""
    key_dict = {
      "M": 1000,
      "CM": 900,
      "D": 500,
      "CD": 400,
      "C": 100,
      "XC": 90,
      "L": 50,
      "XL": 40,
      "X": 10,
      "IX": 9,
      "V": 5,
      "IV": 4,
      "I": 1,  
    }
    for x in key_dict:
        while num >= key_dict[x]:
            roman_num += x
            num -= key_dict[x]
    return roman_num


    # write your code here!