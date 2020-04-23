# A dockerfile must always start by importing the base image.
# We use the keyword 'FROM' to do that.
# In our example, we want import the python image.
# So we write 'python' for the image name and 'latest' for the version.
FROM python:latest


# copy the python packages required 
# import the required python packages for the project
COPY requirements.txt .
RUN pip install -r requirements.txt


# In order to launch our python code, we must import it into our image.
# We use the keyword 'COPY' to do that.
# The first parameter 'hadith.py' is the name of the file on the host.
# The second parameter '/' is the path where to put the file on the image.
# . is the current directory 
# Here we put the file at the image root folder.
COPY . .
# We need to define the command to launch when we are going to run the image.
# We use the keyword 'CMD' to do that.
# The following command will execute "python ./hadith.py".

CMD exec gunicorn --bind 0.0.0.0:8000 --timeout 0 app:app







