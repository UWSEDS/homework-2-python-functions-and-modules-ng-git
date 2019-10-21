{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import math\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "%matplotlib inline\n",
    "import matplotlib\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Read the CSV file into a pandas dataframe.\n",
    "def read(input)\n",
    "    df = pd.read_csv(input)\n",
    "    df.head()\n",
    "    \n",
    "#Add columns to the dataframe containing:\n",
    "# The total (East + West) bicycle count\n",
    "   # df['Total bicycle count'] = df['Fremont Bridge East Sidewalk'] + df['Fremont Bridge West Sidewalk'] \n",
    "\n",
    "# The hour of the day\n",
    "#hours = []\n",
    "#for value in df['Date']:\n",
    "#    if value[20:23] == 'PM':\n",
    "#        extra = 12\n",
    "#    else:\n",
    "#        extra = 0\n",
    "#    hours.append(int(value[11:13]) + extra)\n",
    "#df['Hour'] = hours\n",
    "\n",
    "# The year\n",
    "#years = []\n",
    "#for value in df['Date']:\n",
    "#    years.append(int(value[6:11]))\n",
    "#df['Year'] = years\n",
    "#f.head()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
