 # PDF Page Editor
#### Video Demo:  <URL HERE>

#### Description: 
This python package contains an offline tool to users to delete pages of a PDF file. This project was inspired by my personal need to edit pdf files without paying for Adobe Professional or editing on web-based services with questionable data-privacy.

### Features: 
This package contains 3 types page removal; single page, page range, and mutiple pages.

Single - remove a single page from the file. Example: "2" representing remove page 2.

Range - removes a range of pages from the file.     Example: "2-5" representing removing pages 2,3,4,and 5

Multiple pages: removes a selection of pages(separated by commas). Example: "2,3,6" representing removing pages 2,3, and 6.

#### Selecting modes:
1. User shall type the desired mode of page deletion. Inputs are case insensitive: 

    a. single

    b. range

    c. multiple pages

    **Single** mode allows users to delete one page from the file

    **Range**
     mode allows users to delete a range containing 1 or more pages from the file

    **Multiple pages** allows users to delete one or more sequence of pages from the file

### Error checking:
A number of error checking and user friendly prompts are built-in the package

#### Open File Validation
1. PDF extension only
2. Name must only be comprised of numbers, word characters, spaces, and underscores.
3. File name must be find a match in the location. 

Any error in the above 3 validation checks will result in exit of program.

#### Single Mode Validation
1. Page to delete must be a number
2. Page to delete must be <= 1 and <= the total pages in the file

Any error in the above 2 validation checks will result in a reprompt.

#### Range Mode Validation
1. Range must be in the format of *x-y* with *x* being the starting page to delete and *y* being the ending page to delete
2. Pages in range must be a number
3. Page to delete must be <= 1 and <= the total pages in the file

Any error in the above 3 validation checks will result in a reprompt.

#### Multiple Papges Mode Validation
1. Page(s) must be sepaprated by commas (",")
2. Pages in sequence must be a number
3. Page to delete must be <= 1 and <= the total pages in the file

Any error in the above 3 validation checks will result in a reprompt.

#### Save File Validation
1. PDF extension only
2. Name must only be comprised of numbers, word characters, spaces, and underscores.

Any error in the above 2 validation checks will result in a reprompt of the file name input.




