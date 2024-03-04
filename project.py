import fitz
import sys
import re

class FormatError(Exception):
    "raise when the file name is not in the proper format"
    pass
class ExtensionError(Exception):
    "raise when the file extension is not accepted"
    pass
class NameError(Exception):
    "raise when the file name conntains invalid symbols"
    pass
class RangeError(Exception):
    "raise when the range is not in the format of x-y"
    pass

### Functions ###
def get_file():
    try:
        input_file = input("full file name: ")
        input_parsed = input_file.lower().split(".")
        if len(input_parsed) != 2:
            raise FormatError 
        elif input_parsed[1] != "pdf":
            raise ExtensionError
        elif re.search(r"[\!@#$%^&*()-+?_=,<>/]+",input_parsed[0]) is not None:
            raise NameError
        else:
            file_handle = fitz.open(input_file)
            #print(type(file_handle).__name__)
            total_page = file_handle.page_count
            #print(f"file opened with {total_page} pages")
            return file_handle, total_page
    except FormatError:
        sys.exit("file must contain a name and extension")
    except ExtensionError:
        sys.exit("file must contain pdf extension")
    except NameError:
        sys.exit("File name must contain only characters, numbers, and underscore")
    except fitz.FileNotFoundError:
        sys.exit("File not found")
 
def page_delete(pdf, tp):
    # Passing the variable as an argument 
    accepted_types = ["single", "range", "multiple pages"]
    while True:
        try:
            delete_type =  input("Delete mode: Single, range, or multiple pages: ").lower()
            if delete_type not in accepted_types:
                raise ValueError
            else:
                if delete_type == "single":
                    single_delete(pdf, tp)
                    return pdf
                elif delete_type == "range":
                    range_delete(pdf,tp)
                    return pdf
                else:
                    multiple_delete(pdf,tp)
                    return pdf
        except ValueError:
            print("Input single, range, or multiple pages")

def save_file(pdf):
    while True:
        file_name = save_file_name_check()
        if file_name == "Error":
            pass
        else:
            pdf.save(file_name)
            print(f"File {file_name} saved in local folder")
            break

def save_file_name_check():
        try:
            output_file = input("New file name: ")
            output_parsed = output_file.lower().split(".")
            if len(output_parsed) != 2:
                raise FormatError
            elif output_parsed[1] != "pdf":
                raise ExtensionError
            elif re.search(r"[\!@#$%^&*()-+?_=,<>/]+",output_parsed[0]) is not None:
                raise NameError
            else:
                return output_file
        except FormatError:
            print("File must contain a name and extension")
            return "Error"
        except ExtensionError:
            print("File must contain pdf extension")
            return "Error"
        except NameError:
            print("File name must contain only characters, numbers, and underscore")
            return "Error"

def single_delete(pdf, tp):
    while True:
        try:
            page = int(input("Page to delete starting at 1:")) 
        except ValueError:
            print("integer only")
            pass
        else:
            try:
                assert page >= 1 , "Page must be positive not zero"
                assert (page <= tp), "Page must me less than or equal to total pages of the document"
            except AssertionError as msg:
                print(msg)
            else:
                pdf.delete_page(page-1)
                print(f"Page {page} deleted")
                return pdf
            
def range_delete(pdf,tp):
    while True:
        try:
            delete_range = input("Range delete in the format of x-y: ")
            if re.search(r"^[0-9]+-[0-9]+$", delete_range) is None:
                raise RangeError
            else:
                start, end = delete_range.split("-")
                start = int(start)
                end = int(end)
                assert start <= tp and end <= tp, "Page range must me less than or equal to total pages of the document"
                if start > end:
                    raise ValueError
                elif start == 0:
                    raise ValueError
                else:
                    pdf.delete_pages(start-1, end-1)
                    print(f"delete from {start} to {end}")
                    return pdf
        except ValueError:
            print("Pages must be greater than 0 and first page must be less than or equal to the second page")
        except RangeError:
            print("Range must be in the format x-y")
        except AssertionError as msg:
            print(msg)

def multiple_delete(pdf,tp):
    while True:
        try:
            multi = []
            all_pages =list(range(0,tp))
            all_pages_display = list(range(1,tp+1))
            print("total pages", all_pages_display)
            input_list = list(map(int,input("Pages to delete separated by commas: ").split(",")))
            for i in input_list: # i is not index format
                print(i)
                assert i <= tp, "Page must me less than or equal to total pages of the document"
                if i < 0:
                    raise ValueError
                else:
                    multi.append(i)
                    all_pages.remove(i-1)
                    print(f"iteratively page {i} is deleted")
            print(f"Pages:{multi} deleted")
            pdf.select(all_pages)
            return pdf
        except ValueError:
            print("Invalid pages")
        except AssertionError as msg:
            print(msg)

### Main code 
def main():
    file, page_count = get_file()
    new_file = page_delete(file, page_count)
    save_file(new_file)


if __name__ == "__main__":
    main()


