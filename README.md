## Rajasthan Hackathon 2.0

This project is aim towards improving the service of bhamashah service by government of Rajasthan.
What our project is doing is that it fetches first data from server (because it doesn't own the data), after
fetching the data from the server it indexes the data according to need of the queries.

#### Frameworks used
* Server : Django
* Database : PostgreSQL
* Searching : Elastic Search

## Structure

* **helper** : Contains the file query helper for querying the elastic search backend
* **extractors** : Used for extracting dummy data from server
* **webhelper** : Used for network related tasks
* **views** : Main functions for api calls

Main thing is we are using different indices for different set of problems so that we don't rely on 
one index for querying. 

### Execution

You need to have elasticsearch ruuning in the background for the searching backend on the local machine.
For downloading the elasticsearch and running it, you can find that in the official [documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/_installation.html)

* You need to have database set up according to credentials mentioned in settings.py however you can alter them
as per the need.

```python
virtualenv . 
source ./bin/activate

pip install -r requirements.txt
python manage.py makemigrations
python manage.py runserver
```

Now the server is well and good running on your localhost machine and connect your android device and your 
PC on the same network so as that you can use the api. I hardcoded the url information in my app so that 
it can fetch from the server using elastic search backend. However using elastic search as cloud service
is very expensive, so we haven't deployed it on cloud. For Android app demonstrating the [server](https://github.com/yashLadha/Hackathon2.0_APP)
