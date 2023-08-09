#!/bin/bash

identify -format "%w %h %f\n" ./f1* | sort -n -r -k 1 >> ../d.txt
identify -format "%w %h %f\n" ./f2* | sort -n -r -k 1 >> ../d.txt
identify -format "%w %h %f\n" ./f3* | sort -n -r -k 1 >> ../d.txt
identify -format "%w %h %f\n" ./f4* | sort -n -r -k 1 >> ../d.txt
identify -format "%w %h %f\n" ./f5* | sort -n -r -k 1 >> ../d.txt
identify -format "%w %h %f\n" ./f6* | sort -n -r -k 1 >> ../d.txt
identify -format "%w %h %f\n" ./f7* | sort -n -r -k 1 >> ../d.txt
identify -format "%w %h %f\n" ./f8* | sort -n -r -k 1 >> ../d.txt
identify -format "%w %h %f\n" ./f9* | sort -n -r -k 1 >> ../d.txt
identify -format "%w %h %f\n" ./f0* | sort -n -r -k 1 >> ../d.txt
identify -format "%w %h %f\n" ./t1* | sort -n -r -k 1 >> ../d.txt
identify -format "%w %h %f\n" ./t2* | sort -n -r -k 1 >> ../d.txt
identify -format "%w %h %f\n" ./t3* | sort -n -r -k 1 >> ../d.txt
identify -format "%w %h %f\n" ./t4* | sort -n -r -k 1 >> ../d.txt
identify -format "%w %h %f\n" ./t5* | sort -n -r -k 1 >> ../d.txt
identify -format "%w %h %f\n" ./t6* | sort -n -r -k 1 >> ../d.txt
identify -format "%w %h %f\n" ./t7* | sort -n -r -k 1 >> ../d.txt
identify -format "%w %h %f\n" ./t8* | sort -n -r -k 1 >> ../d.txt
identify -format "%w %h %f\n" ./t9* | sort -n -r -k 1 >> ../d.txt
identify -format "%w %h %f\n" ./t0* | sort -n -r -k 1 >> ../d.txt