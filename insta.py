# import
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint
import pandas as pd

# web driver
chromedriver_path = r'C:\Users\Vignesh Karunagaran\AppData\Local\Programs\Python\Python37-32\Chrome Driver\newDriver\chromedriver.exe'  # Change this to your own chromedriver path!
webdriver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(2)
webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(3)

# 1_login===================================================================================
# User name password
username = webdriver.find_element_by_name('username')
username.send_keys('username')
password = webdriver.find_element_by_name('password')
password.send_keys('yourpassword')
sleep(3)
# click on login
button_login = webdriver.find_element_by_xpath(
    '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button/div')
button_login.click()
sleep(5)
print('[DEBUG]  Login Success')
# verification Code
verificationCode = webdriver.find_element_by_name('verificationCode')
code = input('Verification code:\n')
verificationCode.send_keys(code)
# click on confirm
button_confirm = webdriver.find_element_by_xpath(
    '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/button')
button_confirm.click()
sleep(5)
print('[DEBUG]  Verification Success')

try:
    webdriver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]').click()
    print('[DEBUG]  Not now Success')
except:
    pass

hashtag_list = ['shutterbug', 'note5pro', 'traveler']
prev_user_list = []  # if it's the first time you run it, use this line and comment the two below
# prev_user_list = pd.read_csv('20181203-224633_users_followed_list.csv', delimiter=',').iloc[:,1:2]  # useful to build a user log
# prev_user_list = list(prev_user_list['0'])
print('[DEBUG]  Hashtags :',hashtag_list)
new_followed = []
tag = -1
followed = 0
likes = 0
comments = 0

runStaus = 1

for hashtag in hashtag_list:
    if runStaus:
        print('[DEBUG]  Hashtag :',hashtag)
        tag += 1
        webdriver.get('https://www.instagram.com/explore/tags/' + hashtag_list[tag] + '/')
        sleep(5)
        # first Tumbnail
        first_thumbnail = webdriver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div/div[2]')
        first_thumbnail.click()
        sleep(5)
        while (True):
            # username
            username = webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[1]/h2/a').text
            if username not in prev_user_list:
                decison = input('should i Like|Next|Next HashTag|Close [l,n,h,c]?\n').lower()
                if decison == 'l':
                    print('[DEBUG]  Choice made : LIKE')
                    # If we already follow, do not unfollow
                    if webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').text == 'Follow':
                        webdriver.find_element_by_xpath(
                            '/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').click()
                        new_followed.append(username)
                        followed += 1
                        print('[DEBUG]  Follow Success')
                        # Liking the picture
                        button_like = webdriver.find_element_by_xpath(
                            '/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button/span')
                        button_like.click()
                        likes += 1
                        print('[DEBUG]  Like Success')
                        sleep(5)
                        #TODO comment part
                        '''
                        
                        # Comments and tracker
                        comm_prob = randint(1, 10)
                        # print('{}_{}: {}'.format(hashtag, x, comm_prob))
                        if comm_prob > 7:
                            comments += 1
                            # webdriver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/article/div[2]/section[1]/span[2]/button/span').click()
                            comment_box = webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/textarea')

                            if (comm_prob < 7):
                                comment_box.send_keys('Really cool!')
                                sleep(1)
                            elif (comm_prob > 6) and (comm_prob < 9):
                                comment_box.send_keys('Nice work :)')
                                sleep(1)
                            elif comm_prob == 9:
                                comment_box.send_keys('Nice gallery!!')
                                sleep(1)
                            elif comm_prob == 10:
                                comment_box.send_keys('So cool! :)')
                                sleep(1)
                            # Enter to post comment
                            comment_box.send_keys(Keys.ENTER)
                            print('[DEBUG]  Comment Success')
                            sleep(5)
                            '''

                    # Next picture
                    webdriver.find_element_by_link_text('Next').click()
                    sleep(5)
                    print('[DEBUG]  Next Success')
                elif decison == 'n':
                    print('[DEBUG]  Choice made : NEXT')
                    webdriver.find_element_by_link_text('Next').click()
                    print('[DEBUG]  Next Success')
                    sleep(5)
                elif decison == 'c':
                    print('[DEBUG]  Choice made : Close')
                    for n in range(0, len(new_followed)):
                        prev_user_list.append(new_followed[n])

                    updated_user_df = pd.DataFrame(prev_user_list)
                    updated_user_df.to_csv('{}_users_followed_list.csv'.format(strftime("%Y%m%d-%H%M%S")))
                    print('[DEBUG]  Summary')
                    print('Liked {} photos.'.format(likes))
                    print('Commented {} photos.'.format(comments))
                    print('Followed {} new people.'.format(followed))
                    runStaus = 0
                    break
                elif decison == 'h':
                    print('[DEBUG]  Choice made : NEXT HASHTAG')
                    break
            else:
                webdriver.find_element_by_link_text('Next').click()
                sleep(6)

if runStaus == 1:
    for n in range(0, len(new_followed)):
        prev_user_list.append(new_followed[n])

    updated_user_df = pd.DataFrame(prev_user_list)
    updated_user_df.to_csv('{}_users_followed_list.csv'.format(strftime("%Y%m%d-%H%M%S")))
    print('Liked {} photos.'.format(likes))
    print('Commented {} photos.'.format(comments))
    print('Followed {} new people.'.format(followed))

