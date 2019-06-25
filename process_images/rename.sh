i=0; for FILENAME in *; do i=`expr $i + 1`; echo $i; mv $FILENAME IM_$i.jpg; done
