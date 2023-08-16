FROM git.manifone.com:4443/manifone-data/mnfn-ia-dockers:mnfn-fastapi-latest
# FROM mnfn-fastapi
LABEL AUTHOR=MariaSoto 
LABEL MAIL=m.soto@manifone.com

# build the different folders required
RUN mkdir -p /requirements
RUN mkdir -p /app
RUN mkdir -p /database

# Add requirements files and get the necessary pip packages
COPY requirements*.txt /requirements/
RUN pip install -r /requirements/requirements.txt

# Add all the project files to the root
COPY ./app /app