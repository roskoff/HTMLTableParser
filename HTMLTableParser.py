from HTMLParser import HTMLParser

class HTMLTableParser(HTMLParser):
    """Parses all tables in a web page and return a list of them

    This class walk through every tag on a web page and collects
    data from tables, returning a list of all found tables. Data
    rows are returned as sublists of every table found.

    HTMLTableParser aims to collect the raw data found on <td>
    and <th> tags, said that, if we found:

       <td class="rowHeader"> 
           <strong>2,048</strong>MB RAM
           <div class="subtitle"><strong>80</strong>GB Disk</div> 
       </td>

    will return "2,048 MB RAM 80 GB Disk" as a sublist element

    HTMLTableParser extends HTMLParser class from HTMLParser Python
    standard library.
    
    """

    def __init__(self):
        """ Creates a new HTMLTableParser and initializes internal data

        Public attributes
        tables: The list of tables found on the web page

        """
        global HTMLParser
        HTMLParser.__init__(self)

        # List of tables found on web page
        self.tables = []

        self.table_counter = -1
        self.row_counter = -1
        self.column_counter = -1

        # Indicates if we are parsing inside a <td> or <th> tags
        self.inside_td = False

    def handle_starttag(self, tag, attrs):
        """ Overrides ancestor method, parsing table related tags

        This method is private and parses <table>, <tr>, <td>
        and <th> tags. Here we construct the lists of tables and
        its respective rows.

        """

        if tag == 'table':
            self.table_counter = self.table_counter + 1
            self.row_counter = -1
            self.column_counter = -1
            self.tables.append([])
        elif tag == 'tr':
            self.tables[self.table_counter].append([])
            self.row_counter = self.row_counter + 1
            self.column_counter = -1
        elif tag == 'td' or tag == 'th':
            self.tables[self.table_counter][self.row_counter].append('')
            self.column_counter = self.column_counter + 1
            self.inside_td = True

    def handle_endtag(self, tag):
        """ Overrides ancestor method, parsing table related tags

        This method is private and parses </tr>, </td>, so we can
        know when we are exiting a data tag.

        """

        if tag == 'td' or tag == 'th':
            self.inside_td = False

    def handle_data(self, *args):
        """ Overrides ancestor method, parsing table data

        This method is private and saves the data in the current
        element of the current table.

        """

        value = args[0].strip()
        if self.inside_td and value != '':
           table_value = self.tables[self.table_counter][self.row_counter][self.column_counter]
           table_value = table_value + ' ' + value
           self.tables[self.table_counter][self.row_counter][self.column_counter] = table_value


    def handle_entityref(self, *args):
        """ Overrides ancestor method, parsing table data

        This method is private and saves the special entity references as 
        data in the current element of the current table.

        """

        ref_values = {'mdash': ' - ', 'cent':' cent.'}
        if self.inside_td:
            if args[0] in ref_values.keys():
                table_value = self.tables[self.table_counter][self.row_counter][self.column_counter]
                table_value = table_value + ref_values[args[0]]
                self.tables[self.table_counter][self.row_counter][self.column_counter] = table_value

