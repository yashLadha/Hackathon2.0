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
