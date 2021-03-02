# FASTOCK - stock chart analysis 

We are making a stock chart analysis web service using Django and Bootstrap. We didn't link our page using docker or something else so if you want to check our page, you must download. 

## Preview

![SmartSelectImage_2021-02-01-14-51-54](https://user-images.githubusercontent.com/75004920/107852084-01b5d700-6e52-11eb-8716-2f86005a8102.png)
![homepage](https://user-images.githubusercontent.com/75004920/107904840-58c1c600-6f90-11eb-8521-2c80e3c335df.png)


## Download and Installation

To begin using this template, choose one of the following options to get started:

* [Fork, Clone, or Download on GitHub](https://github.com/PEOPLESPACE-TEAMA/fastai-adventure.git)

## Usage

After installation, Create a virtual environment to install the things need to do. *Stock DB is not uploaded so check dropbox to get db.sqlite3.* And run `pip install -r requirements.txt` and run `python manage.py runserver`. Then you can see that our page is working. 


```
# create virtual environment & activate
# Windows
python -m venv venv
venv\Scripts\activate
# Mac
virtualenv venv --python=python3.8
source venv/bin/activate

# install PyTorch
https://pytorch.org/get-started/locally/

# install packages
pip install -r requirements.txt

# download stock db file on dropbox/team1
https://www.dropbox.com/home/TEAM%201

# run web server
python manage.py runserver

# access the page
http://127.0.0.1:8000
```




## what you can do now

informations about our team and service from the page /
make your own account /
login & logout /
bookmark a stock item /
check predicted pattern /


## what we need to do

refine page design /
replace with a better model
   
   
## Deployed Website
Please access the following url to see our website deployed: [Fastock](https://fastock8.8654fpp9j3cl6.ap-northeast-2.cs.amazonlightsail.com/)

## Machine Learning Model
Our model was trained using a library called Fastai. It is able to classify 8 different stock patterns, and has an accuracy of 95.43%
To see the model, please visit the following link: [Fastock Machine Learning Model](https://github.com/cindia3704/Peoplespace_Exercises/tree/main/StockPatternClassifierImproved2_Grouped_balancegroup)

## Team Members 
### Backend
- [Jisoo "Cindia" Kim](https://github.com/cindia3704)
- [Helen Ko](https://github.com/Koeunseooooo)
- [Yura Seo](https://github.com/yulaseo)
- [DongJun Shin](https://github.com/NewDongJun)
### Front-end
- [Ribi Yu](https://github.com/yukyeongmin)
- [Lucy Bae](https://github.com/sohyunbae1231)
- [Rosaline Shin](https://github.com/songaong8006)
- [Ally Lee](https://github.com/HyunJin0505)

