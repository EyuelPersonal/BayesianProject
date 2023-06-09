To run our code please complete the following:

To create and run with a Python3.9 environment run the following command in the project root folder:


python3.9 -m venv env
source env/bin/activate  ## please note this is a linux command and may differ for windows users
pip install --upgrade pip 
python3 -m pip install -r requirements.txt

Go into the notebook "Final_Bayesian_notebook.ipynb" and select the kernel you created.

Running all cells should run the whole code base seamlessly.

You may want to reduce the tuning and sampling parameters in the "pm.sample()" methods to reduce the runtime of the overall notebook.
