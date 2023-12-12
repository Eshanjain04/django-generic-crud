# django-generic-crud
A small experiment in Django to generate a generic crud for any basic models.
The idea behind it is, it utilizes Django to fetch any model based on app name and model name
We created one Model to store the app-name and model-name for which we want to open the crud.

in the API endpoint, we have a keyword that identifies which model to add get or update the data.
it fetches the data from the model which contains the app-name and model-name.

then it accordingly performs operations.

In the next phase, we will also try to introduce Multiple table inputs. 


#######################################
This project also contains a small project to make a bulk uploader for any model.
It takes the configuration of the model in which we want to store data which includes app-name and model-name, headers of excel, and validation schema in json for the data.

The Bulk upload service will take the excel file and validate the header and data. If everything checks out, it will enter the data in respective model.

