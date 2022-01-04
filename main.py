import spellcheck

print ('what is your favorite sport?')

while True:
  typ = input('sport: ')
  opts = 'soccer basketball football softball baseball volleyball swimming tennis track'.split() 

  if typ in opts:
    print ("ok")
    break
    
    meant = spellcheck.comp_list(typ, opts, minsim=0.4)
    print('Did you mean:', ', '.join(meant))

