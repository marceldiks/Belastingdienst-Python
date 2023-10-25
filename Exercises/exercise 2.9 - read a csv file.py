import sys

filename_in = 'Sandbox/ca-500.csv'

try:
    with open(filename_in) as f:
        headers = f.readline().strip().split(';')

        for line in f:
            fields = line.strip().split(';')

            d = dict(zip(headers, fields))

            if d['city'] == 'Montreal':
                print('{:16} {:16} {:16} {}'.format(d['first_name'], 
                                                    d['last_name'], 
                                                    d['city'], 
                                                    d['email']))

                # print(f"{d['first_name']:16} {d['last_name']:16} {d['city']:16} {d['email']}")

except FileNotFoundError as ex:
    print(f'Bestand {filename_in} bestaat niet.')
    sys.exit(-1)

except KeyError as ex:
    print(f'Veld bestaat niet. {ex}')    
