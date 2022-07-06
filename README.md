# Short Url Application
Service to shorten url
-----------------------------------------------------------------------------------
This application takes long URLs and gives a shorter version of the URL. 
We store the short and long URLs in a DataBase and redirect accordingly.
-----------------------------------------------------------------------------------

Instructions to run the application:
1. Clone the repo using `git clone https://github.com/Vish-Yadlapalli/shortUrl.git`
2. Adjust the environment variables in `.env` file to match the DB you are using. 
3. Install dependencies listed in requirements.txt
3. Run `flask run` on your terminal to run the application locally

    ![](demo.gif)

------------------------------------------------------------------------------------
Future Work: 
- Increase test coverage to Functional tests and integration tests
- Admin functionality to manage links
- Authentication to access admin panel
- Filter out potential spam links
- Dockerize the application to minimize environment issues and scale deployments
-------------------------------------------------------------------------------------
Maintenance expectations:
- Server maintenance:
    - When the traffic scales, this service needs more application servers to handle incoming requests without latency.
    - To ensure low latency, we need to maintain Disk, CPU and Memory usage levels. 
    - As this is a redirecting service, Firewalls and networks need be maintained. Also, the network usage and latence levels need to be maintained.
    - Server upgrades
- Database maintenance:
    - This service needs persistant storage and brings the necessity for database management.
    - Backing up the Databases regularly and test the backups for restoration.
    - Monitor the performance of databases and increase the capacity if required. 
- Security:
    - As this is a redirecting service, there is high risk of cyber attacks. 
    - Hence, we need to secure the endpoints with SSL layer, firewall and access management. 
    - Check the servers for malware.
    
    
