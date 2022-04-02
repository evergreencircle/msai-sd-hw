from flask import Flask, render_template, request, redirect, url_for
import datetime

class Post():
    
    def __init__(self, postId, header, body, timestamp):
        self.postId = postId
        self.header = header
        self.body = body
        self.timestamp = timestamp
        

app = Flask(__name__)
posts = []


@app.route('/main.html')
@app.route('/')
def index():
    return render_template("main.html", posts=posts)


@app.route('/newPost')
def newPost():
    return render_template("newPost.html")


@app.route('/post/<int:postId>')
def showPost(postId):
    return render_template("post.html", post=posts[postId])


@app.route('/savePost', methods=['POST'])
def savePost():

    if request.form['postheader'] and request.form['postbody']:
        post = Post(len(posts), request.form['postheader'], request.form['postbody'], datetime.datetime.utcnow())
        posts.append(post)
        return redirect(url_for("index"))
    else:
        return newPost()

if __name__ == "__main__":
    app.run(debug=True)