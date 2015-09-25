__author__ = 'FeiHou'

'''This program contains:
1.Print each line of the ged file;
2.Print each level number of each items;
3.Detect tags of each line: if it's vaild,print the tag,or print invaild tag;
'''
try:                                              #catch errors when the file cannot be opened
	fopen=open('FamilyTree-FeiHou.ged')
except:
	print "File cannot be opened"
	exit()

for line in fopen:                                #use a loop to operate each line
	line=line.rstrip()                            #delete the '\n' of each line
	words=line.split()                            #split the words of each line
	print "This Line:\n"+line
	print "Level Number:\n"+words[0]
	word=words[1]
	if word in ['NAME','SEX','BIRT','DEAT','FAMC','FAMS','FAM','MARR','HUSB','WIFE','CHIL','DIV','DATE','HEAD','TRLR','NOTE','_MARNM']:    #detect whether the word is in the array provided by the ged data file
		print "Tag:" + word + "\n"
	elif word[0]=="@":
		print "Tag:" + word + "\n"                 #handle with the ID cause each ID of every person may change
	else:
		print "Tag:Invalid Tag" + "\n"