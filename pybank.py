{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'/Users/kathysmacbookpro2019/Desktop'"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pwd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Store filepath in a variable\n",
    "data_file = \"budget_data.csv\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Read Data file with the pandas library\n",
    "data_file_df = pd.read_csv(data_file)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Date</th>\n",
       "      <th>Profit/Losses</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Jan-2010</td>\n",
       "      <td>867884</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Feb-2010</td>\n",
       "      <td>984655</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Mar-2010</td>\n",
       "      <td>322013</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Apr-2010</td>\n",
       "      <td>-69417</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>May-2010</td>\n",
       "      <td>310503</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       Date  Profit/Losses\n",
       "0  Jan-2010         867884\n",
       "1  Feb-2010         984655\n",
       "2  Mar-2010         322013\n",
       "3  Apr-2010         -69417\n",
       "4  May-2010         310503"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#validate data\n",
    "data_file_df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "86"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#The total numbers of months included in dataset\n",
    "#count = data_file_df[\"Date\"].value_counts()\n",
    "#count\n",
    "total_months= len(data_file_df[\"Date\"])\n",
    "total_months\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "38382578"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#net total amount of Profit/Losses over the entire period\n",
    "total = data_file_df[\"Profit/Losses\"].sum()\n",
    "total"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0         NaN\n",
       "1    116771.0\n",
       "2   -662642.0\n",
       "3   -391430.0\n",
       "4    379920.0\n",
       "Name: Profit/Losses, dtype: float64"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#calc the differences\n",
    "#.diff(self, periods=1, axis=0)\n",
    "changes = data_file_df[\"Profit/Losses\"].diff()\n",
    "changes.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "-2315.1176470588234"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#average of the changes in \"Profit/Losses\" over the entire period\n",
    "mean_changes = changes.mean()\n",
    "mean_changes\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1926159.0"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#the greatest increase in profits ( date and amount over the entire period)\n",
    "max_profits = changes.max()\n",
    "max_profits\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "-2196167.0"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#the min increase in profits ( date and amount over the entire period)\n",
    "min_profits = changes.min()\n",
    "min_profits"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Date</th>\n",
       "      <th>Profit/Losses</th>\n",
       "      <th>changes</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Jan-2010</td>\n",
       "      <td>867884</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Feb-2010</td>\n",
       "      <td>984655</td>\n",
       "      <td>116771.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Mar-2010</td>\n",
       "      <td>322013</td>\n",
       "      <td>-662642.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Apr-2010</td>\n",
       "      <td>-69417</td>\n",
       "      <td>-391430.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>May-2010</td>\n",
       "      <td>310503</td>\n",
       "      <td>379920.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       Date  Profit/Losses   changes\n",
       "0  Jan-2010         867884       NaN\n",
       "1  Feb-2010         984655  116771.0\n",
       "2  Mar-2010         322013 -662642.0\n",
       "3  Apr-2010         -69417 -391430.0\n",
       "4  May-2010         310503  379920.0"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#show changes \n",
    "data_file_df['changes'] = changes\n",
    "data_file_df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "25"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#finds index of max change\n",
    "max_index=data_file_df[\"changes\"].idxmax()\n",
    "max_index\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "44"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#finds index of min change\n",
    "min_index=data_file_df[\"changes\"].idxmin()\n",
    "min_index"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Feb-2012'"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#uses max index to find date\n",
    "max_date=data_file_df[\"Date\"][max_index]\n",
    "max_date\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Sep-2013'"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#uses min index to find date\n",
    "min_date=data_file_df[\"Date\"][min_index]\n",
    "min_date\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "-2196167.0"
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#uses min index to find date\n",
    "min_money=data_file_df[\"changes\"][min_index]\n",
    "min_money\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1926159.0"
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "max_money = data_file_df[\"changes\"][max_index]\n",
    "max_money"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Financial Analysis\n",
      "====================\n",
      "Total Months: 86\n",
      "Total: 38382578\n",
      "Average Change: -2315.12\n",
      "Greatest Increase in Profits: Feb-2012 1926159.0\n",
      "Greatest Increase in Profits: Feb-2012 1926159.0\n"
     ]
    }
   ],
   "source": [
    "print(\"Financial Analysis\")\n",
    "print(\"=\"*20)\n",
    "print(\"Total Months:\",total_months)\n",
    "print(\"Total:\",total)\n",
    "print(\"Average Change:\", str(round(mean_changes,2)))\n",
    "print(\"Greatest Increase in Profits:\",max_date,max_money)\n",
    "print(\"Greatest Increase in Profits:\",max_date,max_money)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "  Financial Analysis\n",
    "  ----------------------------\n",
    "  Total Months: 86\n",
    "  Total: $38382578\n",
    "  Average  Change: $-2315.12\n",
    "  Greatest Increase in Profits: Feb-2012 ($1926159)\n",
    "  Greatest Decrease in Profits: Sep-2013 ($-2196167)\n"
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
