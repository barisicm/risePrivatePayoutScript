# Mr_Mojo Rise Private Delegate Pool

This software was created by rise delegate "mr_mojo", 

### Prerequisitions

```
sudo apt-get install python3
sudo apt-get install python3-requests
sudo apt-get install curl
```

Download / clone repo

```
git clone https://github.com/barisicm/risePrivatePayoutScript
```

then rename folder to your own pool site
Configuration

Fork this repo; edit risepool.py and modify the first lines with your settings:

    PUBKEY: your delegate pubkey

    SECRET: your secret

    SECONDSECRET: your second

    NODE: the lisk node where you get forging info

    NODEPAY: the lisk node used for payments

    RISEPERDAY: the amount of rise to payout

    PAYINGDELEGATEADDRESS: the address of your delegate wallet

Info about your voters will be inside the privatepoollogs.json file. In there you will write the name of your voters (if you know them), the addresses to which the payouts will be made. And of course the amount to pay each of them.

### Running it

```
python3 liskpool.py
```

It produces a file "payments.sh" with all payments shell commands. Run this file with:

```
bash payments.sh
```

The payments will be broadcasted (every 10 seconds). 

The script is also runnable by cron using the -y argument:

```
python3 liskpool.py -y`
```

or

```
bash batch.sh
```

This 'batch.sh' file will run liskpool, then payments.sh and copy the poollogs.json in the docs folder.


## License

Copyright 2017 Davide Gessa

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

#### copyright background

https://www.oneseaecosystem.net
