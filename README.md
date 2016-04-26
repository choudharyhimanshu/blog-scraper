
### What is this repository for? ###

To scrape useful data from a blogger's website (mainly focused on travel blogs). It has several types of spiders and each spider scrapes different type of webpage.

### How do I get set up? ###

Required Python Libraries : scrapyrt, tweepy 

To install **scrapyrt**, follow the installation guide given in its repository [https://github.com/scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt)

To install **tweepy**, use the following pip command

```
pip install tweepy
```

Once you have installed both the required libraries, open a terminal in the root directory of this repository and type the following command to start the server

```
scrapyrt
```

### API ###

You can send a simple HTTP GET request to the server running at localhost:9080 (9080 is the default port) to get the scraped data in JSON format.

This will a general form of the request

```
http://localhost:9080/crawl.json?spider_name=SPIDER&url=URL
``` 
Where *SPIDER* will be the spider you want to use. And *URL* will be the url of the webpage you want to scrape.

Currently there are 3 spiders which are as follows:

1). **blogsite** : To get links and titles of all blogs present in a blogger's webpage

Sample Request : http://localhost:9080/crawl.json?spider_name=blogsite&url=http://www.traveljunkiejulia.com/

2). **blog** : To get all useful data from a blog page

Sample Request : http://localhost:9080/crawl.json?spider_name=blog&url=http://bucketlistjourney.net/2016/02/trek-through-a-sri-lankan-village-hiriwadunna/

3). **twitterprofile** : To get user's website url and other useful public data from twitter profile.

Sample Request : http://localhost:9080/crawl.json?spider_name=twitterprofile&url=https://twitter.com/5foottraveler


### Who do I talk to? ###

Himanshu Choudhary

Email : himanshuchoudhary@live.com

Homepage : http://www.himanshuchoudhary.com