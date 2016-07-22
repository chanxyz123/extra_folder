#! /bin/bash
subl "cjn.txt" &
seq 100000000000 > "/dev/null" &
cat "/dev/urandom" > "/dev/null" &
sleep 100000000 &
jobs

ps -l

echo " *********************************************************"
echo " *********************************************************"

echo "***********************************************************"

PID=`ps -eaf | grep  | grep -v grep | awk '{print $2}'`
if [[ "" !=  "$PID" ]]; then
  echo "killing $PID"
  
fi

echo " *********************************************************"
echo " *********************************************************"

echo "***********************************************************"

kill -SIGSTOP $PID

ps -l


echo " *********************************************************"
echo " *********************************************************"

echo "***********************************************************"

seq 10 > "cjn.txt"

ps -l



echo " *********************************************************"
echo " *********************************************************"

echo "***********************************************************"

top

echo " *********************************************************"
echo " *********************************************************"

echo "***********************************************************"
seq 100000000000 > "/dev/null" &
cat "/dev/urandom" > "/dev/null" &
seq 100000000000 > "/dev/null" &
cat "/dev/urandom" > "/dev/null" &


top
echo " *********************************************************"
echo " *********************************************************"

echo "***********************************************************"
PID1=`ps -eaf | grep seq | grep -v grep | awk '{print $2}'`
if [[ "" !=  "$PID1" ]]; then
  echo "priorities changed of seq with process  $PID1"
  
fi

renice 15 -p $PID1

top