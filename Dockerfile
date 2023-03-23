# first layer is our python base image enabling us to run pip
FROM python:3.10-windowsservercore-1809

# create directory in the container for adding your files
WORKDIR /user/src/app

# copy over the requirements file and run pip install to install the packages into your container at the directory defined above
COPY ./mt5connector-investor/requirements.txt ./
RUN python.exe -m pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY ./mt5connector-investor/ ./mt5connector-investor/
COPY ["./MetaTrader 5/", "C:/Program Files/MetaTrader 5/"]
WORKDIR "/mt5connector-investor"
# enter entry point parameters executing the container
ENTRYPOINT ["powershell.exe"]

# exposing the port to match the port in the runserver.py file
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

#CMD [ "/MetaTrader/terminal64.exe", "/portable" ]
# build
# docker build -t mt5connector-investor .
# run
# docker run mt5connector-investor -p 8000:8000