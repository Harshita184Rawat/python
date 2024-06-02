# Question 1: 
# Write a java function which takes a document and a set of search terms. The function should
# return the shortest contiguous sequence of words from the document containing ALL of the given search
# terms in any order (ignoring case), or null, if no such string exists.
# The document can contain only alphanumeric characters and spaces.
# Example:
# terms = ["the", "to"]
# output: "to seek the"

document = "Far over the misty mountains cold To dungeons deep and caverns old " + "We must away ere break of day To seek the pale enchanted gold"

docWords = document.split()
n=len(docWords)
i=0
j=0
result = ''
shortestR = ''

for i in range(0,n):
    if docWords[i] == 'to' or 'the':
        result = result + ' ' + docWords[i]
        continue
        result = result + ' ' + docWords[i]
        if 'to' and 'the' in result:
            break;
        
        if len(result)> len(shortestR):
           shortestR = result
           result=''
        
    
    
    
      
print(shortestR)
    
        
        
        
        
        
        
        
        
    

