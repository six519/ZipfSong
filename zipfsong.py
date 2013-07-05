#!/usr/bin/env python
"""
 :) :) :) :)
"""

if __name__ == "__main__":

    inputs = []
    while 1:

        try:
            inputs.append(raw_input())
        except Exception:
            break

    songs = [{'played': int(inpt.split()[0]),'nm':inpt.split()[1], 'quality': int(inpt.split()[0]) * (i + 1)} for i, inpt in enumerate(inputs[1:int(inputs[0].split()[0]) + 1])]
    result = sorted(songs, key=lambda song:song['quality'], reverse=True)[:int(inputs[0].split()[1])]
    print "\n".join([s['nm'] for s in result])

