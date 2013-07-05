#!/usr/bin/env python
import sys

class ZipFSong(object):


    def run(self):

        try:

            line = sys.stdin.readline().strip()
            song = ()
            qualityList = []
            selc = 0

            splittedInput = line.split(" ")
            songToBeSelected = long(splittedInput[1])

            for n in xrange(long(splittedInput[0])):

                line = sys.stdin.readline().strip()

                splittedInput = line.split(" ")

                quality = long(splittedInput[0]) * (n + 1)
                #song.append()
                song += ((str(splittedInput[1]), quality),)
                if quality not in qualityList:
                    qualityList.append(quality)
            
            while selc != songToBeSelected:
                
                #max_num = mxsort(qualityList)
                #max_num = sorted(qualityList)[-1]
                max_num = max(qualityList)

                for i, nn in enumerate(qualityList):
                    if nn == max_num:
                        del qualityList[i]

                for s in song:
                    if s[1] == max_num:
                        selc += 1
                        sys.stdout.write(s[0] + "\n")
                        #print s[0]
            return 0

        except Exception as e:
            return -1

if __name__ == "__main__":
    ZipFSong().run()