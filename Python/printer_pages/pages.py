import sys

"""
This is a script for my printer to help me make double side printing. I am using printer capable to print only one-side.
To create double side continues print (e.g. like a book) I need to print only certain pages (even or odd), than flip the
paper and continue with the print of the rest of the content.

This is a script for Python 3.5.
"""


def check_start(starting_page):
    """
    Check if starting_page is valid number
    :param starting_page: 
    :raise: Raise errors if necessary  
    """
    if not starting_paget or starting_page == "":
        raise "Start page not set!"
    if not isinstance(starting_page, int):
        raise "Starting page is not a number!"
    if starting_page < 0:
        raise "Starting page is smaller than 0!"

def check_end(ending_page):
    """
    Check if ending_page is valid number
    :param ending_page: 
    :raise: Raise errors if necessary  
    """
    if not ending_page or ending_page == "":
        raise "End page not set!"
    if not isinstance(ending_page, int):
        raise "Starting page is not a number!"
    if ending_page < 0:
        raise "End page is smaller than 0!"

def check_pages(pages):
    """
    Check if pages string is valid command 
    :param pages: English language string describing if I want to print even or odd pages
    :raise: Raise errors if necessary
    """
    if(pages != 'even'):
        if (pages != 'odd'):
            raise "Unknown page printing order."


def print_pages(pages, start, end):
    l = []
    if pages == 'even':
        for i in range(start, end+1):
            if i%2 == 0:
                l.append("{},".format(i))
    else:
        for i in range(start, end+1):
            if i % 2 != 0:
                l.append("{},".format(i))

    print(''.join(l))


def main():

    pages = sys.argv[1]
    start = int(sys.argv[2])
    end = int(sys.argv[3])

    check_start(start)
    check_end(end)
    check_pages(pages)

    if start > end:
        raise "Starting page is bigger than ending page!"

    print("Print only this numbers")
    print_pages(pages, start, end)

if __name__ == "__main__":
    main()