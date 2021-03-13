import readline

def make_completer(vocabulary):
    def custom_complete(text, state):
        # None is returned for the end of the completion session.
        results = [x for x in vocabulary if x.startswith(text)] + [None]
        # A space is added to the completion since the Python readline doesn't
        # do this on its own. When a word is fully completed we want to mimic
        # the default readline library behavior of adding a space after it.
        return results[state] + " "
    return custom_complete

def main():
    vocabulary = {'cat', 'dog', 'canary', 'cow', 'hamster'}
    readline.parse_and_bind('tab: complete')
    readline.set_completer(make_completer(vocabulary))

    try:
        while True:
            s = input('>> ').strip()
            print('[{0}]'.format(s))

            if (s == 'h'):
                print("histoy -----")
                cnt = readline.get_current_history_length()
                print("cnt=", cnt)
                for i in range(cnt):
                    print(readline.get_history_item(i))
                print('endof history')
    except (EOFError, KeyboardInterrupt) as e:
        print('\nShutting down...')

if __name__ == '__main__':
    main()
