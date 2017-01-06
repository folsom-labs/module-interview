import csv

Q = 1.60217657e-19
K = 1.3806488e-23
T = 273.


def your_code_here(*args, **kwargs):
    pass


def read_csv(filename, field_names):
    """load a structured csv file

    Arguments:
        filename {str} -- the path to the file to be loaded
        field_names {List} -- an array of field names in the order of the
                              columns in the csv
    Returns:
        [type] -- [description]
    """
    rtn = []
    with open(filename) as f:
        reader = csv.DictReader(f, fieldnames=field_names)
        reader.next()
        for row in reader:
            rtn.append(row)

    return rtn

def get_parameters(name):
    """get the parameters for a solar module

    Arguments:
        name {str} -- the name of the module you'd like to load
    Returns:
        [dictionary] -- the parameters of the modules
    """
    field_names = ['manufacturer', 'name', 'power', 'i_sc', 'gamma', 'i0',
                   'r_series', 'r_parallel', 'temp_i0']

    all_parameters = read_csv('data.csv', field_names)

    return next(x for x in all_parameters if x['name'] == name)

if __name__ == '__main__':
    import pprint
    pprint.pprint(get_parameters('TSM PA05'))
