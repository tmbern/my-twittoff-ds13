from flask import Blueprint, render_template, request, redirect
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from web_app.models import db, User, Tweet, parse_records
from web_app.services.basilica_service import connection as basilica_connection


stats_routes = Blueprint("stats_routes", __name__)

@stats_routes.route('/stats/iris')

def iris():
    X, y = load_iris(return_X_y=True)
    clf = LogisticRegression(random_state=0, solver='lbfgs', multi_class='multinomial').fit(X, y)
    results = str(clf.predict(X[:2, :]))
    return results

@stats_routes.route("/")
def twitoff_prediction_form():
    return render_template("prediction_form.html")
    
@stats_routes.route("/stats/predict", methods=["POST"])
def twitoff_prediction():
    print("FORM DATA:", dict(request.form))
    
    screen_name_a = request.form["screen_name_a"]
    screen_name_b = request.form["screen_name_b"]
    tweet_text = request.form["tweet_text"]

    # todo: train model
    # inputs: embeddings for each tweet
    # labels: screen name for each tweet

    user_a = User.query.filter(User.screen_name == screen_name_a).one()
    user_b = User.query.filter(User.screen_name == screen_name_b).one()
    user_a_tweets = user_a.tweets
    user_b_tweets = user_b.tweets

    embeddings = []
    labels = []
    all_tweets = user_a_tweets + user_b_tweets
    for tweet in all_tweets:
        embeddings.append(tweet.embedding)
        labels.append(tweet.user.screen_name)
    
    model = LogisticRegression()
    model.fit(embeddings, labels)

    example_embedding = basilica_connection.embed_sentence(tweet_text, model="twitter")
    results = model.predict([example_embedding])
    screen_name_most_likely = results[0]

    
    # todo: make prediction

    return render_template("prediction_results.html",
        screen_name_a=screen_name_a,
        screen_name_b=screen_name_b,
        tweet_text=tweet_text,
        screen_name_most_likely=screen_name_most_likely)
