import nltk
from textblob import TextBlob
from newspaper import Article
import tkinter as tk

def summarize():

    #nltk.download('punkt')

    url = urltext.get('1.0', 'end').strip()
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()

    title.config(state='normal')
    author.config(state='normal')
    publication.config(state='normal')
    summary.config(state='normal')
    sentiment.config(state='normal')

    title.delete('1.0', 'end')
    title.insert('1.0', article.title)

    author.delete('1.0', 'end')
    author.insert('1.0', article.authors)

    publication.delete('1.0', 'end')
    publication.insert('1.0', article.publish_date)

    summary.delete('1.0', 'end')
    summary.insert('1.0', article.summary)

    blob = TextBlob(article.text)
    sentiment.delete('1.0', 'end')
    sentiment.insert('1.0', f'Sentiment: {"Positive" if blob.polarity > 0 else "Negative" if blob.polarity < 0 else "Neutral"}')

    title.config(state='disabled')
    author.config(state='disabled')
    publication.config(state='disabled')
    summary.config(state='disabled')
    sentiment.config(state='disabled')


#GUI using Tkinter
root = tk.Tk()
root.title('News Summarizer')
root.geometry('1280x650')

titlelabel = tk.Label(root, text='Title')
titlelabel.pack()

title = tk.Text(root, height=1, width=140)
title.config(state='disabled', bg='#dddddd')
title.pack()

authlabel = tk.Label(root, text='Author')
authlabel.pack()

author = tk.Text(root, height=1, width=140)
author.config(state='disabled', bg='#dddddd')
author.pack()

publicationlabel = tk.Label(root, text='Publication')
publicationlabel.pack()

publication = tk.Text(root, height=1, width=140)
publication.config(state='disabled', bg='#dddddd')
publication.pack()

summarylabel = tk.Label(root, text='Summary')
summarylabel.pack()

summary = tk.Text(root, height=20, width=140)
summary.config(state='disabled', bg='#dddddd')
summary.pack()

sentimentlabel = tk.Label(root, text='Sentiment')
sentimentlabel.pack()

sentiment = tk.Text(root, height=1, width=140)
sentiment.config(state='disabled', bg='#dddddd')
sentiment.pack()

urllabel = tk.Label(root, text='URL')
urllabel.pack()

urltext = tk.Text(root, height=1, width=140)
urltext.pack()

btn = tk.Button(root, text='Summarize Article', command=summarize)
btn.pack()

root.mainloop()


