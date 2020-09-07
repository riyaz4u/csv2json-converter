Hello,
The challenge was to consume and transform the CSV file in to a nested JSON file which will form a tree structure.

### Prerequisites
I have used Pycharm IDE for the same application to convert csv into json file for its application.

## The desired form

From the CSV, you will see that the data follows a parent child structure. The first entry is always at the top of the tree, with the following entries being children of the previous column. The example below shows the structure that we would like to see.

## Tasks
The task is to convert the provided CSV into JSON (see the example for the structure desired). Examples of the structure we apply for JSON to generate these menus can be found on the main groceries pages on groceries.morrisons.com (hover over shop groceries and have a look through the different categories). The menus on these category pages follow a specific structure with nested child pages to allow customers to browse different categories of groceries.

These menus can vary drastically in size and nesting, therefore you should remain aware of that when writing your solution and think about more columns and rows being in other CSV files that may be processed by your solution.

Create a simple application that can run locally on a unix environment using Python 3.6 or upwards. There should be a few unit tests testing the main logic of your program.

## Deliverables

I have attached csv2jsonconverter.py file ,csv file and generating json file along with this README.md file. 

## Instructions for execution
> Open csv2jsonconverter.py file with pycharm/any other IDE
> Run the script
> CSV2JSON Converter will popup
> Upload csv file
> Press convert and save file
> Check default durectory for JSON file
> For unit tests, open test_csv2jsonconverter file,Run it, all tests pass successfully and OK.
> Done.

## Your solution should consist of at least:

Python code (version > 3.6) :- OK
Unit tests (Framework of your preference) :- OK
requirements file (for dependencies):- OK
README.md containing instructions for execution:- OK




