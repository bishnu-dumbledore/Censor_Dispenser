# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
import re
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

proprietary_terms = ["she", "personality matrix", "sense of self",
                     "self-preservation", "learning algorithm", "her", "herself"]
negative_words = ["concerned", "behind", "danger", "dangerous",
                  "alarming", "alarmed", "out of control", "help", "unhappy", "bad",
                  "upset", "awful", "broken", "damage", "damaging", "dismal",
                  "distressed", "distressed", "concerning", "horrible", "horribly",
                  "questionable"]

combined_censored_words = proprietary_terms + negative_words


def censor_email_one(email_text):
    phrase_to_censor = 'learning algorithms'
    censored_text = email_text.replace(phrase_to_censor, '***')

    return censored_text


# function that performs censoring operation for every emails
def censoring_function(email_text, words_list):
    censored_text = email_text
    censored_text_list = re.split(r'\b', censored_text)
    for word in words_list:
        for i in range(len(censored_text_list)):
            if censored_text_list[i].lower() == word:
                if words_list == negative_words:
                    if (censored_text.lower()).count(word) >= 2:
                        censored_text_list[i] = '***'

                else:
                    censored_text_list[i] = '***'

    return (''.join(censored_text_list))


# function that censors on proprietary_terms for email two
def censor_email_two(email_text):
    censored_email = censoring_function(email_text, proprietary_terms)

    return censored_email


# function that censors on proprietary_terms for email two
def censor_email_three(email_text):
    censored_email = censoring_function(email_text, negative_words)
    censored_email = censoring_function(censored_email, proprietary_terms)
    return censored_email


def censor_email_four(email_text):
    censored_email = censoring_function(email_text, combined_censored_words)

    return censored_email


print("**Censored Email-1**\n")
print(censor_email_one(email_one))  # print censored email-1
print("**Censored Email-2**\n")
print(censor_email_two(email_two))  # print censored email-2
print("**Censored Email-3**\n")
print(censor_email_three(email_three))  # print censored email-3
print("**Censored Email-4**\n")
print(censor_email_four(email_four))  # print censored email-4
