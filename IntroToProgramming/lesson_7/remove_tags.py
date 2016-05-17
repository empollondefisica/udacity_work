# Question 4: Remove Tags

# When we add our words to the index, we don't really want to include
# html tags such as <body>, <head>, <table>, <a href="..."> and so on.

# Write a procedure, remove_tags, that takes as input a string and returns
# a list of words, in order, with the tags removed. Tags are defined to be
# strings surrounded by < >. Words are separated by whitespace or tags. 
# You may assume the input does not include any unclosed tags, that is,  
# there will be no '<' without a following '>'.

def remove_tags(text):
    collecting = True
    string = ''
    results = []
    
    for i in range(0, len(text)):
        if text[i] == '<':
            if collecting and string != '':
                results.append(string)
                string = ''
            collecting = False
        elif text[i] == '>':
            if not collecting:
                collecting = True
        elif text[i] == ' ':
            if collecting and string != '':
                results.append(string)
                string = ''
        elif collecting:
            string = string + text[i]
            if i == len(text) - 1:
                results.append(string)
        
    return results

print remove_tags('''<h1>Title</h1><p>This is a<a href="http://www.udacity.com">link</a>.<p>''')
#>>> ['Title','This','is','a','link','.']

print remove_tags('''<table cellpadding='3'><tr><td>Hello</td><td>World!</td></tr></table>''')
#>>> ['Hello','World!']

print remove_tags("<hello><goodbye>")
#>>> []

print remove_tags("This is plain text.")
#>>> ['This', 'is', 'plain', 'text.']

print remove_tags('This is in <i>italics</i>')
#>>> "['This', 'is', 'in', 'italics']"

print remove_tags('This sentence has no tags.')
#>>> "['This', 'sentence', 'has', 'no', 'tags.']"

print remove_tags('This <i>line</i> has <em>lots</em> of <b>tags</b>.')
#>>> "['This', 'line', 'has', 'lots', 'of', 'tags', '.']"
