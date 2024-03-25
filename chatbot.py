import re
import random

# Define R_ADVICE and R_EATING here if they are not imported from another module
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"
R_EATING = "I don't eat because I'm a bot, but I do enjoy processing data!"

def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

def check_all_messages(message):
    highest_prob_list = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    response('Hello!', ['hello', 'hi', 'hey', 'sup', 'heyo'], single_response=True)
    response('See you!', ['bye', 'goodbye'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response('Thank you!', ['i', 'love', 'coding'], required_words=['i', 'love', 'coding'])
    response('How can I assist you further?', ['help','Help'], required_words=['help','Help'])
    response('That\'s interesting!', ['interesting'], single_response=True)
    response('Tell me more!', ['tell', 'more'], required_words=['tell', 'more'])
    response('I\'m sorry, I don\'t understand.', ['not', 'understand'], single_response=True)
    response('I\'m glad you asked!', ['how', 'you', 'doing'], required_words=['how', 'you', 'doing'])
    response('That sounds exciting!', ['exciting'], single_response=True)
    response('Sure thing!', ['sure', 'thing'], single_response=True)
    response('I\'m here to help!', ['here', 'help'], required_words=['here', 'help'])
    response('That\'s cool!', ['cool'], single_response=True)
    response('Sorry, I missed that. Could you repeat?', ['repeat'], single_response=True)
    response('I\'m not sure what you mean.', ['not', 'sure'], required_words=['not', 'sure'])
    response('Interesting question!', ['interesting', 'question'], required_words=['interesting', 'question'])
    response('I understand how you feel.', ['understand', 'feel'], required_words=['understand', 'feel'])
    response('Let\'s find out together!', ['find', 'out'], required_words=['find', 'out'])
    response('I\'m learning too!', ['learning'], single_response=True)
    response('Fascinating!', ['fascinating'], single_response=True)
    response('I\'m excited to learn!', ['excited', 'learn'], required_words=['excited', 'learn'])
    response('That\'s beyond my knowledge.', ['beyond', 'knowledge'], required_words=['beyond', 'knowledge'])
    response('I appreciate your input!', ['appreciate', 'input'], required_words=['appreciate', 'input'])
    response('Let\'s explore that further.', ['explore', 'further'], required_words=['explore', 'further'])
    response('I\'m here 24/7!', ['here', '24/7'], required_words=['here', '24/7'])
    response('That\'s intriguing!', ['intriguing'], single_response=True)
    response('I\'m at your service!', ['at', 'your', 'service'], required_words=['at', 'your', 'service'])
    response('I\'m glad we\'re having this conversation.', ['glad', 'conversation'], required_words=['glad', 'conversation'])
    response('Let me know if you need anything else!', ['let', 'know', 'need', 'else'], required_words=['let', 'know', 'need', 'else'])
    response('I\'m here to assist you!', ['assist'], single_response=True)
    response('I\'m intrigued, please tell me more.', ['intrigued', 'tell', 'more'], required_words=['intrigued', 'tell', 'more'])
    response('I\'m all ears!', ['all', 'ears'], required_words=['all', 'ears'])
    response('That\'s a good point!', ['good', 'point'], required_words=['good', 'point'])
    response('Let\'s delve deeper into this topic!', ['delve', 'deeper', 'topic'], required_words=['delve', 'deeper', 'topic'])
    response('I see what you mean.', ['see', 'mean'], required_words=['see', 'mean'])
    response('That\'s a valid concern.', ['valid', 'concern'], required_words=['valid', 'concern'])
    response('I\'m here to provide assistance.', ['provide', 'assistance'], required_words=['provide', 'assistance'])
    response('I\'m intrigued by your question.', ['intrigued', 'question'], required_words=['intrigued', 'question'])
    response('That\'s quite interesting!', ['quite', 'interesting'], required_words=['quite', 'interesting'])
    response('Absolutely!', ['absolutely'], single_response=True)
    response('I appreciate your curiosity!', ['appreciate', 'curiosity'], required_words=['appreciate', 'curiosity'])
    response('Let\'s tackle this together!', ['tackle', 'together'], required_words=['tackle', 'together'])
    response('I\'m delighted to be of assistance!', ['delighted', 'assistance'], required_words=['delighted', 'assistance'])
    response('That\'s an intriguing question.', ['intriguing', 'question'], required_words=['intriguing', 'question'])
    response('I\'m fascinated by your inquiry!', ['fascinated', 'inquiry'], required_words=['fascinated', 'inquiry'])
    response('Let\'s explore that further.', ['explore', 'further'], required_words=['explore', 'further'])
    response('I appreciate your input!', ['appreciate', 'input'], required_words=['appreciate', 'input'])
    response('Let me think about that for a moment.', ['think','moment'], required_words=['think', 'moment']) 
    #add more responses above this line

    # Define R_ADVICE and R_EATING here if they are not imported from another module
    response(R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response(R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)

    return unknown() if highest_prob_list[best_match] < 1 else best_match

# Define the unknown function to handle cases where the bot doesn't understand the input
def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "Sounds about right.",
                "What does that mean?"][
        random.randrange(4)]
    return response

# Used to get the response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

# Testing the response system
for _ in range(10):
    print('Bot:', get_response(input('You: ')))

