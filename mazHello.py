#! /usr/bin/python

import sys

def main():
  pi=3.14
  #print a
  #print a[1]
  #print len(a)
  #working with string
  string='The original value of pi is  '
  print string.upper()+ str(pi)
  print string.replace('o','oo')+ str(pi)
  print string.strip()+str(pi)
  #string slicing
  print string[0:-3]
  #print_f type string value
  name='Maz'
  text = ("%s is a good boy and %s did %d bad things! %s wish him best of luck! I owe him %f USD" %
   (name, 'he', 3 , 'We', 4.3))
  print text
  unicodeString = u'A unicode \u018e string \xf1'
  print unicodeString

  #speed = sys.argv[1]
  #mood = sys.argv[2]
  speed=40
  #print mood
  if speed >= 80:
    print 'License and registration please'
  else:
    print "Let's try to keep it under 80 ok?"
  
  #iterating through a list
  aShortList=[34,34,34,78,56,78,90]
  total=0
  for num in aShortList:
    total+=num
  print total

  #determining a value whether it is in the list or not
  anArrayOfList=['Maz','Anu','Asha','Nirmol']
  if 'Anu' in anArrayOfList:
    print 'My Dear Love is here!'
  #print through using while loop
  #for i in range(100):
    #print i

  #python sorting
  strs=['aa', 'bb', 'CC', 'FGH', 'CDF', 'ERT', 'zz', 'Xx']
  #print sorted(strs)
  #print sorted(strs, reverse=True)
  #print sorted(strs, key=len)
  #print sorted(strs, key=str.lower)

  #list comprehension
  nums = [1,1,1,3,4,5,6,8,89,87,67]
  num1 = [n*n for n in nums if n>=5]
  print num1

  fruits = ['Apple', 'BanaNa', 'grapes', 'Orange', 'JackFRUIT']
  fruits1 = [s.lower() for s in fruits if 'O' in s] #case sensitive
  print fruits1

  #tuples
  names=("Maz",)
  print name
  #determinig if something in the list  
if __name__ == '__main__':
  main()
