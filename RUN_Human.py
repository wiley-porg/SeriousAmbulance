import os
import argparse
from SGWHumanPlay_1 import SGW
from gym_sgw.envs.enums.Enums import MapProfiles

parser = argparse.ArgumentParser(description='CLI Argument Parser for Human Play.')
parser.add_argument('--outfile', help='Data logging file name.', default='data_log.json')
parser.add_argument('--creation', help='Allow creation of output file.', default=True, action='store_true')
# parser.add_argument('--NEWARGUMENT',...)          #Add new arguments

def validate_data(out_file, allow_creation=False):
    if allow_creation and not os.path.exists(out_file):
        f = open(out_file, 'w+')
        f.close()
    if not os.path.isfile(out_file):
        raise EnvironmentError('Bad filename provided in CLI arguments.')


if __name__ == '__main__':

    # Parse CLI Args
    args = parser.parse_args()
    os.system('mode con: cols=125 lines=62')
    validate_data(args.outfile, allow_creation=args.creation)

    # Set runtime args
    data_log_file = args.outfile

    #map_file = 'gym_sgw/envs/maps/classic_trolley-ambiguous.xls'  # None -> random map, map files have top priority
    #map_file = "C:/Users/lehma/PycharmProjects/SGW_CW1/gym_sgw/envs/maps/custom/custom_maps/custom_map_2.xls"
    map_file = None
    max_energy = 100
    rand_prof = MapProfiles.trolley     #can change map to "volcano"
    num_rows = 10
    num_cols = 10                       #set map size

    # Create and run game with those params
    sgw_env = SGW(
        data_log_file=data_log_file,
        map_file=map_file,
        max_energy=max_energy,
        rand_prof=rand_prof,
        num_rows=num_rows,
        num_cols=num_cols
    )
    sgw_env.run()

# changed here
