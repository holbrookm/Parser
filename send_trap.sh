#!/bin/sh
Severity=$1
ProbCause=$2
#TrapDestination=172.30.2.8
TrapDestination=10.204.6.17
CommunityString=nssd
Enterprise=1.3.6.1.4.1.9584
GenericTrap=6
SpecificTrap=120
senderIP=10.147.48.114
/home/marc/trapgen/trapgen -d $TrapDestination -i $senderIP -c $CommunityString -o $Enterprise -g $GenericTrap -s $SpecificTrap -v 1.3.6.1.4.1.9584.1 INTEGER "$Severity" -v 1.3.6.1.4.1.9584.2 STRING "$ProbCause" 
