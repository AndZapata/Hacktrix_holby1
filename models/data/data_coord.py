#!/usr/bin/python3
''' Data by selected Zone '''


usr_1 = {'username': 'juanito', 'ubicacion': [4.651375, -74.057543]}
coordenates = {'zone_1': {'coord': [[4.627890, -74.068540],
                                    [4.626040, -74.065890],
                                    [4.631366, -74.064377],
                                    [4.632500, -74.067714]],
                          'days': ['Mart', 'Juev', 'Sab'],
                          'Hour': ['6pm', '2am'],
                          'name': 'Chapinero Central'},
               'zone_2': {'coord': [[4.632682, -74.067714],
                                    [4.655577, -74.062543],
                                    [4.655577, -74.062489],
                                    [4.632276, -74.066426]],
                          'Days': ['Lun', 'Mart', 'Mier',
                                   'Juev', 'Vier', 'Sab', 'Dom'],
                          'Hour': ['10pm', '6am'],
                          'name': 'Chapinero Av.Caracas-cra13'},
               'zone_3': {'coord': [[4.632276, -74.066426],
                                    [4.631431, -74.064270],
                                    [4.651375, -74.057543],
                                    [4.655492, -74.062543]],
                          'Days': ['Mart', 'Juev', 'Sab'],
                          'Hour': ['6pm', '2am'],
                          'name': 'Chapinero cra13-cra7ma'},
               'zone_4': {'coord': [[4.655492, -74.062543],
                                    [4.659352, -74.061717],
                                    [4.654818, -74.055484],
                                    [4.651385, -74.057576]],
                          'Days': ['Mart', 'Juev', 'Sab'],
                          'Hour': ['6pm', '2am'],
                          'name': 'Chapinero cll45-cll72'},
               'zone_5': {'coord': [[4.659320, -74.061846],
                                    [4.668035, -74.060097],
                                    [4.661790, -74.049915],
                                    [4.654914, -74.055483]],
                          'Days': ['Lun', 'Mier', 'Vier'],
                          'Hour': ['6pm', '2am'],
                          'name': 'Chapinero cll72-cll80'}}
def Sort(sub_list):
    ''' Sort a list by second arg '''
    sub_list.sort(key = lambda x: x[1])
    return sub_list

def in_zone(lista=[]):
    for key, val in coordenates.items():
        if usr_1.get('ubicacion') in val.get('coord'):
            print('La ruta para tu zona de nombre {}, pasa los dias {}, en el siguiente Horario {}'.format(val.get('name'), ', '.join(val.get('Days')), '-'.join(val.get('Hour'))))
        else:
            print('La zona que intentas ubicar no se encuentra disponible')

    '''m = []
    try:
        m.append((a[0][1] - a[1][1]) / (a[0][0] - a[1][0]))
        m.append((a[2][1] - a[3][1]) / (a[2][0] - a[3][0]))
        m.append((a[0][1] - a[2][1]) / (a[0][0] - a[2][0]))
        m.append((a[1][1] - a[3][1]) / (a[1][0] - a[3][0]))
        if (m[0] * usr_1.get('ubicacion')[0] - a[0][0]) + a[0][1] < usr_1.get('ubicacion')[1]:
            print('not in zone')
    except:
        print('1')
    print(m)'''
