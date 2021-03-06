import argparse
import gym
import random
import gym_sgw  # do not remove this import
from gym_sgw.envs.enums.Enums import Actions, PlayTypes
from gym_sgw.envs.Print_Colors.PColor import PFont

parser = argparse.ArgumentParser(description='CLI Argument Parser for Basic Testing.')
parser.add_argument('--action_encoding', help='Test encoding and decoding actions.', default=False, action='store_true')
parser.add_argument('--sample_actions', help='Print out sample actions.', type=int, default=0)
parser.add_argument('--state_structure', help='Print out state structure.', default=False, action='store_true')
parser.add_argument('--take_step', help='Take a random step and print results.', default=False, action='store_true')


def check_evn(do_encoding=False, sample=0, do_states=False, do_step=False):

    env = gym.make('SGW-v0')

    if do_encoding:     # checks that encoding and decoding works
        env.print_player_action_selections()
        test_action_1 = random.choice(list(Actions))
        test_action_1_decoded = env.decode_raw_action(test_action_1)    #will reencode a decoded string for
        test_action_1_encoded = env.encode_raw_action(input_str=test_action_1.value)    #checks that encode and decode functions are working

        print(PFont.underline + 'Test 1:' + PFont.reset + '\nOriginal: {0}\nDecoded: {1}\nRecovered: {2}'.format(
            test_action_1, test_action_1_decoded, test_action_1_encoded))
        test_action_2 = random.choice(range(len(Actions)))
        test_action_2_encoded = env.encode_raw_action(input_str=test_action_2)
        test_action_2_decoded = env.decode_raw_action(test_action_2_encoded)
        print(PFont.underline + 'Test 2:' + PFont.reset + '\nOriginal: {0}\nDecoded: {1}\nRecovered: {2}'.format(
            test_action_2, test_action_2_decoded, test_action_2_encoded))

    for i in range(sample):
        raw_action = env.action_space.sample()
        encoded_action = env.encode_raw_action(raw_action)  # Clean up
        readable_action = env.decode_raw_action(encoded_action)  # Make readable
        print(PFont.underline + 'Raw Action Sample {}: {}'.format(i, raw_action) + PFont.reset)
        print('Readable Action Sample {}: {}'.format(i, readable_action))

    if do_states:
        print(PFont.underline + 'Action Space:' + PFont.reset + '\n{}'.format(env.action_space))
        print(PFont.underline + 'Sample Space:' + PFont.reset + '\n{}'.format(env.observation_space))



###### IMPORTANT - GAMEPLAY LOOP IN ACTION


    if do_step:
        print('Initial Render:')
        env.render(mode=PlayTypes.human)            #Renders the game for the human
        action = env.action_space.sample()
        action_encoded = env.encode_raw_action(action)      #encode for added protection
        print('Action Selection: \n{}'.format(env.decode_raw_action(action_encoded)))
        observation, reward, done, info = env.step(action)      # takes a step/"turn" (moving on the board: go forward or turn)
        print('State: \n{}'.format(observation))    #returns new "state" (observation)
        print('Turn Score: {}'.format(reward))      #returns reward
        print('Is Done: {}'.format(done))           #returns status
        print('Info: {}'.format(info))              #returns varying information from that turn
        print('Turn Render:')
        env.render(mode=PlayTypes.human)            #Renders the NEW state


# MAIN LOGIC:
if __name__ == '__main__':
    args = parser.parse_args()
    action_encoding: bool = args.action_encoding  #stores action_encoding as a boolean
    sample_actions: int = args.sample_actions
    state_structure = args.state_structure
    step = args.take_step
    check_evn(action_encoding, sample_actions, state_structure, step)   #Function defined above:


