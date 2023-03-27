from asyncio.windows_events import NULL
import streamlit as st
# import pandas as pd 
import streamlit.components.v1 as stc
# from datetime import date
# import plotly.express as px
from func import *
from streamlit_extras.mention import mention
from streamlit_extras.let_it_rain import rain
from streamlit_extras.no_default_selectbox import selectbox
import time


def main():
	
	user_list = ["Virat Kohli","Greta Thunberg","Sundar Pichai", "Samay Raina"]
	st.set_page_config(page_title="TweetPress", page_icon="🦉", layout="centered", initial_sidebar_state="expanded")

	page_bg_img = '''
	<style>
	body {
	background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366");
	background-size: cover;
	}
	</style>
	'''

	st.markdown(page_bg_img, unsafe_allow_html=True)

	st.markdown(""" <style>
	#MainMenu {visibility: hidden;}
	footer {visibility: hidden;}
	</style> """, unsafe_allow_html=True)

	st.sidebar.title("TweetPress🦉")

	menu = ["Home","Search News","Creators"]
	choice = st.sidebar.radio(" ",menu)

	if choice == "Home":
		st.title("TweetPress🦉")
		st.header("Welcome to TweetPress!!")
		st.text("We are dedicated to recommending the latest and most interesting news articles!")
		my_expander1 = st.expander("**What is TweetPress?**")
		my_expander1.write("TweetPress is a news recommendation system that recommends the latest and most interesting news articles to the user based on their interests. The user can input Twitter handles and the system then recommends the latest news articles based on the user's interests.")
		my_expander2 = st.expander("**How does it work?**")
		my_expander2.write("The system uses the Twitter API to fetch the latest tweets from the user's Twitter handle. The system then uses Newsapi.org to fetch the recent news articles. The system then recommends the latest news articles to the user based on their twitter activity.")
		my_expander3 = st.expander("**How to use TweetPress?**")
		my_expander3.write("To use TweetPress, you can enter a Twitter handle, the number of news articles you want to see and the evaluation metric you would want to use for extracting the relevant news articles. Then you can view the latest news articles recommended to you.")

	# elif choice == "New User":
	# 	st.subheader("Enter your Details:")
	# 	bname = st.text_input("Name")
	# 	bemail = st.text_input("Email")
	# 	btwitterid = st.text_input("Twitter ID")
	# 	if st.button("Register"):
	# 		add_new_user(bname, bemail, btwitterid)
	# 		st.warning("Hi {}! You are registered as a new user".format(bname))
	# 		st.warning("Please Login to get the latest news articles!")

	elif choice == "Search News":
		st.subheader("Enter Relevant Details:")
		# stwitterid = st.text_input("Twitter ID")

		twitter_id = selectbox("Select a Twitter ID", user_list)

		e_metric = selectbox("Select an option", ["Jaccard Coefficient","Binary Weighting Scheme","Raw Count Weighting Scheme", "Term Frequency Weighting Scheme", "Log Normalization Weighting Scheme", "Double Normalization Weighting Scheme"])
		# if e_metric == "Jaccard Coefficient":
		# 	st.write('You selected Jaccard Coefficient.')
		# elif e_metric == "Binary Weighting Scheme":
		# 	st.write("You selected Binary Weighting Scheme.")
		# elif e_metric == "Raw Count Weighting Scheme":
		# 	st.write("You selected Raw Count Weighting Scheme.")
		# elif e_metric == "Term Frequency Weighting Scheme":
		# 	st.write("You selected Term Frequency Weighting Scheme.")
		# elif e_metric == "Log Normalization Weighting Scheme":
		# 	st.write("You selected Log Normalization Weighting Scheme.")
		# elif e_metric == "Double Normalization Weighting Scheme":
		# 	st.write("You selected Double Normalization Weighting Scheme.")
		
		# number_news = st.slider('How many news do you want?', 8, 12)
		number_news = st.number_input('How many news articles do you want?', 8,12)

		if st.button("Search"):
			with st.spinner('Loading News Articles...'):
				rain(emoji="📰", font_size=45, falling_speed=5, animation_length="1")
				time.sleep(8)
			
			qvector = get_query_vector(twitter_id)
			similarity_matrix = helper_1(e_metric, qvector)
			top_x_news = recommend_top_10_articles(similarity_matrix, number_news)

			st.subheader("Here are the top %d news articles for you:" % number_news)
			for i in range(len(top_x_news)):
				st.write(top_x_news[i][2], "[🔗](%s)" % top_x_news[i][1])

			# temp = get_user_data(twitter_id)
			# if(temp == -1):
			# 	st.warning("Invalid Credentials")
			# else:
			# 	st.subheader("Here are the latest news articles for you:")
			# 	news_list = get_news_articles(stwitterid)
			# 	for i in range(len(news_list)):
			# 		st.write(news_list[i][0], "[link](%s)" % news_list[i][1])


	elif choice == "Creators":
		tab1, tab2, tab3, tab4, tab5 = st.tabs(["Kartik Jain", "Manas Agarwal", "Rishabh Oberoi", "Uttkarsh Singh", "Darsh Parikh"])
		with tab1:
			st.header("Kartik Jain")
			st.image("photos\kartik_jain.jpeg",width=250)
			st.write("I am a third-year Computer Science and Social Science Undergraduate at IIIT Delhi. I am an academically goal-driven individual who has strong problem-solving skills. I am open to new experiences and opportunities.")
			st.write("Socials:")
			mention(label="Github",icon="github",  url="https://github.com/Kartik20440")
			mention(label="Linkedin",icon="https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/LinkedIn_logo_initials.png/900px-LinkedIn_logo_initials.png?20140125013055",  url="https://www.linkedin.com/in/kartikxjain/")
			st.write("kartik20440@iiitd.ac.in")

		with tab2:
			st.header("Manas Agarwal")
			st.image("photos\manas_agarwal.jpg", width=250)
			st.write("I am a 3rd Year Undergrad at IIIT Delhi pursuing a Bachelor of Technology majoring in Computer Science.\nI love playing with Data Structures and Algorithms and am highly interested in Problem Solving.\nI am working as a researcher with MIDAS labs and also a Teaching Assistant at IIITD.")
			st.write("Socials:")
			mention(label="Github",icon="github",  url="https://github.com/manas20443")
			mention(label="Linkedin",icon="https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/LinkedIn_logo_initials.png/900px-LinkedIn_logo_initials.png?20140125013055",  url="https://www.linkedin.com/in/manas-agarwal-a63170215/")
			st.write("manas20443@iiitd.ac.in")
		
		with tab3:
			st.header("Rishabh Oberoi")
			st.image("photos\Rishabh_oberoi.jpg", width=200)
			st.write("As a passionate 3rd year Computer Science student, I love exploring the fascinating worlds of data structures and algorithms, mathematics, and cognitive science. \nI find it thrilling to dive deep into complex concepts and uncover their practical applications, always striving to learn and grow as a problem-solver.")
			st.write("Socials:")
			mention(label="Github",icon="github",  url="https://github.com/Rishabh459")
			mention(label="Linkedin",icon="https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/LinkedIn_logo_initials.png/900px-LinkedIn_logo_initials.png?20140125013055",  url="https://www.linkedin.com/in/rishabh-oberoi-327837229/")
			st.write("rishabh20459@iiitd.ac.in")

		with tab4:
			st.header("Uttkarsh Singh")
			st.image("photos\\utkarsh_singh.jpeg", width=250)
			st.write("As a junior at IIIT Delhi, I have a strong interest in data structures and algorithms, and I am passionate about solving real-world problems through programming. I have completed several projects where I have applied my skills in software development.")
			st.write("Socials:")
			mention(label="Github",icon="github",  url="https://github.com/uttkxrrsh")
			mention(label="Linkedin",icon="https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/LinkedIn_logo_initials.png/900px-LinkedIn_logo_initials.png?20140125013055",  url="https://www.linkedin.com/in/uttkarshsingh/")
			st.write("uttkarsh20479@iiitd.ac.in")
		
		with tab5:
			st.header("Darsh Parikh")
			st.image("photos\darsh_parikh.jpg", width=250)
			st.write("I am a 3rd-year student at IIIT Delhi pursuing B.Tech in Computer Science and Artificial Intelligence. I like solving problems related to data structures and also like to play around with ML models on various datasets. I am currently open to interning for software development engineer roles and AI/Ml-related work.")
			st.write("Socials:")
			mention(label="Github",icon="github",  url="https://github.com/darsh20560")
			mention(label="Linkedin",icon="https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/LinkedIn_logo_initials.png/900px-LinkedIn_logo_initials.png?20140125013055",  url="https://www.linkedin.com/in/darsh-parikh-dp/")
			st.write("darsh20560@iiitd.ac.in")


if __name__ == '__main__':
	main()
