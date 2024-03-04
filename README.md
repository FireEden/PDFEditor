# PDFEditor
Python based PDF editor to open pdf, remove pages, and save pdf

#### Video Demo:  <URL HERE>

#### Description: 
This python package contains an offline tool to users to delete pages of a PDF file. This project was inspired by my personal need to edit pdf files without paying for Adobe Professional or editing on web-based services with questionable data-privacy.

### Features: 
This package contains 3 types page removal; single page, page range, and mutiple pages.

Single - remove a single page from the file. Example: "2" representing remove page 2.

Range - removes a range of pages from the file.     Example: "2-5" representing removing pages 2,3,4,and 5

Multiple pages: removes a selection of pages(separated by commas). Example: "2,3,6" representing removing pages 2,3, and 6.


### Error checking:
A number of error checking and user friendly prompts are built-in the package

#### Open File Validation
1. PDF extension only
2. Name must only be comprised of numbers, word characters and underscores.
3. File name must be find a match in the location. 

Any error in the above 3 validation checks will result in exit of program.

#### Save File Validation
1. PDF extension only
2. Name must only be comprised of numbers, word characters and underscores.

Any error in the above 2 validation checks will result in a reprompt of the file name input.
