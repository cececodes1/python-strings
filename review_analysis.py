#Task 1: Keyword Highlighter

reviews = [ "This product is really Good, Im impressed with it's quality.", "The performance of this product is Excellent, highly recommended!", 
           "I had a Bad experience with this product, it didn't meet my expectations.", 
           "Poor quality product, wouldn't recommend it to anyone","The product was Average, nothing extraordinary about it." ]
# Defining the keywords to highlight
keywords = ["good", "excellent", "bad", "poor", "average"]
# Loops through each review
for review in reviews:
# Loops through each keyword
    for keyword in keywords:
# replace keywords with uppercase version
        review = review.replace(keyword, keyword.upper())
        print(review)  # Print the review with the keywords in uppercase

# Task 2: Sentiment Tally

positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]
# a function to tally the sentiment of the review
def sentiment_tally(review):
# Tallies for positive and negative
    positive_count = 0
    negative_count = 0
    if positive_word.lower() in positive_words:
# Increment the positive words
        positive_count += 1
    elif negative_word.lower() in negative_words:
# Decrement the negative words
        negative_count += 1
    return positive_count, negative_count

#Task 3: Review Summary

def review_summary(review):
    summary = review[:30]
    if len(summary) == 30:
        summary += "..."
    return summary

for review in reviews:
    print(review_summary(review))