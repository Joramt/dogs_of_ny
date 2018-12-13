# Dogs of NY 
This is a tornado based web application that use a `/count` endpoint to query a CSV from [the dogs of NY](https://fusiontables.google.com/datadocid=1pKcxc8kzJbBVzLu_kgzoAMzqYhZyUhtScXjB0BQ). It has been coded in a way that any CSV would be able to be queried the same way.

In order to query the dogs of NY file, you must pass a valid filter via the query string. The filters should match your CSV header; in this case those are our headers : 
`dog_name, gender, breed, birth, dominant_color, secondary_color, third_color, spayed_or_neutered, guard_or_trained, borough, zip_code`

example of filtering : `/count?dog_name=buddy&gender=m`
Any attempt to filter by a non existent filter will result in an error.

Once the data have been correctly filtered, the `/count` endpoint will return a JSON-object containing the number of dogs who matches your filterd

example of response : `{"count": 593}`

## Installation

### Fetch the project

Download the base code by running the command below or via my [github repository ](https://github.com/Joramt/dogs_of_ny)
 ``` console
git clone git@github.com:Joramt/dogs_of_ny.git
cd dogs_of_ny
git pull origin master
```  

### Set up your virtual environnement

Make sure first the `virtualenv` package is installed with the following command :
 ``` console
python3 -m virtualenv --version
```  

If not, install it using `pip`.
```console
python3 -m pip install --user virtualenv
```
 [Read this thread](https://stackoverflow.com/questions/17271319/how-do-i-install-pip-on-macos-or-os-x) if you need any help regarding on how to install pip on your Mac/Ubuntu machine.

- Create your virtual env 
 ``` console
python3 -m virtualenv jorelamthor_testingenv
```  
- Activate the newly created virtual environnement
 ``` console
source env/bin/activate
```  

Note : your python version might differ

### Install the dependencies

Making sure that you're in the `dogs_of_ny` folder, that you've created and activated your virtual environnement, run the following command :
 ``` console
sudo pip install -r requirements.txt
```  
This will install every needed dependencies into your virtual environnement.

## Run the Tornado server

 ``` console
python3 main.py
```  

At your convenience, you can also pass a `--port`option. It will use the port `5000`by default

 ``` console
python3 main.py --port=5055
```
  
## Run the test

 ``` console
cd test 
READY_TEST_BASE_URL=http://localhost:5000 python3 apitest.py
```  

Note : Make sure to use the same port that you used when running the Tornado server previously

## Clean up

 ``` console
deactivate 
rmvirtualenv jorelamthor_testingenv
cd ..
sudo rm -rf dogs_of_ny
```  

The following commants will deactivate & destroy the previously created environnement and delete the git repository downloaded

# Deployment

Using my previous knowledge and experience of AWS, this probably would have been my platform of choice to deploy this application. Since i do not have a webserver to deploy this tornado application, i will try to enumerate the modifications i would have took in order to deploy it :
- Creating a `env` file to store sensible variable ( ie : csv path )
- Making it [WSGI compliant](http://www.tornadoweb.org/en/stable/wsgi.html) in order to deploy it in Amazon Beanstalk ( who only uses WSGI for serving Python Web apps )
- Renaming the `main.py` file to `application.py` so Amazon Beanstalk would be [able to start it](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/python-development-environment.html#python-common-configuring).
- Adding [Supervisor](http://supervisord.org/) to monitor process and performance via SSH
- 
# Notes

This project follow the pep8 coding style conventions