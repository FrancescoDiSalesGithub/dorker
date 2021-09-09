# dorker

## How to use

After cloning this project, you can do the following:

- search for a specific google dork giving a topic to search (such as password,login or any other word)
- execute a google dork 

### Search for a dork

Type in your terminal:

`python3 dorker.py search [topic]`

where topic is the term you want to search for a possible google dork.
Example:

`python3 dorker.py search mp3'

In output the program will give all the possible dorks that are similiar to the word you have given.

### Execute a dork

By executing a dork you have two possibilities:

* running a whole research
* running a research only for a specific number of results you want to see

In the first case, type:

`python3 dorker.py execute allintitle:'page'`

The program will run the research until you press CTRL+C or CTRL+Z.

In the second case:

`python3 dorker.py executelimit allintitle:'page'`

The output will be the following:
`how many values do you want to search? `

type a number and the program will give you the exact number of records you want to see


