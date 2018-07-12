# TextAnalysisTool

App used to analyze different types of data source and return statistics like occurence, meaning and category.
The different sources of data include:
- Files
- Sentence
- Essays

## How to use?

- First install the required dependencies:<br/> 
``` python -r requirements.text```<br/>
- Run the app using the following commanf:<br/>
``` python analyze.py <args> ``` <br/>
- Arguments above could be one of the following:<br/>
    1. -f files: Analyzes files separated by space
    2. -s sentence: Analyze a free form sentence
    3. -e: Analyze an essay from the menu

## More details:

Write a command-line text analysis tool that supports the following commands:
1.	Pre-analysis
        1.	analyze "sentence"<br/>
            The user types in a freeform sentence.
        2.  analyze "essay"<br/>
            The user selects a preexisting essay from a list.
2.	Post-analysis
        1.  define "word"

Analysis should output statistics about the analyzed text and create an in-memory cache of words and their meanings. After analysis is complete, the user should have the ability to query a word’s meaning from the cache.
References
Use this for reference word lists, including length categorization: https://github.com/first20hours/google-10000-english
Use this for meanings: http://www.mso.anu.edu.au/~ralph/OPTED/
Use essays from here: https://github.com/xaviervia/essays
Note: you can download the above resources and add them to your project.<br/>

### Analysis Output

Using the word lists from the References section, generate the following statistics:
-   List and count words in short-length category.
-	List and count words in medium-length category.
-	List and count words in long-length category.
-	List and count words that were not found in any of the lists.<br/>

#### Bonus Functionality

-	Parallelise essay analysis up to a factor of 4.
-	Create a single word cache across all four documents.
-	Create a cross-essay analysis.
       -	List and count common words.
       -    List and count exclusive words, grouped by essay.
