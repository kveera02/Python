'''
rec11

for Part THREE
    you will rewrite startUpFillWordList( ) to allow
	a user to choose the name of the file to be read
	from initially.
	you will also complete getValidStartupFilename()
	to be used in your rewrite which takes only the two
	allowed extensions: .clrs and .cpssv    
'''
import random

STARTUP_FILE_NAME = "C:\Users\Kev\Desktop\wordsWordsWords.txt"

def startUpFillWordList( wordList ):
    ''' opens wordsWordsWords.txt and fills list with words from that file
        the words in that file are one per line
    '''
    wrdfl = open(STARTUP_FILE_NAME , 'r')
    for i in wrdfl:
       
        wordList.append(i)
    print "LIST WOULD BE FILLED WITH WORDS FROM FILE"

def saveWords( wordList ):
    ''' Store current word list into the file: wordsWordsWords.txt
	    This will destroy the previous version of the file without
		making a backup.
    '''
    wdfl = open (STARTUP_FILE_NAME , 'w')
    for i in wordList:
        wdfl.write(i)
    wdfl.flush()
    wdfl.close()
    print "WORDS WOULD BE SAVED HERE"

def makeHTMLfile( wordList ):
    ''' makes file: _________.html using words in wordList '''
    fileName = getFlNm()
    fl = open(fileName , 'w')
    title = getTitle()
    heading , size = getHeading(title)
    fl.write('<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n<html xmlns="http://www.w3.org/1999/xhtml">\n')
    fl.write(heading)
    fl.write('<br />\n')
    for i in wordList:
        color = getColor()
        begin , end = getFormat()
        fl.write('<font color=' + '"' + str(color) + '"' + '>' + begin + str(i) + end + '</font><br />\n')
    fl.write('</body>\n</html>')        
    
    print "HTML FILE WOULD BE CREATED HERE"
    
def getTitle():
    ttl = raw_input('Enter the title you would like to use for the html file: ')
    return ttl

def getFlNm():
    fileName = raw_input('Please enter a valid startup file name(Must be an .html extension): ')
    if '.htm' not in fileName:
        x = fileName + '.html'
        return x
    elif '.htm ' in fileName:
        x = fileName + 'l'
        return x
    else:
        return fileName
    
def getHeading(var):
    head = raw_input('Enter the heading you would like to use for the html file: ')
    flhead = '<head>\n' + '<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />\n' + '<title>' + var + '</title>\n</head>\n<body>\n<h1>' + head + '</h1>\n'
    size = int(raw_input('Enter the font size (positive integer) for the heading : '))
    return flhead , size

def getColor():
    clrFl = open('C:\Users\Kev\Desktop\colors.txt' , 'r')
    lst = []
    for i in clrFl:
        lst.append(i)
    num = random.randint(0 , 262)
    color = lst[num]
    return color

def getFormat():
    x = [['<B><U><I>' , '</I></U></B>'] , ['<B>' , '</B>'] , ['<U>', '</U>']]
    num = random.randint(0 , len(x)-1)
    y = x[num]
    begin = y[0]
    end = y[1]
    return begin , end
    
    
    
def getValidStartupFilename( ):
    ''' returns the user's choice of filename
	    filename must .clrs, .csv or .unx extension
    '''
    ext1 = '.clrs'
    ext2 = '.csv'
    ext3 = '.unx'
    fileName = raw_input('Please enter a valid startup file(Must be a .clrs, .csv, or .unx extension): ')
    while ext1 or ext2 or ext3 not in fileName:
        fileName = raw_input('Not a valid filename.\nPlease enter a valid startup file(Must be a .clrs, .csv, or .unx extension): ')
    print "WOULD GET VALID STARTUP FILENAME HERE"
    return fileName

def getOneWord( prompt ):
    ''' prompts user with passed in prompt then enforces 
	    that the user types only 
		one word on the line
	    and returns that one word
    '''
    word = raw_input( prompt )
    while len( word.split() ) != 1:
        word = raw_input( "Just one word! Try again: " )
    return word

