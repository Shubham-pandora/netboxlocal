for i in {1..255} ;do
  ping -c 1 -t 1 192.168.1.$i > /dev/null 2>&1;
    if [ $? -eq 0 ]; then
        echo 192.168.1.$i up `nbtscan 192.168.2.$i | awk '{print $2}' | tail -1`
	echo 192.168.1.$i up `sshpass -p "padnet" ssh root@192.168.1.$i uname -n`
    else
	echo "192.168.1.$i"	Down;
    fi
done