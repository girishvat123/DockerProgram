# Consumer Data Collection 

This simple software extracts the data from mutliple `metrics.json` files corresponding to the consumers and 
outputs the metrics data to a single csv file. This is primarily built for running on **python3**. If you have both versions of python 2 and 3 installed, please change the below commands for **python** to **python3** depending on what is the default python environment.

## Steps for Running it in your own local machine with the cloned repository

1. Clone the repository:
  ```git clone git://github.com/girishvat123/NetSkopeTakeHome``` 

2. ```cd ConsumerDataCollection```

3. Run the following command:
    ```./dist/runnable.exe <nameOfTheOutputFile> /path/to/jsonfilesfolder/```

4. You can see the outputfile with the name you mentioned created in your directory. 

## Steps for running the python script directly

1. Clone the repository as mentioned in step 1 above section.

2. ```cd ConsumerDataCollection```

3. Run below command:

   ```python runnable.py <nameOfTheOutputFile> /path/to/jsonfilesfolder/```

4. You can see the outputfile with the name you mentioned created in your directory.    