def addWord( wordList ):
    ''' adds user's input word to wordList '''
    word = getOneWord( "Enter word to add: " )
    if word not in wordList:
        wordList.append( word.strip() )
    else:
        print "%s rejected - already in list" % word

def removeWord( wordList ):
    ''' removes user's choice of word from list if it is there '''
    if not wordList:
        print "currently no words, can't remove"
        return
    wordToChunk = getOneWord( "Which word to remove? " )
    try:
        wordList.remove( wordToChunk )
    except ValueError:
        print wordToChunk + " is not in current list of words"
    except:
        print "Serious error has occured. Program is bailing out!"
        exit( -1 )

       
def showWords( wordList ):
    ''' display each word in current set, one per line '''
    if not wordList:
        print "currently no words"
        return
    print "Your words are:"
    for word in wordList:
        print word

MENU_CHOICE_VALUE_POSTITION = 0
MENU_CHOICE_TEXT_POSTITION = 1
SHOW_CUR_WORDS = ( 1, "1. Display current words" )
ADD_WORD       = ( 2, "2. Add word to current list (will not allow duplicates)" )
REMOVE_WORD    = ( 3, "3. Remove word form current list" )
MAKE_HTML_FILE = ( 4, "4. Print an HTML version of words in current list (under construction)" )
SAVE_AND_EXIT  = ( 5, "5. Save current list and exit" )
MENU = ( SHOW_CUR_WORDS, ADD_WORD, REMOVE_WORD, MAKE_HTML_FILE, SAVE_AND_EXIT )
VALID_MENU_VALUE_CHOICES = ( SHOW_CUR_WORDS[ MENU_CHOICE_VALUE_POSTITION ], \
                             ADD_WORD[ MENU_CHOICE_VALUE_POSTITION ], \
                             REMOVE_WORD[ MENU_CHOICE_VALUE_POSTITION ], \
                             MAKE_HTML_FILE[ MENU_CHOICE_VALUE_POSTITION ], \
                             SAVE_AND_EXIT[ MENU_CHOICE_VALUE_POSTITION ] )
QUIT_CHOICE = SAVE_AND_EXIT[ MENU_CHOICE_VALUE_POSTITION ] - 1
         
def displayMenu():
    ''' prints menu on screen '''
    print "\n\nrec11 MENU\nPlease choose from the following:\n"
    for menuLine in MENU:
        print menuLine[ MENU_CHOICE_TEXT_POSTITION ]

def getValidMenuChoice():
    ''' returns a valid menu choice '''
    displayMenu()
    choice = raw_input( "Enter menu choice (just the number, please): " )
    while not choice.isdigit() \
          or \
          int(choice) not in VALID_MENU_VALUE_CHOICES:
        print "Not a valid menu choice."
        displayMenu()
        choice = raw_input( "Enter menu (just the number, please): " )
    return int( choice ) - 1

def handleMenuChoice( choice, wordList ):
    ''' calls function to handle a valid menu choice
        assumes ch is valid
    '''
    print

    if   MENU[ choice ] == ADD_WORD:
        addWord( wordList )
        
    elif MENU[ choice ] == REMOVE_WORD:
        removeWord( wordList )
        
    elif MENU[ choice ] == MAKE_HTML_FILE:
        makeHTMLfile( wordList )
        
    elif MENU[ choice ] == SHOW_CUR_WORDS:
        showWords( wordList )
        
    elif MENU[ choice ] == SAVE_AND_EXIT:
        saveWords( wordList )
        print "Your words are saved in file " + STARTUP_FILE_NAME
        print "Thanks for using this program"
        
    else: # SERIOUS PROBLEM
        print "program is exiting due to menu error"
        exit( 1 )

def getAndHandleMenuChoice( wordList ):
    ''' processes wordList based on menu choice '''
    mChoice = getValidMenuChoice()
    handleMenuChoice( mChoice, wordList )
    return mChoice    
    
def main():

    print
    print

    wordList = [ ]
    startUpFillWordList( wordList )

    menuChoice = getAndHandleMenuChoice( wordList )
    while menuChoice != QUIT_CHOICE:
        menuChoice = getAndHandleMenuChoice( wordList )

    print
    print

# are we being executed?
if __name__ == '__main__':
    main()

