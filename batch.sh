echo "--------------------------------------------------------------------"
echo "--------------------------------------------------------------------"
cd /home/USERNAME/DELEGATEDIRECTORY
sleep $(( ( RANDOM % 1800 )  + 1 ))
sudo python3 /home/USERNAME/DELEGATEDIRECTORY/liskpool.py -y
bash /home/USERNAME/DELEGATEDIRECTORY/payments.sh
sudo cp /home/USERNAME/DELEGATEDIRECTORY/poollogs.json /var/www/html/poollogs.json
##when using crontab under user and using a dedicated server, content of docs in html folder##




